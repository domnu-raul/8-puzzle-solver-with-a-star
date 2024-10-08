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


def test_puzzle_3():
    puzzle = Puzzle([
        [1, 4, 2],
        [3, 0, 5],
        [6, 7, 8]
    ])

    expected_grid = [
        [1, 4, 2],
        [3, 0, 5],
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


def test_move():
    puzzle = Puzzle([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Direction.DOWN)
    expected_grid = [
        [3, 1, 2],
        [0, 4, 5],
        [6, 7, 8]
    ]
    assert puzzle.grid == expected_grid

    puzzle.move(Direction.RIGHT)
    expected_grid = [
        [3, 1, 2],
        [4, 0, 5],
        [6, 7, 8]
    ]
    assert puzzle.grid == expected_grid

    puzzle.move(Direction.UP)
    expected_grid = [
        [3, 0, 2],
        [4, 1, 5],
        [6, 7, 8]
    ]
    assert puzzle.grid == expected_grid

    puzzle.move(Direction.LEFT)
    expected_grid = [
        [0, 3, 2],
        [4, 1, 5],
        [6, 7, 8]
    ]


def test_move_2():
    puzzle = Puzzle([
        [0, 4, 2],
        [1, 3, 5],
        [6, 7, 8]
    ])

    assert puzzle.move(Direction.UP) == False
    assert puzzle.move(Direction.LEFT) == False
    assert puzzle.move(Direction.RIGHT) == True
    assert puzzle.move(Direction.DOWN) == True


def test_try_move():
    puzzle = Puzzle([
        [1, 4, 2],
        [3, 0, 5],
        [6, 7, 8]
    ])

    assert puzzle.try_move(Direction.UP) == 2
    assert puzzle.manhattan_heuristic() == 4

    assert puzzle.try_move(Direction.DOWN) == 6
    assert puzzle.manhattan_heuristic() == 4

    assert puzzle.try_move(Direction.LEFT) == 4
    assert puzzle.manhattan_heuristic() == 4

    assert puzzle.try_move(Direction.RIGHT) == 6
    assert puzzle.manhattan_heuristic() == 4


def test_is_solved():
    puzzle = Puzzle([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    assert puzzle.is_solved == True


def test_is_solved_2():
    puzzle = Puzzle([
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    assert puzzle.is_solved == False


def test_scramble_puzzle():
    puzzle = Puzzle()
    puzzle.scramble()
    print(puzzle.grid)
    assert puzzle.is_solved == False


def test_scramble_puzzle_2():
    puzzle = Puzzle()
    puzzle.scramble()
    print(puzzle.grid)
    assert puzzle.is_solved == False


def test_manhattan_distance():
    puzzle = Puzzle([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])

    assert puzzle.manhattan_distance(Vector2(0, 0)) == 1
    assert puzzle.manhattan_distance(Vector2(2, 2)) == 4


def test_manhattan_distance_2():
    puzzle = Puzzle()

    for x in range(3):
        for y in range(3):
            assert puzzle.manhattan_distance(Vector2(x, y)) == 0


def test_manhattan_heuristic():

    puzzle = Puzzle([[1, 4, 2],
                     [0, 3, 5],
                     [6, 7, 8]])

    assert puzzle.manhattan_heuristic() == 4


def test_solve():
    puzzle = Puzzle([
        [1, 4, 2],
        [3, 0, 5],
        [6, 7, 8]
    ])

    moves = puzzle.solve(True)
    assert len(moves) == 2
    assert puzzle.is_solved == True


def test_solve_2():
    puzzle = Puzzle([
        [1, 4, 2],
        [3, 7, 5],
        [6, 8, 0]
    ])

    moves = puzzle.solve(True)
    assert len(moves) == 4
    assert puzzle.is_solved == True


def test_solve_3():
    puzzle = Puzzle()
    puzzle.scramble(4)

    puzzle.solve(True)
    assert puzzle.is_solved == True


def test_solve_4():
    puzzle = Puzzle([
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ])

    moves = puzzle.solve(True)
    assert len(moves) == 26
    assert puzzle.is_solved == True
