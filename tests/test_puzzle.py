from src.puzzle import Puzzle, Vector2, Direction, Solver


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


def test_try_move_simulation():
    grid = [
        [0, 4, 2],
        [1, 3, 5],
        [6, 7, 8]
    ]
    empty_position = Vector2(0, 0)

    assert Solver.try_move_simulation(
        grid, empty_position, Direction.UP) == None
    assert Solver.try_move_simulation(
        grid, empty_position, Direction.LEFT) == None
    assert Solver.try_move_simulation(
        grid, empty_position, Direction.RIGHT) == (
        [[4, 0, 2],
         [1, 3, 5],
         [6, 7, 8]], Vector2(1, 0)
    )
    assert Solver.try_move_simulation(
        grid, empty_position, Direction.DOWN) == (
        [[1, 4, 2],
         [0, 3, 5],
         [6, 7, 8]], Vector2(0, 1)
    )


def test_manhattan_heuristic():

    grid = [[1, 4, 2],
            [0, 3, 5],
            [6, 7, 8]]

    assert Solver.manhattan_heuristic(grid) == 4


def test_manhattan_heuristic_2():
    grid = [[1, 0, 2],
            [3, 4, 5],
            [6, 7, 8]]

    assert Solver.manhattan_heuristic(grid) == 2


def test_solve():
    puzzle = Puzzle([
        [1, 4, 2],
        [3, 0, 5],
        [6, 7, 8]
    ])

    moves = Solver.solve(puzzle, True)
    assert len(moves) == 2
    assert puzzle.is_solved == True


def test_solve_2():
    puzzle = Puzzle([
        [1, 4, 2],
        [3, 7, 5],
        [6, 8, 0]
    ])

    moves = Solver.solve(puzzle, True)
    assert len(moves) == 4
    assert puzzle.is_solved == True


def test_solve_3():
    puzzle = Puzzle()
    puzzle.scramble(4)

    moves = Solver.solve(puzzle, False)
    assert puzzle.is_solved == False


def test_solve_4():
    puzzle = Puzzle([
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ])

    moves = Solver.solve(puzzle, True)
    assert len(moves) == 26
    assert puzzle.is_solved == True
