from enum import Enum
from typing import List, Optional, Tuple
from random import choice
import heapq
from dataclasses import dataclass


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

    def __lt__(self, other):
        return True

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

    def scramble(self, moves: int = 96) -> None:
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


class Solver:
    @dataclass
    class Node:
        f_cost: int
        g_cost: int
        grid: List[List[int]]
        empty_position: Vector2
        parent: Optional["Node"] = None

        def __init__(self, f_cost: int, g_cost: int, grid: List[List[int]], empty_position: Vector2):
            self.f_cost = f_cost
            self.g_cost = g_cost
            self.grid = grid
            self.empty_position = empty_position

        def __lt__(self, other):
            return self.f_cost < other

        def __gt__(self, other):
            return self.f_cost > other

        def __eq__(self, other):
            return self.grid == other.grid

        def __hash__(self):
            return hash(self.grid)

    @staticmethod
    def manhattan_heuristic(grid: List[List[int]]) -> int:
        """Returns the manhattan distance of the given grid."""
        distance = 0
        for y in range(3):
            for x in range(3):
                square = grid[y][x]
                target_x, target_y = square % 3, square // 3
                distance += abs(x - target_x) + abs(y - target_y)

        return distance

    @staticmethod
    def try_move_simulation(grid: List[List[int]], empty_position: Vector2, direction: Vector2 | Direction) -> tuple[List[List[int]], Vector2] | tuple[None, None]:
        """Simulates a move in the given grid and returns the new grid and empty position if the move is valid, None otherwise."""
        if isinstance(direction, Direction):
            direction = direction.value
        other_position = empty_position + direction

        if other_position.x < 0 or other_position.x >= 3 or other_position.y < 0 or other_position.y >= 3:
            return None, None

        new_grid = [row[:] for row in grid]
        new_grid[empty_position.y][empty_position.x] = new_grid[other_position.y][other_position.x]
        new_grid[other_position.y][other_position.x] = 0

        return new_grid, other_position

    @staticmethod
    def _grid_to_tuple(grid: List[List[int]]):
        """Convert the grid to a tuple for use in a set (for visited states)."""
        return tuple(tuple(row) for row in grid)

    @staticmethod
    def solve(puzzle: Puzzle, apply: Optional[bool] = False) -> List[Vector2]:
        """Solves the puzzle using the A* algorithm with the manhattan heuristic.
        Returns the cost of the solution.
        _________________________________

        apply : if True, the solution will be applied on the puzzle, else, only the moves will be returned.
        """

        pq = []
        initial_state = [row[:]
                         for row in puzzle.grid]  # deep copy of the grid
        initial_node = Solver.Node(
            0 + Solver.manhattan_heuristic(initial_state), 0, initial_state, puzzle.empty_position)

        # f_cost, moves(the moves that were used to get there, the length of this list is the g_cost), grid, empty_position
        heapq.heappush(pq, initial_node)

        visited = set()
        visited.add(Solver._grid_to_tuple(initial_state))

        directions = [Direction.UP.value, Direction.DOWN.value,
                      Direction.LEFT.value, Direction.RIGHT.value]

        while pq:
            current_node = heapq.heappop(pq)
            if current_node.g_cost == current_node.f_cost:
                moves = []
                n = current_node
                while n.parent:
                    moves.insert(0, n.empty_position - n.parent.empty_position)
                    n = n.parent

                if apply:
                    puzzle._grid = current_node.grid
                    puzzle._empty_position = current_node.empty_position

                return moves

            for direction in directions:
                new_grid, new_empty_position = Solver.try_move_simulation(
                    current_node.grid, current_node.empty_position, direction)

                if new_grid is None or new_empty_position is None:
                    continue

                new_grid_tuple = Solver._grid_to_tuple(new_grid)
                if new_grid_tuple in visited:
                    continue

                visited.add(new_grid_tuple)

                new_f_cost = current_node.g_cost + 1 + \
                    Solver.manhattan_heuristic(new_grid)
                new_node = Solver.Node(
                    new_f_cost, current_node.g_cost + 1, new_grid, new_empty_position)

                new_node.parent = current_node
                heapq.heappush(pq, new_node)

        return []
