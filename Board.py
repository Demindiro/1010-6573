class Board:

    def __init__(self, dimension, positions_to_fill):
        self.dots = set(
            dot for dot in positions_to_fill
            if dot[0] <= dimension and dot[1] <= dimension and dot[0] > 0 and dot[1] > 0
        )
        self.dimension = dimension
        #print(self.dimension, '\n', self.dots, '\n', positions_to_fill)


def make_board(dimension=10, positions_to_fill=frozenset()):
    """
        Return a new board of the given dimension for which all cells at the
        given positions are already filled.
        ASSUMPTIONS
        - The given dimension is a positive integer number.
        - The filled positions is a collection of proper positions. Positions
          outside the boundaries of the new board have no impact on the content
          of the new board.
    """
    return Board(dimension, positions_to_fill)


def copy_board(board):
    """
        Return a copy of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    return Board(board.dimension, board.dots)



def is_proper_board(board):
    """
        Check wether the given board is a proper board.
        - ...
        ASSUMPTIONS
        - None
        NOTE
        - You need to complete the conditions
        (as they depend on the internal representation you have chosen for the board)
    """
    for dot in board.dots:
        if dot[0] > board.dimension or dot[1] > board.dimension:
            return False
    return True




def dimension(board):
    """
        Return the dimension of the given board.
        - The function returns the number of rows (== number of columns) of
          the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    return board.dimension



def get_all_filled_positions(board):
    """
        Return a set of all the positions of filled cells on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    return frozenset(board.dots)




def is_filled_at(board, position):
    """
        Return a boolean indicating whether or not the cell at the given position
        on the given board is filled.
        - Returns false if the given position is outside the boundaries of the
          given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """
    return position in board.dots





def is_filled_row(board, row):
    """
        Return a boolean indicating whether or not all the cells of the given
        row on the given board are filled.
        - Returns false if the given row is not an integer number or if it is
          outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use for statements in the body of this function.
    """
    i = 0
    while i < board.dimension:
        if (row, i) not in board.dots:
            return False
        i += 1
    return True



def is_filled_column(board, column):
    """
        Return a boolean indicating whether or not all the cells of the given
        column on the given board are filled.
        - Returns false if the given column is not an integer number or if it is
          outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use while statements in the body of this function.
    """
    for i in range(board.dimension):
        if (i, column) not in board.dots:
            return False
        i += 1
    return True



def get_all_filled_rows(board):
    """
        Return all the rows on the given board that are completely filled.
        - The function returns a list of the numbers in ascending order of
          all the rows that are completely filled.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use for statements in the body of this function.
    """
    filled = []
    i = 0
    while i < board.dimension:
        if is_filled_row(i):
            filled.append(i)
        i += 1
    return filled



def get_all_filled_columns(board):
    """
        Return all the columns on the given board that are completely filled.
        - The function returns a tuple of the numbers in descending order of
          all the columns that are completely filled.
        ASSUMPTIONS
        - The given board is a proper board.
        NOTE
        - You are not allowed to use while statements in the body of this function.
    """
    return [i for i in range(board.dimension) if is_filled_column(board, i)]



def fill_cell(board, position):
    """
        Fill the cell at the given position on the given board.
        - Nothing happens if the given position is outside the
          boundaries of the given board or if the given cell is
          already filled.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """
    board.dots.add(position)



def fill_all_cells(board, positions):
    """
        Fill all the cells at each position in the given collection of
        positions on the given board.
        - Positions outside the boundaries of the given board are ignored.
        - Positions that are already filled are left untouched.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each position in the collection of positions is a proper position.
    """
    board.dots.update(position)




def free_cell(board, position):
    """
        Free the cell at the given position of the given board.
        - Nothing happens if the cell is already free or if the given
          position is outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
    """
    board.dots.discard(position)



def free_all_cells(board, positions):
    """
        Fill all the cells at each position in the tuple of positions on
        the given board.
        - Positions outside the boundaries of the given board are ignored.
        - Positions that are already filled are left untouched.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each position in the tuple of positions is a proper position.
        NOTE
        - This function must be worked out in a recursive way.
    """
    board.dots.difference_update(positions)




def free_row(board, row):
    """
        Free all the cells of the given row on the given board.
        - Nothing happens if the given row is not an integer number or if
          it is outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    board.dots.difference_update(((row, i) for i in range(board.dimension)))




