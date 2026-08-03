import pygame

WIDTH, HEIGHT = 600, 400
BALL_SIZE = 30
SPEED = 5

def play():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball")
    clock = pygame.time.Clock()

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = SPEED, SPEED
    color = (255, 100, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x += dx
        y += dy

        if x <= 0 or x + BALL_SIZE >= WIDTH:
            dx = -dx
            color = tuple(min(255, c + 40) % 256 for c in color)
        if y <= 0 or y + BALL_SIZE >= HEIGHT:
            dy = -dy
            color = tuple(min(255, c + 40) % 256 for c in color)

        screen.fill((20, 20, 30))
        pygame.draw.ellipse(screen, color, (x, y, BALL_SIZE, BALL_SIZE))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    play()
