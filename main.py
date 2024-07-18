import pygame
import sys

import entities

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))

        self.clock = pygame.time.Clock()


    def run(self):
        global ball
        ball = entities.Ball((255, 0, 0), 10)

        global paddle1
        paddle1 = entities.Paddle((0, 255, 0), 10, 100)

        global paddle2
        paddle2 = entities.Paddle((0, 0, 255), 10, 100)
        

        while True:

            ball.draw(self.window, 300, 300)

            paddle1.draw(self.window, 10, 300)
            paddle2.draw(self.window, 590, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)


Game().run()


