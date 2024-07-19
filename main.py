import pygame
import sys

import entities

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        self.paddle1 = entities.Paddle((255, 255, 255), 10, 200, 10, 100)
                                        #color           x   y  width height
        self.paddle2 = entities.Paddle((255, 255, 255), 580, 200, 10, 100) 

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pressed = pygame.key.get_pressed()
            #Paddle 1 movement
            if pressed[pygame.K_w]:
                self.paddle1.move_up(5)
            if pressed[pygame.K_s]:
                self.paddle1.move_down(5)
            #Paddle 2 movement
            if pressed[pygame.K_UP]:
                self.paddle2.move_up(5)
            if pressed[pygame.K_DOWN]:
                self.paddle2.move_down(5)


            # Reset screen to black
            self.window.fill((0, 0, 0))

            # Update entities
            self.paddle1.draw(self.window)
            self.paddle2.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)

Game().run()