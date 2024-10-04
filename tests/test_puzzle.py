import os
import sys
from src.puzzle import Puzzle, Vector2, Direction


def test_puzzle():
    puzzle = Puzzle()
    assert puzzle is not None


def test_puzzle_2():
    puzzle = Puzzle()
    expected_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid


def test_get_square():
    puzzle = Puzzle()
    square = puzzle.get_square(Vector2(0, 0))
    assert square == 0


def test_get_square_2():
    puzzle = Puzzle()
    square = puzzle.get_square(Vector2(1, 1))
    assert square == 4


def test_move_up():
    puzzle = Puzzle([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Vector2(0, 1), Direction.UP)
    expected_grid = [
        [3, 1, 2],
        [0, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid

def test_move_down():
    puzzle = Puzzle([
        [3, 1, 2],
        [0, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Vector2(0, 0), Direction.DOWN)

    expected_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid

def test_move_left():
    puzzle = Puzzle([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Vector2(1, 0), Direction.LEFT)

    expected_grid = [
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid

def test_move_right():
    puzzle = Puzzle([
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Vector2(0, 0), Direction.RIGHT)

    expected_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid

def test_move_up_2():
    puzzle = Puzzle([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Vector2(0, 2), Direction.UP)

    expected_grid = [
        [3, 1, 2],
        [6, 4, 5],
        [0, 7, 8]
    ]

    assert puzzle.grid == expected_grid

def test_move_down_2():
    puzzle = Puzzle([
        [3, 1, 2],
        [6, 4, 5],
        [0, 7, 8]
    ])

    puzzle.move(Vector2(0, 0), Direction.DOWN)

    expected_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid

def test_move_left_2():
    puzzle = Puzzle([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Vector2(2, 0), Direction.LEFT)

    expected_grid = [
        [1, 2, 0],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid

def test_move_right_2():
    puzzle = Puzzle([
        [1, 2, 0],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Vector2(0, 0), Direction.RIGHT)

    expected_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid
