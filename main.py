import pygame as pg
import sys
from pygame.math import Vector2
from random import randint

# CONSTANTS VALUES
START_POS = randint(0, 25)  # Random start position
SCORE_POS = (335, 15)  # Score showing position
SCORE_COLOR = (225, 225, 225)  # RGB
CELL_SIZE = 25  # Size of a single qube on the screen
CELLS_NUMBER = 30  # Number of qubes on the screen
HEIGHT = CELL_SIZE * CELLS_NUMBER  # Height of the display screen
WIDTH = CELL_SIZE * CELLS_NUMBER  # WIDTH of the display screen
FPS = 60
SNAKE_COLOR = (10, 225, 10)  # RGB
BG_COLOR = (0, 0, 0)  # RGB
SCREEN_UPDATE = pg.USEREVENT
RUN = True
GAME_SPEED = 80
# FRUIT_COLOR = (225, 10, 10)  # Replace by the apple

# SNAKE CLASS
class SNAKE:

    def __init__(self):
        self.body = [Vector2(START_POS, START_POS), Vector2(START_POS - 1, START_POS),
                     Vector2(START_POS - 2, START_POS)]
        self.direction = Vector2(1, 0)
        self.increase_length = False

    def draw(self):
        for cell in self.body:
            x_pos = cell.x * CELL_SIZE
            y_pos = cell.y * CELL_SIZE
            snake_shape = pg.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(screen, SNAKE_COLOR, snake_shape)

    def move(self):
        if self.increase_length:
            body_copy = self.body[:]    # Copy the body of the snake
            body_copy.insert(0, body_copy[0] + self.direction)  # Add a cell to the head position + direction
            self.body = body_copy[:]    # Body = Updated body
            self.increase_length = False    # Stop adding cells
        else:
            body_copy = self.body[:-1]  # Copy body without last cell
            body_copy.insert(0, body_copy[0] + self.direction)  # add cell to the right direction
            self.body = body_copy[:]    # Body = Updated body

    def add_cell(self):
        self.increase_length = True

# FRUIT CLASS
class FRUIT:

    def __init__(self):
        self.x = randint(0, CELLS_NUMBER - 1)
        self.y = randint(0, CELLS_NUMBER - 1)
        self.position = Vector2(self.x, self.y)

    def new_position(self):
        self.x = randint(0, CELLS_NUMBER - 1)
        self.y = randint(0, CELLS_NUMBER - 1)
        self.position = Vector2(self.x, self.y)


class RED_FRUIT(FRUIT):
    def draw(self):
        x_pos = self.x * CELL_SIZE
        y_pos = self.y * CELL_SIZE
        fruit_shape = pg.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        screen.blit(red_apple, fruit_shape)
        # pg.draw.rect(screen, FRUIT_COLOR, fruit_shape)

class GREEN_FRUIT(FRUIT):   # Optional
    def draw(self):
        x_pos = self.x * CELL_SIZE
        y_pos = self.y * CELL_SIZE
        fruit_shape = pg.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        screen.blit(green_apple, fruit_shape)

# MANAGE GAME CLASS
class GAME:

    def __init__(self):
        self.snake = SNAKE()
        self.fruit = RED_FRUIT()
        self.points = 0

    def update(self):
        self.snake.move()
        self.check_eating()
        self.check_if_failed()

    def draw(self):
        self.snake.draw()
        self.fruit.draw()
        self.show_score()

    def increase_points(self):
        if self.points < 10:
            self.points += 1
        elif 10 <= self.points < 100:
            self.points += 10
        else:
            self.points += 20

    def check_eating(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.new_position()
            self.snake.add_cell()
            self.increase_points()

    def show_score(self):
        text = f'SCORE: {self.points}'
        font = pg.font.Font('freesansbold.ttf', 20)
        text = font.render(text, True, SCORE_COLOR)
        screen.blit(text, SCORE_POS)

    def check_if_failed(self):
        # Check if the head of the snake get into the end of the screen
        if not 0 <= self.snake.body[0].x < CELLS_NUMBER or not 0 <= self.snake.body[0].y < CELLS_NUMBER:
            game_over()
        # Check if the head of the snake hit a cell from the body
        for cell in self.snake.body[1:]:
            if cell == self.snake.body[0]:
                game_over()

# FUNCTIONS
def game_over():
    # End the game
    pg.quit()
    sys.exit()


# SETUP
pg.init()  # Initializing pg (pygame) functions
game = GAME()
pg.time.set_timer(SCREEN_UPDATE, GAME_SPEED)  # do SCREEN_UPDATE function every 150 milli-seconds
clock = pg.time.Clock()  # Create clock for fps controlling

# Graphics
screen = pg.display.set_mode((WIDTH, HEIGHT))  # Create a screen with WIDTH and HEIGHT setups
pg.display.set_caption("Itzik's snake!!!")  # Change title
red_apple = pg.image.load('images/red apple.png').convert_alpha()  # Convert photo so pygame can understand and load it
red_apple = pg.transform.scale(red_apple, (CELL_SIZE, CELL_SIZE))  # Transform the size of the image

green_apple = pg.image.load('images/green apple.png').convert_alpha()
green_apple = pg.transform.scale(green_apple, (CELL_SIZE, CELL_SIZE))

# GAME LOOP
while RUN:
    # Check actions of user - ("events")
    for event in pg.event.get():
        if event.type == pg.QUIT:  # If press on 'X' button
            pg.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        # ACTION BY KEYBOARD
        if event.type == pg.KEYDOWN:  # If there is a push on the keyboard
            if event.key == pg.K_UP:
                if game.snake.direction.y != 1:  # If its not a "reverse" command
                    game.snake.direction = Vector2(0, -1)  # Make direction -> UP
            if event.key == pg.K_DOWN:
                if game.snake.direction.y != -1:  # If its not a "reverse" command
                    game.snake.direction = Vector2(0, 1)  # Make direction -> DOWN
            if event.key == pg.K_LEFT:
                if game.snake.direction.x != 1:  # If its not a "reverse" command
                    game.snake.direction = Vector2(-1, 0)  # Make direction -> LEFT
            if event.key == pg.K_RIGHT:
                if game.snake.direction.x != -1:  # If its not a "reverse" command
                    game.snake.direction = Vector2(1, 0)  # Make direction -> RIGHT

    screen.fill(BG_COLOR)  # Paint the background of the screen
    game.draw()
    pg.display.update()  # Update all pygame display setups
    clock.tick(FPS)  # Update the display every <FPS> milli second

# HOW THINGS WORKS?
'''
# PLACE ELEMENTS ON THE SCREEN:
test = pg.Surface((20, 30))    -   create a new surface with a size
test_rect = test.get_rect(PLACE = (xPos, yPos))   -   create rectangle around the surface and costume place
screen.blit(test,test_rect)   -   show on screen
PLACE_OPTIONS: {topleft, midtop, topright, midleft, center, 
                midright, bottomleft, midbottom, bottomright}

* Create a new rectangle:
create_rect = pg.Rect(xPos, Ypos, Width, Height)   -   create a new rectangle
pg.draw.SHAPE_NAME("SCREEN , COLOR, RECTANGLE_NAME)   -   draw rectangle

* Show surface
test.fill((RGB-COLOR))    -    fill the surface with RGB collor
screen.blit(test,(300,400))   -   makes the surface appear on the screen
'''
