from sudoku_reader import Sudoku_reader
import numpy as np


class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.nums = [[nums[i][j] for j in range(self.n_rows)] for i in range(self.n_cols)]

        # Lager lister for hver av variablene
        self.squares = []
        self.rows = []
        self.cols = []
        self.boxes = []
        self._set_up_nums()
        self._set_up_elems()
        

    def _set_up_nums(self):
        # Set up the squares on the board (ints into Square objects)
        for col in range(len(self.nums)):
            for row in range(len(self.nums)):
                square = Square(self.nums[row][col])
                if row <= 2:
                    if col <= 2:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 1
                    elif 2 < col <= 5:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 2
                    elif 5 < col <= 8:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 3
                if 2 < row <= 5:
                    if col <= 2:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 4
                    elif 2 < col <= 5:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 5
                    elif 5 < col <= 8:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 6
                if 5 < row <= 8:
                    if col <= 2:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 7
                    elif 2 < col <= 5:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 8
                    elif 5 < col <= 8:
                        square.col = row + 1
                        square.row = col + 1
                        square.box = 9
                if square.number != 0:
                    square.hasnum = True
                    self.squares.append(square)
                else:
                    square.hasnum = False
                    self.squares.append(square)
                self.nums[row][col] = square
        # print("These are all the squares:")
        # print(self.squares)
    
    def _set_up_elems(self):
        # You should set up links between your squares and elements
        for box in [[self.nums[r][c] for r in range(row,row+3) for c in range(col, col+3)] for row in range(0,9,3) for col in range(0,9,3)]:
            box_element = Element(box)
            self.boxes.append(box_element)

        # print("These are the boxes:")
        # print(self.boxes)

        row_counter = 0
        row_temp = []

        for i in range(9):
            for j in range(9):
                row = [self.nums[i][j]]
                for rows in row:
                    row_counter += 1
                    row_temp.append(rows)
                    if row_counter % 9 == 0:
                        row_element = Element(row_temp)
                        self.rows.append(row_element)

                        row_temp = []
                        row_counter = 0
        
        # print("These are the rows:")
        # print(self.rows)

        col_counter = 0
        col_temp = []

        for i in range(9):
            col = [row[i] for row in self.nums]
            for cols in col:
                col_counter += 1
                col_temp.append(cols)
                if col_counter % 9 == 0:
                    col_element = Element(col_temp)
                    self.cols.append(col_element)
                    col_temp = []
                    col_counter = 0
        
        # print("These are the cols:")
        # print(self.cols)


    # Connects the squares to the rows, cols and boxes it is ment to be in
        for row_pos, row in enumerate(self.nums):
            for col_pos, square in enumerate(row):
                square.row = self.rows[row_pos]
                square.col = self.cols[col_pos]
                square.box = self.boxes[(row_pos//3)*3 + (col_pos//3)]

            

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        r += "[["
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + ", "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r

class Sudokuboard(Board):
    def __init__(self, nums):
        super().__init__(nums)

    def find_empty(self):
    # Returns True if the square is empty/=0
        for row in self.nums:
            for square in row:
                if square.number == 0:
                    return square
        return None

    def solve(self):
    # Uses all the functions made to solve the sudoku boards
        opensquare = self.find_empty()
        if not opensquare:
            return True
        for num in range(1,10):
            if opensquare.is_valid(num):
                opensquare.set_value(num)
                if self.solve():
                    return True
                opensquare.number = 0
        return False

class Square:
    def __init__(self, number):
        self.number = number
        self.row = None
        self.col = None
        self.box = None
        self.hasnum = None

    def is_valid(self, num):
    # Returns True if the number is valid
        for square in self.row.squares:
            if square.number == num:
                return False
        for square in self.col.squares:
            if square.number == num:
                return False
        for square in self.box.squares:
            if square.number == num:
                return False
        return True
    

    def set_value(self, given_value):
    # Sets the number to the wished value
        self.number = given_value
    
    def set_row(self, elem):
    # Sets the row of the square to the given square
        self.row = elem
    
    def set_col(self, elem):
    # Sets the colum of the square to the given square 
        self.col = elem
    
    def set_box(self, elem):
    # Sets the box of the square to the given square
        self.box = elem
            

    def __str__(self) -> str:
        # result = self.number, self.row, self.col, self.box, self.hasnum
        # return str(result)
        return str(self.number)
    __repr__ = __str__

class Element:
    def __init__(self, squares):
        self.squares = squares
        self.init_squares()

    def init_squares(self):
    # Sets rows/boxs/cols to the given element
        for square in self.squares:
            square.set_row(self)
            square.set_col(self)
            square.set_box(self)

    def __str__(self):
        return str(self.squares)
    __repr__ = __str__


if __name__ == "__main__":
    # Test code...
    reader = Sudoku_reader("sudoku_10.csv")
    #board = Board(reader.next_board())
    while True:
        board = reader.next_board()
        if board is None:
            break

        sudoku = Sudokuboard(board)

        sudoku.solve()

        print(sudoku)

    