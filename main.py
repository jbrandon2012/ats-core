import pygame, sys, os
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
        
        # Load and resize background images dynamically from folder
        self.background_frames = self.load_background_frames('graphics/homescreen')
        if not self.background_frames:
            raise FileNotFoundError("No background frames found in the specified directory.")
        self.current_frame = 0
        self.frame_count = len(self.background_frames)
        self.frame_delay = 980  # Milliseconds per frame
        self.last_update_time = pygame.time.get_ticks()
        
        self.font = pygame.font.Font(None, 74)

        self.start_text = pygame.font.Font(None, 50).render("Press Enter to Start", True, (255, 255, 255))
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))  # Adjusted y-coordinate

    def load_background_frames(self, folder):
        frames = []
        for filename in sorted(os.listdir(folder)):
            if filename.endswith('.PNG'):
                img_path = os.path.join(folder, filename)
                print(f"Loading image: {img_path}")  # Debugging statement
                img = pygame.image.load(img_path)
                img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
                frames.append(img)
        return frames

    def update_background(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.frame_delay:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_update_time = current_time

    def display(self):
        self.update_background()
        # Draw the current background frame
        self.display_surface.blit(self.background_frames[self.current_frame], (0, 0))
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
