from enum import Enum
from typing import List, Optional
from random import choice


class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.x, self.y))


class Direction(Enum):
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)


class Puzzle:
    def __init__(self, grid: Optional[List[List[int]]] = None):
        if grid:
            self._grid = grid
            for y in range(3):
                for x in range(3):
                    if grid[y][x] == 0:
                        self._empty_position = Vector2(x, y)
                        return
        else:
            self._grid = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]
            ]
            self._empty_position = Vector2(0, 0)

    @property
    def empty_position(self) -> Vector2:
        return self._empty_position

    @property
    def grid(self) -> List[List[int]]:
        return self._grid

    @property
    def is_solved(self) -> bool:
        for y in range(3):
            for x in range(3):
                if self._grid[y][x] != y * 3 + x:
                    return False

        return True

    def get_square(self, position: Vector2) -> int:
        return self._grid[position.y][position.x]

    def move(self, direction: Direction | Vector2) -> bool:
        """Moves the empty square in the given direction. Returns True if the move was successful, False otherwise."""
        if isinstance(direction, Direction):
            direction = direction.value

        other_position = self.empty_position + direction
        if other_position.x < 0 or other_position.x >= 3 or other_position.y < 0 or other_position.y >= 3:
            return False

        self._grid[self.empty_position.y][self.empty_position.x] = \
            self.get_square(other_position)
        self._grid[other_position.y][other_position.x] = 0

        self._empty_position = other_position
        return True

    def try_move(self, direction: Direction | Vector2) -> int:
        """Returns the manhattan distance of the puzzle after moving in the given direction."""
        if isinstance(direction, Direction):
            direction = direction.value

        if not self.move(direction):
            return -1

        distance = self.manhattan_heuristic()
        self.move(-direction)
        return distance

    def scramble(self, moves: int = 48) -> None:
        """Scrambles the puzzle by making a given number(default 48) of random moves.
        If the puzzle is already solved, it will scramble it again."""
        for _ in range(moves):
            directions = [Direction.UP, Direction.DOWN,
                          Direction.LEFT, Direction.RIGHT]
            for direction in directions:
                bound = self.empty_position + direction.value
                if bound.x < 0 or bound.x >= 3 or bound.y < 0 or bound.y >= 3:
                    directions.remove(direction)

                direction_chosen = choice(directions).value

                self.move(direction_chosen)

        if self.is_solved:
            self.scramble(moves)

    def manhattan_distance(self, position: Vector2) -> int:
        """Returns the manhattan distance of the given position to its target position."""
        square = self.get_square(position)

        target = Vector2(square % 3, square // 3)
        return abs(position.x - target.x) + abs(position.y - target.y)

    def manhattan_heuristic(self) -> int:
        """Returns the manhattan distance of the puzzle.
        The sum of the manhattan distances of all squares."""
        distance = 0
        for y in range(3):
            for x in range(3):
                position = Vector2(x, y)
                distance += self.manhattan_distance(position)

        return distance

    def solve(self) -> int:
        """Solves the puzzle using the A* algorithm with the manhattan heuristic.
        Still in development, not working properly yet. Returns the cost of the solution."""

        g_cost = 0
        h_cost = self.manhattan_heuristic()

        directions = [Direction.UP.value, Direction.DOWN.value,
                      Direction.LEFT.value, Direction.RIGHT.value]

        last_direction = Vector2(0, 0)
        while not self.is_solved:
            moves = [(move, cost) for move in directions if (
                cost := self.try_move(move)) != -1]

            for i, (move, cost) in enumerate(moves):
                if -move == last_direction:
                    moves.pop(i)
                    break

            best_move, _ = min(moves, key=lambda x: x[1])
            last_direction = best_move

            self.move(best_move)
            g_cost += 1
            h_cost = self.manhattan_heuristic()

        return g_cost
