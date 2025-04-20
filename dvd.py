import pygame
import os

class DVD:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("DVD Screensaver")
        self.clock = pygame.time.Clock()

        # Load the DVD image
        self.dvd_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "pixalwan.png"))
        self.dvd_rect = self.dvd_image.get_rect()
        self.dvd_rect.x = 400
        self.dvd_rect.y = 300

        # Set initial speed
        self.x_speed = 4
        self.y_speed = 5

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update position
            self.dvd_rect.x += self.x_speed
            self.dvd_rect.y += self.y_speed

            # Bounce off walls
            if self.dvd_rect.right >= 800 or self.dvd_rect.left <= 0:
                self.x_speed = -self.x_speed
            if self.dvd_rect.bottom >= 600 or self.dvd_rect.top <= 0:
                self.y_speed = -self.y_speed

            # Clear the screen
            self.window.fill((255, 255, 255))

            # Draw the DVD logo
            self.window.blit(self.dvd_image, self.dvd_rect)

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)
        if not running:
            pygame.quit()
            exit()
       

if __name__ == "__main__":
    dvd = DVD()
    dvd.run()