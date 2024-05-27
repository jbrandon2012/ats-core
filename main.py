import pygame, sys
from settings import *
from level import Level

import pygame, sys
from settings import *
from level import Level

class HomePage:
    def __init__(self):
        # Initialize Pygame's mixer for music
        pygame.mixer.init()
        
        # Load and play music
        pygame.mixer.music.load('audio/aot_main_theme.mp3')
        pygame.mixer.music.play(-1)  # Loop indefinitely

        # Display settings
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 74)
        self.title_text = self.font.render("Kepler 94b", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        self.start_text = pygame.font.Font(None, 50).render("Press Enter to Start", True, (255, 255, 255))
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

    def display(self):
        self.display_surface.fill((0, 0, 0))  # Black background
        self.display_surface.blit(self.title_text, self.title_rect)
        self.display_surface.blit(self.start_text, self.start_rect)
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    return True
        return False

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Kepler 94b, A Space Odyssey')
        self.clock = pygame.time.Clock()
        self.home_page = HomePage()
        self.level = Level()
        self.show_home_page = True

    def run(self):
        while True:
            if self.show_home_page:
                self.home_page.display()
                if self.home_page.handle_events():
                    self.show_home_page = False
                    # pygame.mixer.music.stop()  # Stop home page music
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                dt = self.clock.tick() / 1000
                self.level.run(dt)
                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()


