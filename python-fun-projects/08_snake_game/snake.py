import pygame
import random
from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Snake:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.reset()

    def reset(self):
        start_x = self.grid_width // 2
        start_y = self.grid_height // 2
        self.body = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT

    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= self.grid_width or head[1] < 0 or head[1] >= self.grid_height:
            return True
        if head in self.body[1:]:
            return True
        return False

    def set_direction(self, direction):
        if (self.direction.value[0] * -1, self.direction.value[1] * -1) != direction.value:
            self.next_direction = direction

class Food:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = self.spawn()

    def spawn(self):
        return (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1))

    def respawn(self):
        self.position = self.spawn()

class SnakeGame:
    GRID_SIZE = 20
    GRID_WIDTH = 30
    GRID_HEIGHT = 20
    FPS = 10

    COLORS = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "green": (0, 255, 0),
        "red": (255, 0, 0),
        "gray": (128, 128, 128),
    }

    def __init__(self):
        pygame.init()
        self.width = self.GRID_WIDTH * self.GRID_SIZE
        self.height = self.GRID_HEIGHT * self.GRID_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.symbol_font = pygame.font.Font(None, int(self.GRID_SIZE * 1.5))

        self.snake = Snake(self.GRID_WIDTH, self.GRID_HEIGHT)
        self.food = Food(self.GRID_WIDTH, self.GRID_HEIGHT)
        self.score = 0
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction(Direction.RIGHT)
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.reset_game()
        return True

    def update(self):
        if self.game_over:
            return

        self.snake.move()

        if self.snake.check_collision():
            self.game_over = True
            return

        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.respawn()
            self.score += 10

    def draw(self):
        self.screen.fill(self.COLORS["black"])

        for i, segment in enumerate(self.snake.body):
            x, y = segment
            symbol = "◉" if i == 0 else "●"
            color = (100, 255, 100) if i == 0 else (0, 200, 0)
            sym_surf = self.symbol_font.render(symbol, True, color)
            sym_rect = sym_surf.get_rect(center=(x * self.GRID_SIZE + self.GRID_SIZE // 2,
                                                  y * self.GRID_SIZE + self.GRID_SIZE // 2))
            self.screen.blit(sym_surf, sym_rect)

        fx, fy = self.food.position
        food_surf = self.symbol_font.render("★", True, (255, 200, 50))
        food_rect = food_surf.get_rect(center=(fx * self.GRID_SIZE + self.GRID_SIZE // 2,
                                               fy * self.GRID_SIZE + self.GRID_SIZE // 2))
        self.screen.blit(food_surf, food_rect)

        score_text = self.font.render(f"Score: {self.score}", True, self.COLORS["white"])
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press SPACE to restart", True, self.COLORS["red"])
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    def reset_game(self):
        self.snake.reset()
        self.food.respawn()
        self.score = 0
        self.game_over = False

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)

        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
