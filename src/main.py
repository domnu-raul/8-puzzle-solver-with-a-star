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

cell_size = screen.get_width() / 9
grid_start = pygame.Vector2(screen.get_width() / 3 * 2 - 100,
                            (screen.get_height() - cell_size * 3) // 2)

button_size = pygame.Vector2(400, 150)
button_gap = 20
buttons_start = pygame.Vector2(
    100, (screen.get_height() - button_size.y * 2 - button_gap) // 2)

scramble_button = pygame.Rect(
    buttons_start.x, buttons_start.y, button_size.x, button_size.y)
solve_button = pygame.Rect(
    buttons_start.x, buttons_start.y + 170, button_size.x, button_size.y)


font = pygame.font.Font(None, 36)
rect_color = (255, 255, 255)
timer = 0

moves = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if scramble_button.collidepoint(event.pos):
                puzzle.scramble()
                rect_color = (255, 255, 255)
                moves = []
            elif solve_button.collidepoint(event.pos):
                moves = puzzle.solve()

    screen.fill("black")
    timer += dt

    for y, row in enumerate(puzzle.grid):
        for x, cell in enumerate(row):

            cell_start = pygame.Vector2(
                grid_start.x + x * cell_size, grid_start.y + y * cell_size)

            rect = pygame.Rect(cell_start.x, cell_start.y,
                               cell_size - 5, cell_size - 5)

            pygame.draw.rect(screen, rect_color, rect)

            if cell == 0:
                continue

            pos = font.render(str(cell), True, "black")
            screen.blit(pos, (cell_start.x + (cell_size // 2 - 5),
                        cell_start.y + (cell_size // 2 - 10)))

    pygame.draw.rect(screen, "white", scramble_button)
    pygame.draw.rect(screen, "white", solve_button)

    scramble_text = font.render("Scramble", True, "black")
    solve_text = font.render("Solve", True, "black")
    screen.blit(scramble_text, (buttons_start.x + 100, buttons_start.y + 50))
    screen.blit(solve_text, (buttons_start.x + 100, buttons_start.y + 220))

    if timer > 0.15 and moves:
        move = moves.pop(0)
        puzzle.move(move)
        timer = 0

    if puzzle.is_solved:
        rect_color = (0, 255, 0)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
