"""
Cookie Clicker Simulator
Burke Green
http://www.codeskulptor.org/#user43_UKa7CPzKMh_80.py
"""
import math
import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(50)

import poc_clicker_provided as provided

# Constants
#SIM_TIME = 10000000000.0
SIM_TIME = 50000.0
class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._history = [(0.0, None, 0.0, 0.0)]
        self._total_cookies = 0.0
        self._ttime = 0.0
        self._cps = 1.0
        self._current_cookies = 0.0
        
    def __str__(self):
        """
        Return human readable state
        """
        my_string = '\n' + "you currently have " + str(self._current_cookies)+ '\n' + "You have made " + str(math.floor(self._total_cookies)) +"\n" + "the time is " + str(self._ttime) + "\n" + "and your cps is " + str(self._cps)
        
        return my_string
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._ttime
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        the_history = list(self._history)
        return the_history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        else:
            delta = cookies - self._current_cookies
            time_until = math.ceil(delta/self._cps)
        
        return time_until
    
    def wait(self, time):
        """
        Wait for given amount of time and update state
        Should do nothing if time <= 0.0
        """
        if time <= 0:
            return
        else:
            self._ttime += time
            self._total_cookies += self._cps * time
            self._current_cookies += self._cps*time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        history:  (time, item, cost of item, total cookies)
        """
        if self._current_cookies < cost:
            return
        else:
            self._cps += additional_cps
            self._current_cookies -= cost
            self._history.append((self._ttime, item_name, cost, self._total_cookies))
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    cstate = ClickerState()
    bld = build_info.clone()
    while cstate.get_time() <= duration:
        time_left = duration - cstate.get_time()
        # if time_left <= 0:
        #    break
        item_to_buy = strategy(cstate.get_cookies(), cstate.get_cps(),cstate.get_history(), time_left, bld)
        if item_to_buy == None:
            break
        if bld.get_cost(item_to_buy) > math.floor((cstate.get_cps()*time_left + cstate.get_cookies())):
            print "it's too expensive!"
            break
        delay = cstate.time_until(bld.get_cost(item_to_buy))
        cstate.wait(delay)
        cstate.buy_item(item_to_buy, bld.get_cost(item_to_buy), bld.get_cps(item_to_buy))
        bld.update_item(item_to_buy)
    # for item in cstate.get_history():
    #    print item
    time_to_wait = duration - cstate.get_time()
    if time_to_wait > 0:
        cstate.wait(time_to_wait)
    return cstate


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    shopping = []
    to_buy = build_info.build_items()
    cheapest_item = [' ', float('inf')]
    for item in to_buy:
        cost = build_info.get_cost(item)
        cps_incr = build_info.get_cps(item)        
        shopping.append([item, cost, cps_incr])
    for obj in shopping:
        #print obj
        if obj[1] < cheapest_item[1]:
            cheapest_item[0] = obj[0]
            cheapest_item[1] = obj[1]       
    if cheapest_item[1] > (float(cookies) + cps*time_left):
        return None
    else:
        return cheapest_item[0]

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    shopping = []
    to_buy = build_info.build_items()
    expensive = [None, 0]
    for item in to_buy:
        cost = build_info.get_cost(item)
        cps_incr = build_info.get_cps(item)
        #here only append if the cost is less than the expected income
        if cost < (cookies + time_left * cps):
            shopping.append([item, cost, cps_incr])
    if len(shopping) == 0:
        return None
    for obj in shopping:
        temp_list = []
        if obj[1] > expensive[1]:
            expensive[0] = obj[0]
            expensive[1] = obj[1]
        temp_list.append(expensive[0])
        temp_list.append(expensive[1])
    if expensive[1] > (float(cookies) + cps*time_left):
        return None
    else:
        return temp_list[0]


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    shopping = []
    to_buy = build_info.build_items()
    # print to_buy
    for item in to_buy:
        cost = build_info.get_cost(item)
        cps_incr = build_info.get_cps(item)        
        ratio = cost/cps_incr
        if cost < (cookies + cps*time_left):
            #lower is better
            ranking =  3.5 *(ratio) + .8 * ((cost-cookies)/cps)
            #print item, ranking
            #print ranking
            shopping.append([item, ranking])
    shopping.sort(key = lambda x: x[1])
    if len(shopping) > 1:
        if shopping[0][0] == 'Cursor' and shopping[0][1] > 200:
            shopping.pop(0)
        if shopping[0][0] == 'Grandma' and shopping[0][1] > 2000:
            shopping.pop(0)
        if shopping[0][0] == 'Farm' and shopping[0][1] > 5000:
            shopping.pop(0)
        if shopping[0][0] == 'Mine' and shopping[0][1] > 10000:
            shopping.pop(0)
        if shopping[0][0] == 'Factory' and shopping[0][1] > 10000:
            shopping.pop(0)
        if shopping[0][0] == 'Shipment' and shopping[0][1] > 90000:
            shopping.pop(0)
        if shopping[0][0] == 'Alchemy Lab' and shopping[0][1] > 900000:
            shopping.pop(0)
        #if shopping[0][0] == 'Portal' and shopping[0][1] > 1666666*10:
       #     shopping.pop(0)
    #print shopping
    if len(shopping) > 0:
        return shopping[0][0]
    else:
        return None        

        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    # run_strategy("cursor always", SIM_TIME, strategy_cursor_broken)
    # run_strategy("none", SIM_TIME, strategy_none)
run()


# mine 10000  36312694013.0   mine 50000   23293372197


#print 236623400404 - 480970360907
