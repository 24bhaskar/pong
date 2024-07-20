import pygame
pygame.init()

class Ball():

    def __init__(self, color, x, y, size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def bounce(self):
        pass
    
    def move_up(self, speed):
        if self.y > 0:
            self.y -= speed
    
    def move_down(self, speed):
        if self.y < 600:
            self.y += speed

    def move_left(self, speed):
        if self.x > 0:
            self.x -= speed
        
    def move_right(self, speed):
        if self.x < 600:
            self.x += speed

class Paddle():

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move_up(self, speed):
        if self.y > 0:
            self.y -= speed
    
    def move_down(self, speed):
        if self.y < 600 - self.height:
            self.y += speed