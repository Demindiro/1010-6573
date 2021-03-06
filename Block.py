import Position


class _Block:

    def __init__(self, dot_positions):
        self.dots = set(dot_positions)
        self.recalculate_boundaries()

    def get_normalized(self):
        for anchor in self.dots:
            break
        block = _Block.__new__(_Block)
        block.dots    = {(dot[0] - anchor[0], dot[1] - anchor[1]) for dot in self.dots}
        block.topleft = (self.topleft[0] - anchor[0], self.topleft[1] - anchor[1])
        block.size    = self.size
        return block

    def get_topleft_on_anchor(self):
        block = _Block.__new__(_Block)
        block.dots    = {(dot[0] - self.topleft[0], dot[1] - self.topleft[1]) for dot in self.dots}
        block.topleft = (0,0)
        block.size    = self.size
        return block

    def recalculate_boundaries(self):
        from math import inf
        min_x, min_y = inf, inf
        max_x, max_y = -inf, -inf
        for pos in self.dots:
            if pos[0] < min_x:
                min_x = pos[0]
            if pos[1] < min_y:
                min_y = pos[1]
            if pos[0] > max_x:
                max_x = pos[0]
            if pos[1] > max_y:
                max_y = pos[1]
        self.topleft = (min_x, min_y)
        self.size    = (max_x - min_x, max_y - min_y)





def make_block(dot_positions):
    """
       Create a new block involving the given mutable set of dot positions.
       ASSUMPTIONS
       - The given set of dot positions is not empty and each of its
         elements is a proper position.
       - The given dot positions are chained together.
    """
    return _Block(dot_positions)

    



def get_all_dot_positions(block):
    """
        Return a mutable set of all the dot positions of the given block.
        - Dot positions are relative towards the block's anchor.
        ASSUMPTIONS
        - The given block is a proper block.
    """
    return set(block.dots)





def is_proper_block(block):
    """
        Check whether the given block is a proper block.
        - True if and only if the set of dot positions of the given block is not empty,
          if each of its elements is a proper position, and if the dot positions of the
          given block are chained together.
        ASSUMPTIONS:
        - None
    """
    if type(block) is not _Block or len(block.dots) == 0:
        return False
    for pos in block.dots:
        if not Position.is_proper_position(pos):
            return False
    return Position.are_chained(block.dots)






def add_dot(block, dot_position):
    """
        Add the given dot position to the given block.
        - Nothing happens if the given block already has a dot at the given position, or
          if the given dot cannot be chained with existing dots of the given block.
        ASSUMPTIONS
        - The given block is a proper block.
        - The given position is a proper position.
    """
    for offset in ((1,0), (-1,0), (0,1), (0,-1)):
        if (dot_position[0] + offset[0], dot_position[1] + offset[1]) in block.dots:
            block.dots.add(dot_position)
            block.recalculate_boundaries()
            break



def remove_dot(block, dot_position):
    """
        Remove the given dot position from the given block.
        - Nothing happens if the given dot is not part of the given block, if the
          given block only has the dot to be removed as its single dot, or if the dots
          in the resulting block can no longer be chained.
        ASSUMPTIONS
        - The given block is a proper block.
        - The given position is a proper position.
    """
    block.dots.discard(dot_position)
    if not is_proper_block(block):
        block.dots.add(dot_position)
    else:
        block.recalculate_boundaries()


def get_horizontal_offsets_from_anchor(block):
    """
        Return the horizontal offsets from the anchor of this block.
        - The function returns a tuple involving the smallest horizontal offset
          to the left of the anchor, followed by the largest horizontal offset
          to the right the anchor.
          More formally, if the function returns the tuple (L,R), then for each dot
          position (x,y) of the given block, L <= x <= R
        ASSUMPTIONS
        - The given block is a proper block.
    """
    return (block.topleft[0], block.topleft[0] + block.size[0])



def get_vertical_offsets_from_anchor(block):
    """
        Return the vertical offsets from the anchor of this block.
        - The function returns a tuple involving the smallest vertical offset
          below the anchor, followed by the largest vertical offset above the anchor.
          More formally, if the function returns the tuple (B,A), then for each dot
          position (x,y) of the given block, B <= y <= A
        ASSUMPTIONS
        - The given block is a proper block.
    """
    return (block.topleft[1], block.topleft[1] + block.size[1])



