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
            x, y = 0, 0
            while self._grid[y][x] != 0:
                x += 1
                if x == 3:
                    x = 0
                    y += 1

            self._empty_position = Vector2(x, y)
        else:
            self._grid = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]
            ]
            self._empty_position = Vector2(0, 0)

    @property
    def empty_position(self):
        return self._empty_position

    @property
    def grid(self):
        return self._grid

    @property
    def is_solved(self):
        for y in range(3):
            for x in range(3):
                if self._grid[y][x] != y * 3 + x:
                    return False

        return True

    def get_square(self, position: Vector2):
        return self._grid[position.y][position.x]

    def move(self, position: Vector2, direction: Direction | Vector2):
        if isinstance(direction, Direction):
            direction = direction.value

        if position.x < 0 or position.x >= 3 or position.y < 0 or position.y >= 3:
            return

        square = self.get_square(position)

        if square == 0:
            return

        other_position = position + direction

        if other_position.x < 0 or other_position.x >= 3 or other_position.y < 0 or other_position.y >= 3:
            return

        other_square = self.get_square(other_position)

        if other_square != 0:
            self.move(other_position, direction)
            other_square = self.get_square(other_position)

        if other_square == 0:
            self._grid[other_position.y][other_position.x] = square
            self._grid[position.y][position.x] = 0
            self._empty_position = position

    def scramble(self, moves: int = 32):
        from random import choice

        for _ in range(moves):
            directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
            for direction in directions:
                bound = self.empty_position + direction.value
                if bound.x < 0 or bound.x >= 3 or bound.y < 0 or bound.y >= 3:
                    directions.remove(direction)

                direction_chosen = choice(directions).value

                self.move(self.empty_position + direction_chosen, -direction_chosen)
            
