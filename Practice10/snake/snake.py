import random

class Snake:
    def __init__(self, size=20):
        self.size = size
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

    def change_direction(self, dx, dy):
        # Prevent 180-degree turns (reversing into yourself)
        if (self.dx == -dx and self.dy == -dy):
            return
        self.dx = dx
        self.dy = dy

def generate_food(snake_body, width, height, size):
    while True:
        x = random.randint(0, (width // size) - 1) * size
        y = random.randint(0, (height // size) - 1) * size
        if (x, y) not in snake_body:
            return (x, y)