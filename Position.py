# Positions are used to
#  (1) identify cells on the board
#  (2) dots on blocks relative to the block's anchor.


def is_proper_position(position):
    """
        Check whether the given position is a proper position.
        - True if and only if the given position is a tuple of length 2
          whose elements are both integer numbers.
        ASSUMPTIONS
        - None
    """






def is_proper_position_for_board(dimension, position):
    """
        Check whether the given position is a proper position for a square
        board with the given dimension.
        - True if and only if (1) the given dimension is a positive integer
          number and (2) if the given position is a proper position within
          the boundaries of a board with the given dimension, i.e not below
          1 nor above the given dimension in both directions.
        ASSUMPTIONS
        - None
    """



def left(dimension, position):
    """
        Return the position on any board with the given dimension immediately to
        the left of the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
    """



def right(dimension, position):
    """
       Return the position on any board with the given dimension immediately to
       the right of the given position.
       - None is returned if the generated position is outside the boundaries of
         a board with the given dimension.
       ASSUMPTIONS
       - The given position is a proper position for any board with the
         given dimension.
     """



def up(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        above the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """



def down(dimension, position):
    """
        Return the position on any board with the given dimension immediately
        below the given position.
        - None is returned if the generated position is outside the boundaries of
          a board with the given dimension.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """



def next(dimension, position):
    """
        Return the position on any board with the given dimension next to the
        given position.
        - If the given position is not at the end of a row, the resulting position
          is immediately to the right of the given position.
        - If the given position is at the end of a row, the resulting position is
          the leftmost position of the row above. If that next row does not exist,
          None is returned.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension.
     """



def translate_over(position, delta_x, delta_y):
    """
        Return the position resulting from translating the given position horizontally
        and vertically over the given delta's.
        ASSUMPTIONS
        - The given position is a proper position.
        - The given delta's are integer numbers.
    """



def get_adjacent_positions(position, dimension=None):
    """
        Return a mutable set of all positions immediately adjacent to the
        given position and within the boundaries of a board with the given
        dimension.
        - Adjacent positions are either at a horizontal distance or at a vertical
          distance of 1 from the given position.
        - If the given dimension is None, no boundaries apply.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension, or simply a proper position if no dimension is supplied.
    """



def is_adjacent_to(position, other_positions):
    """
        Check whether the given position is adjacent to at least one of the positions
        in the collection of other positions.
        - True if and only if at least one of the other positions is one of the positions
          adjacent to the given position in an unbounded area.
        ASSUMPTIONS
        - The given position is a proper position
        - All positions in the collection of other positions are proper positions.
    """




def get_surrounding_positions(position, dimension=None):
    """
        Return a mutable set of all positions immediately surrounding the
        given position and within the boundaries of a board with the given
        dimension.
        - Surrounding positions are at a horizontal distance and/or a vertical
          distance of 1 from the given position.
        - If the given dimension is None, no boundaries apply.
        ASSUMPTIONS
        - The given position is a proper position for any board with the
          given dimension, or simply a proper position if no dimension is supplied.
    """




def are_chained(positions):
    """
        Check whether the given collection of positions make up a chain.
        - True if and only if each position in the given collection of positions
          can be reached from each other position in that collection.
          A position P1 can be reached from another position P2 if
            (1) P1 and P2 are adjacent to each other, or
            (2) there exists at least one position P3 in the given collection
                of positions that can be reached from both P1 and P2.
       ASSUMPTIONS
       - Each position in the collection of positions is a proper position.
       NOTE
       - This version of the function must be worked out in an iterative way.
         The body may use while statements and/or for statements.
    """



def are_chained_rec \
                (positions):
    """
        Check whether the given collection of positions make up a chain.
        - True if and only if each position in the given collection of positions
          can be reached from each other position in that collection.
          A position P1 can be reached from another position P2 if
            (1) P1 and P2 are adjacent to each other, or
            (2) there exists at least one position P3 in the given collection
                of positions that can be reached from both P1 and P2.
       ASSUMPTIONS
       - Each position in the collection of positions is a proper position.
       NOTE
       - This version of the function must be worked out in a recursive way. The body
         may not use while statements nor for statements.
       TIP
       - Extend the heading of the function with two additional parameters:
          - chained_positions: a frozen set of positions that already form a chain.
          - non_chainable_positions: a frozen set of positions that are not
            adjacent to any of the positions in the set of chained positions.
         Assign both extra parameters the empty frozen set as their default value.
    """
