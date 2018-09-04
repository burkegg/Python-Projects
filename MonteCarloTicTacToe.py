"""
Monte Carlo Tic-Tac-Toe Player
A project from a class that I took.
It uses Monte Carlo Methods to play against you.
Run here:
http://www.codeskulptor.org/#user43_yFJi0DQfZg_36.py

"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
NTRIALS = 250         # Number of trials to run
SCORE_CURRENT = 3.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player
SIZE = 3

def mc_trial(board, player):
    """
    takes the board and next player.
    plays a game from board, makes random moves, 
    returns when game is over.  Does not return anything.
    modified board contains state of board.
    """
    
    empties = board.get_empty_squares()        
    random.shuffle(empties)
    
    for empty in empties:
        board.move(empty[0], empty[1], player)
        player = provided.switch_player(player)
        if board.check_win() in (2, 3, 4):
            return

    if board.check_win() in (2, 3, 4):
        return
    

def mc_update_scores(scores, board, player):
    """
    Grid of values list of lists
    completed board
    the machine's label - x or o    
    Updates scores grid - returns None
    X = 2
    O = 3
    draw = 4
    """

    empty_squares = board.get_empty_squares()
    to_judge = []
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            loc = (row, col)
            if loc not in empty_squares:
                to_judge.append(loc)
    if board.check_win() == 4:
        return
    elif board.check_win() == player:

        for spot in to_judge:
            if board.square(spot[0], spot[1]) == player:
                scores[spot[0]][spot[1]] += SCORE_CURRENT
            elif board.square(spot[0], spot[1]) != player:
                scores[spot[0]][spot[1]] -= SCORE_OTHER   

    elif board.check_win() != player:
        for spot in to_judge:
            if board.square(spot[0], spot[1]) != player:
                scores[spot[0]][spot[1]] += SCORE_OTHER
            elif board.square(spot[0], spot[1]) == player:
                scores[spot[0]][spot[1]] -= SCORE_CURRENT

    
def get_best_move(board, scores):
    """
    takes actual board
    takes scores
    looks for all maxima
    returns a random maximum
    """
    choices=[]
    maxim = -NTRIALS * SCORE_CURRENT
    empties = board.get_empty_squares()
    if len(empties) == 1:
        return empties[0]
    
    for empty in empties:
        score = scores[empty[0]][empty[1]]
        if score > maxim:
            maxim = score
            print "maximum is: ", maxim
            choices = []
            choices.append(empty)
            print "choices are: ", choices
        elif score == maxim:
            choices.append(empty)
    loc = random.choice(choices)
    return loc

def mc_move(board, player, trials):
    """
    current board, which is machine, # of trials
    does the whole MC above, and yields (row, col)
    returns the loc from get_best_move
    """
    print "NTRIALS IS: ", NTRIALS
    print "starting board: " , '\n', board
    scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_num in range(trials):
        copy = board.clone()
        mc_trial(copy, player)
        mc_update_scores(scores, copy, player)
    return get_best_move(board, scores)
      
    
poc_ttt_gui.run_gui(3, provided.PLAYERO, mc_move, NTRIALS, False)
