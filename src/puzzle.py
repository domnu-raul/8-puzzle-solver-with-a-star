from enum import Enum
from typing import List, Optional


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
        else:
            self._grid = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]
            ]

    @property
    def grid(self):
        return self._grid

    def get_square(self, position: Vector2):
        return self._grid[position.y][position.x]

    def move(self, position: Vector2, direction: Direction):
        if position.x < 0 or position.x >= 3 or position.y < 0 or position.y >= 3:
            return

        square = self.get_square(position)

        if square == 0:
            return

        other_position = position + direction.value

        if other_position.x < 0 or other_position.x >= 3 or other_position.y < 0 or other_position.y >= 3:
            return

        other_square = self.get_square(other_position)

        if other_square != 0:
            self.move(other_position, direction)
            other_square = self.get_square(other_position)

        if other_square == 0:
            self._grid[other_position.y][other_position.x] = square
            self._grid[position.y][position.x] = 0
