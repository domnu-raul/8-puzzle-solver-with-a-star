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


def test_move_down():
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


def test_move_up():
    puzzle = Puzzle([
        [3, 1, 2],
        [0, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Direction.UP)

    expected_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid


def test_move_right():
    puzzle = Puzzle([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Direction.RIGHT)

    expected_grid = [
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid


def test_move_left():
    puzzle = Puzzle([
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle.move(Direction.LEFT)

    expected_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    assert puzzle.grid == expected_grid


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
