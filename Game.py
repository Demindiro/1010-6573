#!/usr/bin/env python3

import Position
import Block
import Board
import random
import math



def get_score(board, block):
    """
    Get the score this board would give
    """
    score = 0
    score_adder = 10
    for _ in Board.get_all_filled_columns(board):
        score += score_adder
        score_adder += 10
    for _ in Board.get_all_filled_rows(board):
        score += score_adder
        score_adder += 10
    return score + len(block.dots)



def highest_score(board, blocks, start=0):
    """
        Return the highest possible score that can be obtained by dropping
        all the blocks in the given sequence of blocks starting from the given
        start index in the order from left to right on the given board.
        - If a solution is possible, the function actually returns a tuple
          consisting of the highest score followed by a list of all positions
          at which the successive blocks must be dropped.
        - If the highest score can be reached in several possible ways, the
          function will give preference to positions closest to the bottom left
          corner to drop the next block.
        - If no solution is possible, the function returns the tuple (None,None).
        - At the end of the function, the board must still be in the same
          state it was in at the start of the function.
        ASSUMPTIONS
        - The given board is a proper board.
        - Each block in the given sequence of blocks is a proper block.
        - The given start index is not negative, but may be beyond the last element
          in the sequence of blocks.
        NOTE
        - You are allowed to take a copy of the given board.
        - You are not allowed to extend the heading of the function with
          additional parameters, nor to introduce an auxiliary function
          to be able to pass additional information.
        - The function should be worked out in a recursive way.
    """
    if start == len(blocks):
        return (0, [])

    best_score = 0
    best_order = []
    has_solution = False

    block = blocks[start]
    for position in Board.get_droppable_positions(board, block):
        board_copy = Board.copy_board(board)

        Board.drop_at(board_copy, block, position) 
        score = get_score(board_copy, block)
        Board.clear_full_rows_and_columns(board_copy)

        score_rec, order_rec = highest_score(board_copy, blocks, start + 1)
        if score_rec is None:
            continue

        score += score_rec
        if score > best_score:
            best_score = score
            best_order = order_rec
            best_order.insert(0, position)
            has_solution = True

    if not has_solution:
        return (None, None)

    return (best_score, best_order)




def _play_greedy_rec(board, blocks, current_score=0, current_length_sum=0):
    best_score      = 0
    best_board      = None
    best_length_sum = math.inf

    # Try starting with every block
    # When recursing this effectively becomes a permutation
    for block in blocks:
        for position in Board.get_droppable_positions(board, block):
            board_copy = Board.copy_board(board)

            Board.drop_at(board_copy, block, position) 
            score = get_score(board_copy, block)
            Board.clear_full_rows_and_columns(board_copy)

            length_sum = math.sqrt(position[0] ** 2 + position[1] ** 2)

            if len(blocks) > 1:
                remaining_blocks = blocks.copy()
                remaining_blocks.remove(block)
                score, length_sum = _play_greedy_rec(board_copy, remaining_blocks, score, length_sum)
                if score is None:
                    continue

            if score > best_score or (score == best_score and best_length_sum > length_sum):
                best_score      = score
                best_board      = board_copy
                best_length_sum = length_sum

    if best_board:
        board.dots = best_board.dots
        return current_score + best_score, current_length_sum + best_length_sum
    else:
        return None, None


def play_greedy(board, blocks):
    """
        Drop the given sequence of blocks in the order from left to right on
        the given board in a greedy way.
        - The function will take blocks in triplets (groups of 3) in the order from
          left tot right, and drop them on the given board in the best possible way
          (i.e yielding the highest possible score) not taking into account blocks
          that still need to be dropped further on.
        - If the number of blocks is not a multiple of 3, the function will take the
          remaining blocks (1 or 2) in the last step.
        - The function will search for the best possible positions to drop each
          of the 3 blocks in succession. If several positions yield the same highest
          score, the function will give preference to positions closest to the bottom
          left corner.
        - If a solution is possible, the function returns the total score obtained
          from dropping all the blocks.
        - If no solution is possible, the function returns None. All the blocks that
          could be dropped are effectively dropped on the given board.
        ASSUMPTIONS
        - The given board is a proper board.
        - The number of blocks in the given sequence of blocks is a multiple of 3.
    """

    best_length = 0
    print('Start')
    Board.print_board(board)

    score = 0
    print('---')
    for triplet in (blocks[i:i+3] for i in range(0, len(blocks), 3)):
        # Using a set doesn't necessarily preserve order 
        # Hence, use lists, which are deterministic and do have an order
        # (Determinism is nice when debugging)
        result = highest_score(board, triplet)
        #round_score, _ = _play_greedy_rec(board, list(triplet))
        if result[0] is None:
            return None
        for blk, pos in zip(triplet, result[1]):
            print(pos)
            print('Round')
            Board.print_board(board)
            Block.print_block(blk)
            assert Board.can_be_dropped_at(board, blk, pos)
            Board.drop_at(board, blk, pos)
        score += result[0]
    print(board.dots)

    return score
        




def game_move(board, block, position):
    """
        Drop the given block at the given position on the given board, and
        clear all full rows and columns, if any, after the drop.
        - The function returns the score obtained from the give move.
        ASSUMPTIONS
        - The given board is a proper board
        - The given block is a proper block.
        - The given position is a proper position.
        - The given block can be dropped at the given position on the given
          board.
    """
    Board.drop_at(board, block, position)
    nb_filled_seqs = \
        len(Board.get_all_filled_columns(board)) + \
        len(Board.get_all_filled_rows(board))
    Board.clear_full_rows_and_columns(board)
    return \
        len(Block.get_all_dot_positions(block)) + \
        10 * ((nb_filled_seqs + 1) * nb_filled_seqs) // 2


def play_game():
    """
        Play the game.
    """
    the_board = Board.make_board(5)
    score = 0
    current_block = Block.select_standard_block()
    print("Score: ", score)
    print()
    print("Next block to drop:")
    Block.print_block(current_block)
    print()
    Board.print_board(the_board)
    print()

    while len(Board.get_droppable_positions(the_board, current_block)) > 0:

        position = input("Enter the position to drop the block: ")
        if position == "":
            position = \
                random.choice(Board.get_droppable_positions(the_board, current_block))
            print("   Using position: ", position[0], ",", position[1])
        else:
            position = eval(position)
            if not isinstance(position, tuple):
                print("Not a valid position")
                continue

        if not Board.can_be_dropped_at(the_board, current_block, position):
            print("Block cannot be dropped at the given position")
            continue

        score += game_move(the_board, current_block, position)

        current_block = Block.select_standard_block()
        print("Score: ", score)
        print()
        print("Next block to drop:")
        Block.print_block(current_block)
        print()
        Board.print_board(the_board)
        print()

    print("End of game!")
    print("   Final score: ", score)


if __name__ == '__main__':
    play_game()
