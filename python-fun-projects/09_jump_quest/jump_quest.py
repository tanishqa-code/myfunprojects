import pygame
import random

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.velocity = 0
        self.gravity = 0.6
        self.jump_power = -15
        self.ground_y = y

    def jump(self):
        if self.y >= self.ground_y:
            self.velocity = self.jump_power

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y > self.ground_y:
            self.y = self.ground_y
            self.velocity = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y - self.height, self.width, self.height)

    def is_jumping(self):
        return self.y < self.ground_y

class Obstacle:
    def __init__(self, x, ground_y, width=40, height=60):
        self.x = x
        self.y = ground_y - height
        self.width = width
        self.height = height
        self.speed = 7

    def update(self):
        self.x -= self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_offscreen(self):
        return self.x < -self.width

class JumpQuestGame:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400
    FPS = 60

    COLORS = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "cyan": (0, 255, 255),
        "red": (255, 0, 0),
        "yellow": (255, 255, 0),
    }

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Jump Quest - Avoid Obstacles!")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.symbol_font = pygame.font.Font(None, 50)

        self.player = Player(50, self.SCREEN_HEIGHT - 120)
        self.obstacles = []
        self.score = 0
        self.game_over = False
        self.obstacle_spawn_timer = 0
        self.obstacle_spawn_rate = 80

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.reset_game()
                    else:
                        self.player.jump()
        return True

    def update(self):
        if self.game_over:
            return

        self.player.update()

        self.obstacle_spawn_timer += 1
        if self.obstacle_spawn_timer > self.obstacle_spawn_rate:
            self.obstacles.append(Obstacle(self.SCREEN_WIDTH, self.player.ground_y))
            self.obstacle_spawn_timer = 0
            if self.obstacle_spawn_rate > 40:
                self.obstacle_spawn_rate -= 2

        for obstacle in self.obstacles:
            obstacle.update()

            if obstacle.get_rect().colliderect(self.player.get_rect()):
                self.game_over = True
                return

            if obstacle.is_offscreen():
                self.obstacles.remove(obstacle)
                self.score += 10

    def draw(self):
        self.screen.fill(self.COLORS["black"])

        player_rect = self.player.get_rect()
        pygame.draw.rect(self.screen, self.COLORS["cyan"], player_rect)
        pygame.draw.rect(self.screen, self.COLORS["white"], player_rect, 2)

        for obstacle in self.obstacles:
            obs_rect = obstacle.get_rect()
            pygame.draw.rect(self.screen, self.COLORS["red"], obs_rect)
            pygame.draw.rect(self.screen, self.COLORS["yellow"], obs_rect, 2)

        score_text = self.font.render(f"Score: {self.score}", True, self.COLORS["white"])
        self.screen.blit(score_text, (10, 10))

        if not self.game_over:
            instruction_text = self.font.render("Press SPACE to jump!", True, self.COLORS["yellow"])
            self.screen.blit(instruction_text, (self.SCREEN_WIDTH - 350, 10))

        if self.game_over:
            game_over_surf = self.symbol_font.render("GAME OVER!", True, self.COLORS["red"])
            game_over_rect = game_over_surf.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(game_over_surf, game_over_rect)

            final_score_text = self.font.render(f"Final Score: {self.score}", True, self.COLORS["white"])
            final_rect = final_score_text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 + 20))
            self.screen.blit(final_score_text, final_rect)

            restart_text = self.font.render("Press SPACE to restart", True, self.COLORS["cyan"])
            restart_rect = restart_text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 + 80))
            self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    def reset_game(self):
        self.player = Player(50, self.SCREEN_HEIGHT - 120)
        self.obstacles = []
        self.score = 0
        self.game_over = False
        self.obstacle_spawn_timer = 0
        self.obstacle_spawn_rate = 80

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)

        pygame.quit()

if __name__ == "__main__":
    game = JumpQuestGame()
    game.run()
