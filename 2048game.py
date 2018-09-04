"""
My clone of 2048 game.  To play, visit:
http://www.codeskulptor.org/#user43_8mjXJOeGxv_28.py
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):

    """
    Helper function that merges a single row or column in 2048
    """

    already_combined = False
    copy_list = []
    for item in line:
        if item is not 0:
            if len(copy_list) == 0:
                copy_list.append(item)

            elif item == copy_list[len(copy_list)-1] and not already_combined:
                copy_list[len(copy_list)-1] = copy_list[len(copy_list)-1] * 2
                already_combined = True

            else:
                copy_list.append(item)
                already_combined = False

    if len(copy_list) < len(line):
        difference = len(line) - len(copy_list)
        for dummy_num in range(difference):
            copy_list.append(0)
    return copy_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width

        self.reset()

        self._indices = {}
        dummy_up_indices = []
        for dummy_count in range(self._grid_width):
            dummy_up_indices.append((0, dummy_count))
        self._indices[UP] = dummy_up_indices

        dummy_left_indices = []
        for dummy_count in (range(self._grid_height)):
            dummy_left_indices.append((dummy_count, 0))
        self._indices[LEFT] = dummy_left_indices

        dummy_down_indices = []
        for dummy_count in (range(self._grid_width)):
            dummy_down_indices.append((grid_height-1, dummy_count))
        self._indices[DOWN] = dummy_down_indices

        dummy_right_indices = []
        for dummy_count in (range(self._grid_height)):
            dummy_right_indices.append((dummy_count, self._grid_width-1))
        self._indices[RIGHT] = dummy_right_indices


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                           for dummy_row in range(self._grid_height)]

        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        show = ""
        for item in self._grid:
            for loc in item:
                show += str(loc)

        return show

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        height = self._grid_height
        return height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        width = self._grid_width
        return width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        was_moved = False
        move = OFFSETS[direction]
        starting_index = self._indices[direction]
        if direction in (1, 2):
            steps = self._grid_height
        elif direction in (3, 4):
            steps = self._grid_width

        else:
            print "Not a valid move"

        for loc in starting_index:
            new_list = []
            for step in range(steps):
                val = self._grid[loc[0] + step*move[0]][loc[1] + step*move[1]]
                new_list.append(val)
            print "new list:  ", new_list
            replacement_list = merge(new_list)
            print "replacement list ", replacement_list
            step = 0
            if replacement_list != new_list:
                was_moved = True
                print "we've got one!"
                for item in replacement_list:
                    self._grid[loc[0] + step*move[0]][loc[1] + step*move[1]] = item
                    step += 1
        if was_moved == True:
            self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_num = random.randrange(0, 10)
        if new_num == 9:
            new_num = 4
        else:
            new_num = 2
        #row_place = random.randrange(0, self._grid_height)
        #col_place = random.randrange(0, self._grid_width)
        #self.spot = [row_place, col_place]
        spot = [random.randrange(0, self._grid_height), random.randrange(0, self._grid_width)]
        #print "spot is:  ", self.spot
        #print "here is a new number and its spot"
        if self._grid[spot[0]][spot[1]] == 0:
            self.set_tile(spot[0], spot[1], new_num)
            return
        else:
            self.new_tile()

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        val_to_return = self._grid[row][col]
        return val_to_return



#test_move()

#print str(test_str_())
#test_get_tile()
#print test_reset()
#print "testing new tile:  ", test_new_tile()
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
