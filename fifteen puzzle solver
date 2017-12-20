
"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors

Run using CodeSkulptor:
http://www.codeskulptor.org/#user43_GKpidah5Rn_0.py


"""
import codeskulptor
import poc_fifteen_gui
codeskulptor.set_timeout(60)
class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction
  
    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if self.get_number(target_row, target_col) != 0:
            return False
        
        for tile in range(target_col+1, self.get_width()):
            if (target_row, tile) != self.current_position(target_row, tile):
                return False
        for row in range(target_row + 1, self.get_height()):
            for col in range(self.get_width()):
                if (row, col) != self.current_position(row, col):
                    return False
                
        return True
    
    
    def bring_down(self, target_row, target_col, desired_row, board):
        """
        A helper function to bring the target tile down to the row 
        This should be called when 0 tile is on the target row.
        """
        print "inside bring down"
        print board
        bd_copy = board.clone()
        my_string = ""
        
        if bd_copy.current_position(0, 0)[0] > bd_copy.current_position(target_row, target_col)[0]:
            print "inside if"
            while bd_copy.current_position(0, 0)[0] > bd_copy.current_position(target_row, target_col)[0]:
                thread = "u"
                my_string += thread
                bd_copy.update_puzzle(thread)
        # In any case, 0 should be on top of the target tile.
        
        while bd_copy.current_position(target_row, target_col)[0] < desired_row:
            thread = "lddru"
            my_string += thread
            print thread
            bd_copy.update_puzzle(thread)
        
        return my_string

    def bring_right(self, target_row, target_col, desired_col, board):
        """
        A helper function that will bring a tile to the right.
        This should probably be called if the target tile is
        on the bottom row or the bring_it_down fnxn has already been called.
        This assumes the target tile is not on row0.
        """
        br_copy = board.clone()
        my_string = ""
        
        # First see if tile is on row0.  If so, bring down one.
        if br_copy.current_position(target_row, target_col)[0] == 0:
            # Go just below target tile
            while br_copy.current_position(0,0)[0] > br_copy.current_position(target_row, target_col)[0] + 1:
                thread = "u"
                my_string += thread
                br_copy.update_puzzle(thread)
            while br_copy.current_position(0,0)[1] > br_copy.current_position(target_row, target_col)[1]:
                thread = "l"
                my_string += thread
                br_copy.update_puzzle(thread)
            thread = "urd"
            my_string += thread
            br_copy.update_puzzle(thread)
            # Now zero should be adjacent to target, on the right.
             
        # If t0 is below target, go up.
        print br_copy
        if br_copy.current_position(0,0)[0] > br_copy.current_position(target_row, target_col)[0]:
            while br_copy.current_position(0,0)[0] > br_copy.current_position(target_row, target_col)[0]:
                # I just changed the above line by removing the + 1
                thread = "u"
                my_string += thread
                br_copy.update_puzzle(thread)
        
        # If t0 is on the same row, but not adjacent, get adjacent.
        if (br_copy.current_position(0,0)[0] == br_copy.current_position(target_row, target_col)[0] and
            br_copy.current_position(0,0)[1] > br_copy.current_position(target_row, target_col)[1] + 1):
            while br_copy.current_position(0,0)[1] > br_copy.current_position(target_row, target_col)[1] + 1:
                thread = "l"
                my_string += thread
                br_copy.update_puzzle(thread)
        #t0 should now be to the right, and adjacent to, target.
        
        thread = "l"
        my_string += thread
        br_copy.update_puzzle(thread)

        # Now loop around until target tile is in desired column
        while br_copy.current_position(target_row, target_col)[1] < desired_col:
            thread = "urrdl"
            my_string += thread
            br_copy.update_puzzle(thread)
        thread = "ur"
        my_string += thread
        br_copy.update_puzzle(thread)
        return my_string
    
    def bring_left (self, target_row, target_col, desired_col, board):
        """
        A helper function to bring tiles to the left of their current location.
        """
        
        bl_copy = board.clone()
        my_string = ""
        
        # First see if tile is on row0.  If so, bring down one.
        if bl_copy.current_position(target_row, target_col)[0] == 0:
            # Go just below target tile
            while bl_copy.current_position(0,0)[0] > bl_copy.current_position(target_row, target_col)[0] + 1:
                thread = "u"
                my_string += thread
                bl_copy.update_puzzle(thread)
            while bl_copy.current_position(0,0)[1] < bl_copy.current_position(target_row, target_col)[1]:
                thread = "r"
                print thread
                my_string += thread
                bl_copy.update_puzzle(thread)
            thread = "uld"
            my_string += thread
            bl_copy.update_puzzle(thread)
            # Now zero should be adjacent to target, on the left.
            
            
        # If 0 is below, go up to the target tile's row.
        if bl_copy.current_position(0,0)[0] > bl_copy.current_position(target_row, target_col)[0]:
            while bl_copy.current_position(0,0)[0] > bl_copy.current_position(target_row, target_col)[0]:
                thread = "u"
                print thread
                my_string += thread
                bl_copy.update_puzzle(thread)
            
        # If t0 is not adjacent to the target, go right until it is.
        if  bl_copy.current_position(0,0)[1] < bl_copy.current_position(target_row, target_col)[1] + 1:
            while bl_copy.current_position(0,0)[1] >= bl_copy.current_position(target_row, target_col)[1] + 1:
                thread = "r"
                my_string += thread
                bl_copy.update_puzzle(thread)

        # t0 should now be directly left of target tile.
        
        thread = "r"
        my_string += thread
        bl_copy.update_puzzle(thread)
        
        while bl_copy.current_position(target_row, target_col)[1] > desired_col:
            thread = "ulldr"
            print thread
            my_string += thread
            bl_copy.update_puzzle(thread)
            print bl_copy , "bl_copy2"

        thread = "ul"
        my_string += thread
        bl_copy.update_puzzle(thread)
        return my_string
        
        
    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # check valid intro to function
        assert self.lower_row_invariant(target_row, target_col), "failed at solve_interior beginning"
        assert target_col > 0, "Don't use that method here:  column is zero?"
        assert target_row > 1, "Don't use that method here:  row is 0 or 1?"
        copy = self.clone()
        my_string = ""
        print "info"
        print copy.current_position(target_row, target_col)
        print target_row, target_col
        if copy.current_position(target_row, target_col)[1] > target_col:
            thread = copy.bring_left(target_row, target_col, target_col, copy)
            my_string += thread
            copy.update_puzzle(thread)
            print "bringing left?"
            print copy
        if copy.current_position(target_row, target_col)[1] < target_col:
            thread = copy.bring_right(target_row, target_col, target_col, copy)
            my_string += thread
            copy.update_puzzle(thread)
        if copy.current_position(target_row, target_col)[0] < target_row:
            thread = copy.bring_down(target_row, target_col, target_row, copy)
            my_string += thread
            copy.update_puzzle(thread)
        #hopefully the target tile is in its location.  0 should be on top of it.    
        my_string += "ld"
        copy.update_puzzle("ld")
        self.update_puzzle(my_string)
        return my_string
        


    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # First bring the target tile into the col 0.
        # Then use the 3x2 solution.
        target_col = 0
        my_string = ""
        assert self.lower_row_invariant(target_row, target_col), "failed at solve_interior beginning"
        copy = self.clone()
        
        
        thread = "ur"
        copy.update_puzzle(thread)
        my_string += thread
        
        # Check the edge case
        if (copy.current_position(target_row, target_col)[0] == target_row - 1 and
            copy.current_position(target_row, target_col)[1] == 0):
            thread = "lruldrdlurdluurddlur"
            copy.update_puzzle(thread)
            my_string += thread
            while copy.current_position(0, 0)[1] < copy.get_width() - 1:
                thread = "r"
                my_string += thread
                copy.update_puzzle(thread)
            self.update_puzzle(my_string)
            return my_string
        
        #If it happens to have solved it, move on
        if copy.current_position(target_row, target_col) == (target_row, target_col):
            while copy.current_position(0, 0)[1] < copy.get_width() - 1:
                thread = "r"
                my_string += thread
                copy.update_puzzle(thread)
            self.update_puzzle(my_string)
            return my_string
        
        # Bring the target tile left to t+1
        if copy.current_position(target_row, target_col)[1] > target_col + 1:
            thread = copy.bring_left(target_row, target_col, target_col + 1, copy)
            my_string += thread
            copy.update_puzzle(thread)
        
        # Bring the target tile down to t-1.
        if copy.current_position(target_row, target_col)[0] < target_row - 1:
            thread = copy.bring_down(target_row, target_col, target_row - 1, copy)
            my_string += thread
            copy.update_puzzle(thread)
        thread = "ld"
        my_string += thread
        copy.update_puzzle(thread)

        thread = "ruldrdlurdluurddlur"
        my_string += thread
        copy.update_puzzle(thread)
        while copy.current_position(0, 0)[1] < copy.get_width() - 1:
            copy.update_puzzle("r")
            my_string += "r"
        assert copy.lower_row_invariant(target_row - 1, copy.get_width() - 1), "error on exiting col0"
        self.update_puzzle(my_string)
        return my_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        target_row = 0
        
        if self.get_number(target_row, target_col) != 0:
            return False
        
        for tile in range(target_col+1, self.get_width()):
            if (target_row, tile) != self.current_position(target_row, tile):
                return False
        for col in range(target_col + 1, self.get_width()):
            for row in range(self.get_height()):
                if ((row, col) != self.current_position(row, col) or
                    (target_row + 1, target_col) != self.current_position(target_row + 1, target_col)):
                    return False
        for row in range(target_row + 2, self.get_height()):
            for col in range(self.get_width()):
                if (row, col) != self.current_position(row, col):
                    return False
                
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        target_row = 1
        if self.get_number(target_row, target_col) != 0:
            return False
        
        for tile in range(target_col+1, self.get_width()):
            if (target_row, tile) != self.current_position(target_row, tile):
                return False
        for row in range(target_row + 1, self.get_height()):
            for col in range(self.get_width()):
                if (row, col) != self.current_position(row, col):
                    return False
        for col in range(target_col+1, self.get_width()):
            for row in range(self.get_height()):
                if(row, col) != self.current_position(row, col):
                    return False
                
                
        return True        

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col), "Row 0 assertion error upon entry"
        
        copy = self.clone()
        target_row = 0
        my_string = ""
        thread = "ld"
        my_string += thread
        copy.update_puzzle(thread)
        if copy.current_position(target_row, target_col)[1] == target_col:
            #assert copy.row1_invariant(1, target_col - 1), "exit 1"
            self.update_puzzle(my_string)
            return my_string
        if copy.current_position(target_row, target_col)[1] == target_col - 1:
            thread = "uldurdlurrdluldrruld"
            my_string += thread
            copy.update_puzzle(thread)
            #assert copy.row1_invariant(1, target_col - 1), "exit 2"
            self.update_puzzle(my_string)
            return my_string
        if copy.current_position(target_row, target_col)[0] == 1:
            thread = copy.bring_right(target_row, target_col, target_col - 1, copy)
            my_string += thread
            copy.update_puzzle(thread)
            thread = "ld"
            my_string += thread
            copy.update_puzzle(thread)
            thread = "urdlurrdluldrruld"
            my_string += thread
            copy.update_puzzle(thread)
            #assert copy.row1_invariant(1, target_col - 1), "exit 3"
            self.update_puzzle(my_string)
            return my_string
        if copy.current_position(target_row, target_col)[0] == 0:
            thread = copy.bring_right(target_row, target_col, target_col - 1, copy)
            my_string += thread
            copy.update_puzzle(thread)
            thread = "ld"
            my_string += thread
            copy.update_puzzle(thread)
            thread = "urdlurrdluldrruld"
            my_string += thread
            copy.update_puzzle(thread)
            #assert copy.row1_invariant(1, target_col - 1), "exit 4"
            self.update_puzzle(my_string)
            return my_string

        
    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """

        assert self.row1_invariant(target_col), "entering solve_row1 error"
        copy = self.clone()
        target_row = 1
        my_string = ""
        
        thread = "u"
        my_string += thread
        copy.update_puzzle(my_string)
        if (copy.current_position(0, 0) == (target_row-1, target_col) and 
            copy.current_position(target_row, target_col) == (target_row, target_col)):
            self.update_puzzle(my_string)
            return my_string
        else:
            while copy.current_position(0, 0)[1] > copy.current_position(target_row, target_col)[1]:
                thread = "l"
                my_string += thread
                copy.update_puzzle(thread)
            thread = "d"
            my_string += thread
            copy.update_puzzle(thread)
            while copy.current_position(0,0)[1] < target_col:
                thread = "r"
                my_string += thread
                copy.update_puzzle(thread)
        my_string += copy.solve_row1_tile(target_col)    
        self.update_puzzle(my_string)
        return my_string
                   

    ###########################################################
    # Phase 3 methods
    def truth_2x2(self):
        """
        Helper function to determine whether 2x2 is solved.
        """
        
        if self.current_position(0, 0) != (0, 0):
            return False
        if self.current_position(0, 1) != (0, 1):
            return False
        if self.current_position(1, 0) != (1, 0):
            return False
        if self.current_position(1, 1) != (1, 1):
            return False
        return True
        
        
    
    
    def solve_2x2(self): 
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        assert self.row1_invariant(1), "failed upon entry to 2x2"
        copy = self.clone()
        my_string = ""
        thread = "lu"
        my_string += thread
        copy.update_puzzle(thread)
        for dummy_num in range(4):
            thread = "rdlu"
            my_string += thread
            copy.update_puzzle(thread)
            if copy.truth_2x2():
                self.update_puzzle(my_string)
                return my_string
        for dummy_num in range(4):
            thread = "drul"
            my_string += thread
            copy.update_puzzle(thread)
            if copy.truth_2x2():
                self.update_puzzle(my_string)
                print "we should have exited safely"
                return my_string
        if not copy.truth_2x2():
            print "error on 2x2.  It can't finish this puzzle"
        self.update_puzzle(my_string)
        return my_string
    
             
    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        
        prime_copy = self.clone()
        my_string = ""
        delta_zero_x = self.get_width()-prime_copy.current_position(0, 0)[1] - 1
        delta_zero_y = self.get_height() - prime_copy.current_position(0, 0)[0] - 1

        for dummy_num in range(delta_zero_x):
            thread = "r"
            my_string += thread
            prime_copy.update_puzzle(thread)
        for dummy_num in range(delta_zero_y):
            thread = "d"
            my_string += thread
            prime_copy.update_puzzle(thread)
            
        print "first" , "\n" , prime_copy
        for target_row in range(prime_copy.get_height()-1, 1, -1):
            for target_col in range(prime_copy.get_width()-1, 0, -1):
                my_string += prime_copy.solve_interior_tile(target_row, target_col)
            my_string += prime_copy.solve_col0_tile(target_row)
        #self.update_puzzle(my_string)
        
        for target_col in range(prime_copy.get_width() - 1, 1, -1):
            my_string += prime_copy.solve_row1_tile(target_col)
            my_string += prime_copy.solve_row0_tile(target_col)
        my_string += prime_copy.solve_2x2()

            
        print self
        self.update_puzzle(my_string)
        return my_string

# Start interactive simulation
obj = Puzzle(3, 6, [[16, 7, 13, 17, 5, 9], 
                    [3, 0, 14, 10, 12, 6], 
                    [4, 15, 2, 11, 8, 1]]) 

poc_fifteen_gui.FifteenGUI(obj)


#obj.solve_puzzle() 