def are_equivalent(block, other_block):
    """
       Check whether the given blocks are equivalent, i.e. cover equivalent
       chains of dots.
       - A block is equivalent with some other block , if there exists a position
         for the anchor of the one block such that the set of dots covered by that
         block relative towards that anchor position, is identical to the set of
         dots covered by the other block.
        ASSUMPTIONS
        - Both given blocks are proper blocks.
    """
    return block.get_topleft_on_anchor().dots == other_block.get_topleft_on_anchor().dots



def is_normalized(block):
    """
       Check whether the given block is normalized.
       - True if and only if the anchor of the given block is one of the dot positions
         of that block.
       ASSUMPTIONS
       - The given block is a proper block.
    """
    return (0,0) in block.dots



def normalize(block):
    """
       Return a new block that is a normalized version of the given block.
       - The resulting block must be equivalent with the given block.
       - The function is free to choose a proper anchor for the normalized
         block.
       ASSUMPTIONS
       - The given block is a proper block.
    """
    return block.get_normalized()





def print_block(block):
    """
        Print the given block on the standard output stream.
        - The anchor of the given block will be revealed in the print-out.
        ASSUMPTIONS
        - The given block is a proper block.
    """
    horizontal_offsets = get_horizontal_offsets_from_anchor(block)
    width = max(horizontal_offsets[1], 0) - min(horizontal_offsets[0], 0) + 1
    vertical_offsets = get_vertical_offsets_from_anchor(block)
    height = max(vertical_offsets[1], 0) - min(vertical_offsets[0], 0) + 1
    printout = [[" " for column in range(1, width + 1)]
                for row in range(1, height + 1)]
    dot_positions = get_all_dot_positions(block)
    for (column, row) in dot_positions:
        printout[row - min(vertical_offsets[0], 0)] \
            [column - min(horizontal_offsets[0], 0)] = "\u25A9"
    if (0, 0) in dot_positions:
        anchor_symbol = "\u25A3"
    else:
        anchor_symbol = "\u25A2"
    printout[-min(vertical_offsets[0], 0)][-min(horizontal_offsets[0], 0)] = anchor_symbol
    for row in range(len(printout) - 1, -1, -1):
        for col in range(0, len(printout[0])):
            print(printout[row][col], end=" ")
        print()


# collection of standard blocks used to play the game.


standard_blocks = \
    (  # Single dot
        make_block({(0, 0)}),
        # Horizontal line of length 2
        make_block({(0, 0), (1, 0)}),
        # Horizontal line of length 3
        make_block({(-1, 0), (0, 0), (1, 0)}),
        # Horizontal line of length 4
        make_block({(-3, 0), (-2, 0), (-1, 0), (0, 0)}),
        # Horizontal line of length 5
        make_block({(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)}),
        # Vertical line of length 2
        make_block({(0, 0), (0, 1)}),
        # Vertical line of length 3
        make_block({(0, -1), (0, 0), (0, 1)}),
        # Vertical line of length 4
        make_block({(-2, 2), (-2, 3), (-2, 4), (-2, 5)}),
        # Vertical line of length 5
        make_block({(0, -6), (0, -5), (0, -4), (0, -3), (0, -2)}),
        # T-squares 1x1
        make_block({(-1, 0), (0, 0), (0, 1)}),
        make_block({(0, 0), (0, 1), (1, 0)}),
        make_block({(0, 0), (0, -1), (1, 0)}),
        make_block({(-1, 0), (0, 0), (0, -1)}),
        # T-squares 2x2
        make_block({(-2, 0), (-1, 0), (0, 0), (0, 1), (0, 2)}),
        make_block({(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)}),
        make_block({(2, 0), (1, 0), (0, 0), (0, -1), (0, -2)}),
        make_block({(-2, -2), (-1, -2), (0, -2), (-2, -1), (-2, 0)}),
        # Square block 2x2
        make_block({(0, 0), (1, 0), (0, 1), (1, 1)}),
        # Square block 3x3
        make_block({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)}),
    )


def select_standard_block():
    """
        Return one of the standard blocks.
        - The resulting block is selected randomly.
    """
    import random
    return random.choice(standard_blocks)
