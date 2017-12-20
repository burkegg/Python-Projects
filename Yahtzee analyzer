"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
Looks at current hand, determines optimum holds.
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    maximum = 0
    counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for die in hand:
        if die not in counts:
            break
        counts[die] += die
        
    for val in counts:
        if counts[val] > maximum:
            maximum = counts[val]        
    print counts
    return maximum


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    expected = 0
    maxes = []
    outcome_list = []
    for sequence in gen_all_sequences(range(1, (num_die_sides+1)), num_free_dice):
        state = []
        for die in held_dice:
            state.append(die)
        for num in sequence:
            state.append(num)
        outcome_list.append(state)
        
    for state in outcome_list:
        tallies = dict()
        for num in state:
            tallies[num] = (state.count(num)* num)
        maxis = 0
        for key in tallies:
            if tallies[key] > maxis:
                maxis = tallies[key]
        maxes.append(maxis)
    for dummy_entry in maxes:
        expected += dummy_entry / float((len(maxes)))
    
    return expected       

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([()])
    answer_set2 = set([()])

    final = [(),]
    #counter = 0
    
        
    for idx in range(0, len(hand), 1):
        final.append(tuple([idx]))
        
    for toops in final:
        for dummy_num in range(0, len(hand)):
            if dummy_num not in toops:
                new_toop = toops + tuple([dummy_num])
                lis = sorted(new_toop)
                new_toop2 = tuple(lis)
                if new_toop2 not in final:
                    final.append(new_toop2)
    for tup in final:
        sorted(tup)
        if tup not in answer_set:
            answer_set.add(tup)

           
    for toop in answer_set:
        temp_toop = []
        for idx in toop:
            temp_toop.append(hand[idx])
        answer_set2.add(tuple(temp_toop))
            
            
    return answer_set2
        
def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    highest_value = 0
    for hold in gen_all_holds(hand):
        free = len(hand)-len(hold)
        #print hold, len(hold), free
        temp_val = expected_value(hold, num_die_sides, free)
        #print temp_val
        if temp_val > highest_value:
            highest_value = temp_val
            to_hold = hold
    return (highest_value, to_hold)

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (5, 3)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    print score(hand)
    gen_all_sequences([5, 3, 2], 2)
    
    print gen_all_holds(hand)
    
    
    gen_all_holds(hand)
       # print obj
run_example()
#num_die_sides = 6
#hand = (5, 3, 2, 6, 1)
#print strategy(hand, num_die_sides)
