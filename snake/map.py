from fruit import *
from snake import *
import time

fruit = Fruit(3, 3)
snake = Snake(3, 5)


class Map:
    def __init__(self, height, width) -> None:
        self.map = [[' 'for _ in range(width)] for _ in range(height)]

    def draw_map(self):
        horizontal_boder = f'+{"-"*len(self.map[0])}+'
        for row_index, row in enumerate(self.map):
            if row_index == 0 or row_index == len(self.map) - 1:
                print(horizontal_boder)
            print(f'|{"".join(row)}|')
    
    def clean_screen(self):
        for row in self.map:
            for i in range(len(row)):
                row[i] = ' '
    
    def game_over(self):
        print("Game Over!")
        time.sleep(10)  # Wait for 2 seconds before restarting
        self.clean_screen()  # Clear the screen
        global snake, fruit
        snake = Snake(3, 10)  # Create a new snake object at initial position
        fruit = Fruit(5, 20)  # Create a new fruit object at initial position
    
    def update_snake(self):
        print(f'snake pos = ({snake.x},{snake.y})')
        print(len(self.map[0]) - 1)
        snake.change_direction()
        snake.move()
        snake.draw(self.map)
        # print(f'Snake coord ({snake.x},{snake.y})')
        if snake.check_death(harta=self.map):
            self.game_over()

    def update_fruit(self):
        fruit.display(self.map)
        fruit.check_collision(snake, self.map)

    def update(self):
        self.draw_map()
        self.clean_screen()
        self.update_snake()
        self.update_fruit()
    