def free_column(board, column):
    """
        Free all the cells of the given column on the given board.
        - Nothing happens if the given column is not an integer number or if
          it is outside the boundaries of the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    board.dots.difference_update(((i, column) for i in range(board.dimension)))




def can_be_dropped_at(board, block, position):
    """
        Check whether the given block can be dropped at the given position.
        - The given position determines the position for the anchor of the
          given block.
        - True if and only if for each of the dot positions D of the given block
          there is a FREE cell at a position within the boundaries of the given
          board and at the same horizontal- and vertical distance from the
          given position as the horizontal- and vertical distance of the dot
          position D from the anchor of the given block.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        - The given position is a proper position.
    """
    offset_dots = frozenset((dot[0] + position[0], dot[1] + position[1]) for dot in block.dots)
    return not offset_dots & board.dots



def get_droppable_positions(board, block):
    """
        Return a list of all positions at which the given block can be dropped
        on the given board.
        - The positions in the resulting list are in ascending order.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given block is a proper block.
        NOTE
        - The function should only examine positions at which the given block
          fully fits within the boundaries of the given board.
    """
    return [
        (row, column)
        for row in range(board.dimension - block.size[0])
        for column in range(board.dimension - block.size[1])
        if can_be_dropped_at(board, block, (row, column))
    ]




def drop_at(board, block, position):
    """
        Drop the given block at the given position on the given board.
        - Each of the cells on the given board at a position with the same
          horizontal- and vertical distance from the given position as a dot
          position of the given block from the block's anchor, is filled.
        - Nothing happens if the given block can not be dropped at the given
          position on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The given position is a proper position.
        - The given block is a proper block.
    """
    offset_dots = frozenset((dot[0] + position[0], dot[1] + position[1]) for dot in block.dots)
    board.dots += offset_dots



def clear_full_rows_and_columns(board):
    """
        Clear all full rows and all full columns on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for row in get_all_filled_rows(board):
        free_row(row)
    for column in get_all_filled_columns(board):
        free_column(column)



def _are_chainable(board, positions_mutable):
    dot = positions_mutable.pop()
    for offset in ((1,0), (-1,0), (0,1), (0,-1)):
        dot_offset = (dot[0] + offset[0], dot[1] + offset[1]);
        if dot_offset in board:
            _are_chainable(positions_mutable)



def are_chainable(board, positions):
    """
        Check whether the given collection of positions is chained on the
        given board.
        - True if and only if at least one collection of chained positions exists
          on the given board that includes all given positions and for which all
          the cells in that collection are either all filled or all empty.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each of the given positions is a proper position for the given board.
        - All the cells on the given board at the given positions all have the
          same state, i.e. they are all filled or all empty.
        NOTE
        - This function should be worked out in a recursive way
    """
    dots = set(posititions)
    _are_chainable(dots)
    return len(dots)



def print_board(board):
    """
        Print the given board on the standard output stream.
        ASSUMPTIONS
        - The given board is a proper board.
    """
    for row in range(dimension(board), 0, -1):
        print('{:02d}'.format(row), end="  ")
        for column in range(1, dimension(board) + 1):
            if is_filled_at(board, (column, row)):
                print(" \u25A9 ", end=" ")
            else:
                print("   ", end=" ")
        print()
    print("    ", end="")
    for column in range(1, dimension(board) + 1):
        print('{:02d}'.format(column), end="  ")
    print()
