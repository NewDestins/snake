import keyboard

class Snake:
    def __init__(self, x, y, direction='right') -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.symbol = 'S'
        self.body = [(x, y)]  # List to store body parts, starting with the head
    
    def change_direction(self):
        if keyboard.is_pressed('w') and self.direction != 'down':
            self.direction = 'up'
        elif keyboard.is_pressed('s') and self.direction != 'up':
            self.direction = 'down'
        elif keyboard.is_pressed('a') and self.direction != 'right':
            self.direction = 'left'
        elif keyboard.is_pressed('d') and self.direction != 'left':
            self.direction = 'right'
    
    def move(self):
        # Add new head position based on the direction
        if self.direction == 'up':
            new_head = (self.x, self.y - 1)
        elif self.direction == 'down':
            new_head = (self.x, self.y + 1)
        elif self.direction == 'left':
            new_head = (self.x - 1, self.y)
        elif self.direction == 'right':
            new_head = (self.x + 1, self.y)
        
        # Insert new head at the beginning of the body list
        self.body.insert(0, new_head)
        
        # Remove the last element if the snake didn't eat any food (i.e., keep the same length)
        if len(self.body) > 1:
            self.body.pop()

        # Update head coordinates
        self.x, self.y = new_head
    
    def eat_fruit(self):
        self.body.append(self.body[-1])

    def check_death(self, harta):
        if self.x <= 0 or self.x >= len(harta[0]) - 1 or self.y <= 0 or self.y >= len(harta)-1:
            return True
        return False

    def draw(self, harta):
        # Draw the head
        harta[self.y][self.x] = self.symbol
        
        # Draw the body parts
        for x, y in self.body[1:]:
            harta[y][x] = self.symbol
