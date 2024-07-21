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

        self.ball = entities.Ball((255, 255, 255), 300, 300, 10, 5, 5)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # ball initial movement and bouncing off walls
            if self.ball.x + self.ball.size >= 600 or self.ball.x - self.ball.size < 0:
                self.ball.velocity[0] = -self.ball.velocity[0]
            if self.ball.y + self.ball.size >= 600 or self.ball.y - self.ball.size < 0:
                self.ball.velocity[1] = -self.ball.velocity[1]
            #circle movement and bouncing
            self.ball.x += self.ball.velocity[0]
            self.ball.y += self.ball.velocity[1]
            # Collision detection
            if self.ball.x - (self.paddle1.x + self.paddle1.width) <= self.ball.size:
                # check if ball is hitting top or bottom of paddle 1
                self.ball.velocity[0] *= -1
            if (self.paddle2.x + self.paddle2.width)- self.ball.x <= self.ball.size:
                self.ball.velocity[0] *= -1
            
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

            

            # ball movement
            if pressed[pygame.K_i]:
                self.ball.move_up(5)
            if pressed[pygame.K_k]:
                self.ball.move_down(5)
            if pressed[pygame.K_j]:
                self.ball.move_left(5)
            if pressed[pygame.K_l]:
                self.ball.move_right(5)

            # Reset screen to black
            self.window.fill((0, 0, 0))

            # Update entities
            self.paddle1.draw(self.window)
            self.paddle2.draw(self.window)

            self.ball.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)

Game().run()