import random

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
    if type(position) is tuple and len(position) == 2:
        x, y = position
        if type(x) is int and type(y) is int:
            return True
    return False




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
    if type(dimension) is int and is_proper_position(position):
        x, y = position
        return x >= 1 and y >= 1 and x <= dimension and y <= dimension




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
    x, y = position
    return (x - 1, y) if x > 1 else None




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
    x, y = position
    return (x + 1, y) if x < dimension else None




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
    x, y = position
    return (x, y + 1) if y < dimension else None




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
    x, y = position
    return (x, y - 1) if y > 1 else None




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
    x, y = position
    if x == dimension:
        if y == dimension:
            return None
        y += 1
        x = 0
    x += 1
    return x, y




def translate_over(position, delta_x, delta_y):
    """
        Return the position resulting from translating the given position horizontally
        and vertically over the given delta's.
        ASSUMPTIONS
        - The given position is a proper position.
        - The given delta's are integer numbers.
    """
    x, y = position
    return (x + delta_x, y + delta_y)




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
    x, y = position

    if dimension is None:
        return {(x-1,y), (x+1,y), (x,y-1), (x,y+1)}

    s = set()
    if x > 1:
        s.add((x - 1, y))
    if x < dimension:
        s.add((x + 1, y))
    if y > 1:
        s.add((x, y - 1))
    if y < dimension:
        s.add((x, y + 1))
    return s




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
    x, y = position
    s = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
    return len(s & set(other_positions)) > 0




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
    x, y = position
    surrounding = {(x+i,y+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0}
    if dimension is None:
        return surrounding
    not_surrounding = {
            p for p in surrounding
            if p[0] < 1 or p[0] > dimension or \
                p[1] < 1 or p[1] > dimension
        }

    return surrounding - not_surrounding




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

    positions = set(positions)
    chained_positions = set()
    for pos in positions:
        tocheck_positions = {pos}
        break
    else:
        return True

    while True:
        tochecknext_positions = set()
        for pos in tocheck_positions:
            for adjpos in get_adjacent_positions(pos):
                if adjpos not in chained_positions and adjpos in positions:
                    tochecknext_positions.add(adjpos)
        chained_positions |= tocheck_positions
        if len(tochecknext_positions) == 0:
            break
        tocheck_positions  = tochecknext_positions

    return len(positions - chained_positions) == 0





def are_chained_rec(positions, next_pos=None, chained_positions=None):
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

    if len(positions) <= 1:
        return True

    if next_pos == None:
        next_pos = positions[0]
        print(next_pos)
        chained_positions = set()

    x, y = next_pos

    npos = (x - 1, y)
    if npos in positions and npos not in chained_positions:
        chained_positions.add(npos)
        are_chained_rec(positions, npos, chained_positions)
    npos = (x, y - 1)
    if npos in positions and npos not in chained_positions:
        chained_positions.add(npos)
        are_chained_rec(positions, npos, chained_positions)
    npos = (x + 1, y)
    if npos in positions and npos not in chained_positions:
        chained_positions.add(npos)
        are_chained_rec(positions, npos, chained_positions)
    npos = (x, y + 1)
    if npos in positions and npos not in chained_positions:
        chained_positions.add(npos)
        are_chained_rec(positions, npos, chained_positions)

    return len(set(positions)) == len(chained_positions)
