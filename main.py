import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)


def main():
    difficulty_selected = False
    running = True

    while running:
        SCREEN.fill(BLACK)

        # Always process events first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if not difficulty_selected:
                    if event.key == pygame.K_1:
                        engine.set_difficulty("Easy")
                        difficulty_selected = True
                    elif event.key == pygame.K_2:
                        engine.set_difficulty("Medium")
                        difficulty_selected = True
                    elif event.key == pygame.K_3:
                        engine.set_difficulty("Hard")
                        difficulty_selected = True
                else:
                    engine.handle_keydown(event.key)

        # Show difficulty selection screen
        if not difficulty_selected:
            title_font = pygame.font.SysFont("Arial", 50)
            option_font = pygame.font.SysFont("Arial", 30)

            title = title_font.render("Choose Difficulty", True, WHITE)
            easy = option_font.render("1 - Easy", True, WHITE)
            medium = option_font.render("2 - Medium", True, WHITE)
            hard = option_font.render("3 - Hard", True, WHITE)

            SCREEN.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)))
            SCREEN.blit(easy, easy.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
            SCREEN.blit(medium, medium.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
            SCREEN.blit(hard, hard.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70)))
        else:
            engine.handle_input()
            engine.update()
            engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
