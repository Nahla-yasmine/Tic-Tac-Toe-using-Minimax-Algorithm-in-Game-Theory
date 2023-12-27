# Tic-Tac-Toe-using-Minimax-Algorithm-in-Game-Theory
This Python project features a classic Tic Tac Toe game where players challenge an AI opponent using the minimax algorithm for optimal moves.

# #Tic Tac Toe Game with Minimax AI

This is a simple implementation of the classic Tic Tac Toe game in Python, featuring an AI opponent that uses the minimax algorithm to play optimally. The minimax algorithm logic was adapted from [GeeksforGeeks](https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/).

## Overview

The `TicTacToe` class initializes a game board and provides methods to display the board, make moves, check for a winner, and let the AI play against a human player.

### Methods:

- `__init__()`: Initializes the game with an empty board.
- `show()`: Displays the current state of the board.
- `clearBoard()`: Clears the board for a new game.
- `whoWon()`: Determines the winner or declares a draw.
- `availableMoves()`: Returns available positions for a move.
- `makeMove(position, player)`: Places a player's move on the board.
- `checkWin(player)`: Checks if a player has won.
- `gameOver()`: Checks if the game is over.
- `minimax(depth, isMaximizingPlayer)`: Implements the minimax algorithm for the AI. Source: [GeeksforGeeks](https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/)
- `findBestMove()`: Finds the best move for the AI using minimax.

## How to Play

1. Run the code.
2. Enter a number (1-9) to place your 'X' on the board.
3. The AI (playing 'O') will make its move.
4. The game continues until someone wins or it's a draw.

## Usage

Run the script and follow the console prompts to play the game.

```python
python MinMaxAlgorithme.py
