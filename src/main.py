import pygame
from src.puzzle import Puzzle, Direction

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
puzzle = Puzzle()
puzzle.scramble()
moves = puzzle.solve()

cell_size = screen.get_width() / 9
grid_start = pygame.Vector2(screen.get_width() / 3,
                            (screen.get_height() - cell_size * 3) // 2)
font = pygame.font.Font(None, 36)
timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     match event.key:
        #         case pygame.K_s:
        #             puzzle.move(Direction.UP)
        #         case pygame.K_w:
        #             puzzle.move(Direction.DOWN)
        #         case pygame.K_d:
        #             puzzle.move(Direction.LEFT)
        #         case pygame.K_a:
        #             puzzle.move(Direction.RIGHT)
        #         case _:
        #             pass
        #
    screen.fill("black")
    timer += dt

    for y, row in enumerate(puzzle.grid):
        for x, cell in enumerate(row):

            cell_start = pygame.Vector2(
                grid_start.x + x * cell_size, grid_start.y + y * cell_size)
            rect = pygame.Rect(cell_start.x, cell_start.y,
                               cell_size - 5, cell_size - 5)

            pygame.draw.rect(screen, "white", rect)

            if cell == 0:
                continue

            pos = font.render(str(cell), True, "black")
            screen.blit(pos, (cell_start.x + (cell_size // 2 - 5),
                        cell_start.y + (cell_size // 2 - 10)))

    if timer > 1 and moves:
        move = moves.pop(0)
        puzzle.move(move)
        timer = 0

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
