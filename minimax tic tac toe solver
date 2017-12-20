"""
Mini-max Tic-Tac-Toe Player
Uses recursion to tie you at Tic Tac Toe.
Burke Green
Run at:

http://www.codeskulptor.org/#user43_WDpkEEutvg_1.py
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win():
        return 0, (-1, -1)
    empties = board.get_empty_squares()
    best_move = (0, (-1, -1))
    
    for empty in empties:
        copy = board.clone()
        copy.move(empty[0], empty[1], player)
        
        if copy.check_win():
            score = SCORES[copy.check_win()]
            winner = copy.check_win()
            
            
            if player == provided.PLAYERX and winner == provided.PLAYERX:
                best_move = (1, empty)
                return best_move
            elif player == provided.PLAYERX and score >= best_move[0]:
                best_move = (score, empty)
            elif player == provided.PLAYERO and winner == provided.PLAYERO:
                best_move = (score, empty)
                return best_move
            elif player == provided.PLAYERO and score <= best_move[0]:
                best_move = (score*SCORES[player], (empty))
            
        else:
            best_move = mm_move(copy, player = provided.switch_player(player))

        
    return best_move            
    

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


"""
print mm_move(provided.TTTBoard(2, False, [
            [provided.EMPTY, provided.EMPTY], 
            [provided.EMPTY, provided.EMPTY]]), 
        provided.PLAYERO) 
#expected score -1 but received (1, (0, 0))
#the_board = provided.TTTBoard(2, False, None)
#print mm_move(the_board, provided.PLAYERX)
"""
"""
print mm_move(provided.TTTBoard(3, False, [
            [provided.PLAYERX, provided.EMPTY, provided.EMPTY], 
            [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], 
            [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), 
                    provided.PLAYERX) 
"""
#returned bad move (-1, (2, 0))

"""
print mm_move(provided.TTTBoard(3, 
                          False, [
            [provided.PLAYERX, provided.PLAYERX, provided.EMPTY], 
            [provided.PLAYERX, provided.PLAYERO, provided.PLAYERO], 
            [provided.PLAYERO, provided.PLAYERO, provided.EMPTY]]), 
        provided.PLAYERX) 
"""
#returned bad move (1, (2, 0))

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
