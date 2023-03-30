import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, position, size, sprite):
        super().__init__()
        self.image = pygame.image.load(sprite).convert()


class Game():
    def __init__(self):
        
        # pygame setup
        pygame.init() 
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        screen = pygame.display.set_mode((1280, 720))
        running = True

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")

            # RENDER YOUR GAME HERE
            sprite = pygame.sprite.Sprite()
            sprite.posir

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60


            #change


game = Game()