import random

class Fruit:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.symbol = 'F'
    
    def delete(self, harta):
        harta[self.y][self.x] = ' '

    def check_collision(self, snake, harta):
        if self.x == snake.x and self.y == snake.y:
            self.delete(harta)
            self.x = random.randint(1, len(harta) - 1)
            self.y = random.randint(1, len(harta) - 1)
            snake.eat_fruit()

    def display(self, harta):
        harta[self.y][self.x] = self.symbol