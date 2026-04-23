import pygame
import random

class Snake:
    def __init__(self):
        self.size = 20
        self.body = [(300, 200)]  
        self.dx = self.size
        self.dy = 0
        self.grow = False  

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)
        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                (0, 200, 0),
                (segment[0], segment[1], self.size, self.size)
            )

    def change_direction(self, dx, dy):
        if self.dx == -dx and self.dy == -dy:
            return
        self.dx = dx
        self.dy = dy

def generate_food(snake, width, height, size):
    while True:
        x = random.randint(0, (width // size) - 1) * size
        y = random.randint(0, (height // size) - 1) * size
        if (x, y) not in snake.body:
            return (x, y)