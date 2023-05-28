# Snake Game

This is a simple implementation of the classic Snake game using the Pygame library. The game features a snake that moves around the screen and tries to eat fruits to increase its length and score. The game ends if the snake hits the boundaries of the screen or collides with its own body.

## Prerequisites

To run this game, make sure you have Python installed on your system. Additionally, you need to have the Pygame library installed. You can install Pygame using the following command:

## Instructions

1. Clone or download the repository to your local machine.
2. Make sure you have the required images for the fruits (`red apple.png` and `green apple.png`) in the `images` folder.
3. Run the `snake_game.py` file using the following command:
4. Use the arrow keys on your keyboard to control the movement of the snake.
5. Try to eat the red fruits to increase your score. Green fruits (optional) can also be added for additional gameplay elements.
6. The game will end if the snake hits the boundaries of the screen or collides with its own body.

## Game Controls

- Up Arrow: Move the snake upwards.
- Down Arrow: Move the snake downwards.
- Left Arrow: Move the snake to the left.
- Right Arrow: Move the snake to the right.
- X Button (Window Close): Quit the game.

## Customization

You can customize certain aspects of the game by modifying the constants in the code:

- `CELL_SIZE`: The size of each cell (square) on the screen.
- `CELLS_NUMBER`: The number of cells in each row and column of the screen.
- `FPS`: The frames per second at which the game runs.
- `GAME_SPEED`: The speed at which the snake moves.
- `SNAKE_COLOR`: The color of the snake.
- `BG_COLOR`: The background color of the screen.

Feel free to modify these constants to change the appearance and behavior of the game.

**Note:** If you want to use different fruit images, make sure to replace the `red apple.png` and `green apple.png` files in the `images` folder and update the corresponding code in the `FRUIT` and `GREEN_FRUIT` classes.

## Acknowledgements

- This game was created by Itzik Rahamim ([GitHub](https://github.com/eizikr)).
- The game is built using the Pygame library.

Have fun playing the Snake game!
