import pygame
import sys
import random

import entities

class Game:

    player1_score = 0
    player2_score = 0

    state = "running"
    state_counter = 0

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()

        self.paddle1 = entities.Paddle((255, 255, 255), 10, 200, 10, 100)
                                        #color           x   y  width height
        self.paddle2 = entities.Paddle((255, 255, 255), 580, 200, 10, 100)

        #self.ball_random_y_pos = random.randint(10, 500)
        self.ball = entities.Ball((255, 255, 255), 300, 10, 10, 5, 5)

        self.font = pygame.font.Font("Arial.ttf", 32)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #pause key press
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        Game.state_counter += 1
                        if Game.state_counter % 2 == 0:
                            Game.state = "running"
                        else:
                            Game.state = "paused"
            
            if Game.state == "running":
                if self.ball.x + self.ball.size >= 600:
                    Game.player1_score += 1
                    print(f"Player 1: {self.player1_score}, Player 2: {self.player2_score}")
                    Game().run()
                
                if self.ball.x - self.ball.size < 0:
                    Game.player2_score += 1
                    print(f"Player 1: {self.player1_score}, Player 2: {self.player2_score}")
                    Game().run()

                # ball bouncing off walls
                if self.ball.y + self.ball.size >= 600 or self.ball.y - self.ball.size < 0:
                    self.ball.velocity[1] *= -1
                #circle movement and bouncing
                self.ball.x += self.ball.velocity[0]
                self.ball.y += self.ball.velocity[1]
                # Collision detection
                if self.ball.x - (self.paddle1.x + self.paddle1.width) <= self.ball.size and self.ball.y >= self.paddle1.y and self.ball.y <= self.paddle1.y + self.paddle1.height:
                    self.ball.velocity[0] *= -1

                    #Check if ball hit top or bottom of paddle1
                    if self.ball.y < self.paddle1.y + self.paddle1.height / 2: # top
                        self.ball.velocity[1] = -5
                    if self.ball.y > self.paddle1.y + self.paddle1.height / 2: # bottom
                        self.ball.velocity[1] = 5
                    
                if (self.paddle2.x + self.paddle2.width) - self.ball.x <= self.ball.size and self.ball.y >= self.paddle2.y and self.ball.y <= self.paddle2.y + self.paddle2.height:
                    self.ball.velocity[0] *= -1

                    #Check if ball hit top or bottom of paddle2
                    if self.ball.y < self.paddle2.y + self.paddle2.height / 2: # top
                        self.ball.velocity[1] = -5
                    if self.ball.y > self.paddle2.y + self.paddle2.height / 2: # bottom
                        self.ball.velocity[1] = 5
                
                pressed = pygame.key.get_pressed()
                # Paddle 1 movement (player controlled)
                if pressed[pygame.K_w]:
                    self.paddle1.move_up(5)
                if pressed[pygame.K_s]:
                    self.paddle1.move_down(5)
                # Paddle 2 movement (player controlled)
                if self.ball.y > self.paddle2.y + self.paddle2.height / 2:
                    self.paddle2.move_down(4)
                if self.ball.y < self.paddle2.y + self.paddle2.height / 2:
                    self.paddle2.move_up(4)

                # Reset screen to black
                self.window.fill((0, 0, 0))

                # Update entities
                self.player1_score_text = self.font.render(f"Player 1: {Game.player1_score}", True, (255, 255, 255))
                self.window.blit(self.player1_score_text, (10, 10))

                self.player2_score_text = self.font.render(f"Player 2: {Game.player2_score}", True, (255, 255, 255))
                self.window.blit(self.player2_score_text, (430, 10))

                self.paddle1.draw(self.window)
                self.paddle2.draw(self.window)

                self.ball.draw(self.window)

                pygame.display.update()
                self.clock.tick(60)

            else:
                pygame.display.update()
                self.clock.tick(60)
                
                continue

Game().run()