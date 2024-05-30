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
        
        # Load background image
        self.background = pygame.image.load('graphics/homescreen/IMG_0002.png')
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.font = pygame.font.Font(None, 74)

        self.start_text = pygame.font.Font(None, 50).render("Press Enter to Start", True, (255, 255, 255))
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))

    def display(self):
        # Draw the background image
        self.display_surface.blit(self.background, (0, 0))
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

