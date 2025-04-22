# Graphical Sudoku Game

A simple graphical Sudoku game built with Python and Pygame.

## Features

- Interactive Sudoku board
- Auto-solve functionality
- New game generation
- Win detection
- User-friendly interface
- Notes system for tracking possible values
- Smart notes management - automatic cleanup
- Undo/Redo functionality - track your moves
- Start screen with game options
- Keyboard shortcuts for all functions

## Requirements

- Python 3.x
- Pygame
- NumPy

## Installation

1. Clone this repository or download the files
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```
   python sudoku.py
   ```
2. On the start screen:
   - Press 'S' or click "Start Game" to begin
   - Press 'Q' or click "Quit" to exit
3. In the game:
   - Click on a cell to select it
   - Press a number key (1-9) to enter a number
   - Press Delete or Backspace to clear a number
   - Use keyboard shortcuts or buttons for all functions

## Controls

### Game Functions
- **Mouse Click**: Select a cell
- **Number Keys (1-9)**: Enter a number in the selected cell, or toggle a note when in notes mode
- **Delete/Backspace**: Clear the selected cell and all its notes

### Keyboard Shortcuts
- **N**: Toggle notes mode
- **Z**: Undo last move
- **Y**: Redo move
- **F**: Auto-solve the puzzle
- **R**: Start a new game
- **Q**: Quit the game

### Buttons
- **Solve (F)**: Automatically solve the puzzle
- **Notes (N)**: Toggle between normal mode and notes mode
- **Undo (Z)**: Go back to previous move
- **Redo (Y)**: Go forward to next move
- **New (R)**: Start a new puzzle

## Notes Feature

The notes feature allows you to keep track of possible numbers for each cell:
- Toggle notes mode by clicking the "Notes" button or pressing 'N'
- In notes mode, pressing a number adds a small notation in the selected cell
- Pressing the same number again removes that notation
- Notes are automatically cleared when you place a number in the cell
- Notes appear as small numbers in the corners of empty cells
- **Smart Notes Management**: When you place a number in a cell, all notes for that number will be automatically removed from related cells (same row, column, and 3x3 box)

## Undo/Redo Functionality

The game tracks your moves, allowing you to:
- Undo actions with the Undo button or 'Z' key
- Redo actions with the Redo button or 'Y' key
- Navigate through your entire solving history
- Experiment with different solving paths
- Correct mistakes without starting over

## Game Rules

- Each row must contain the numbers 1-9 without repetition
- Each column must contain the numbers 1-9 without repetition
- Each 3x3 box must contain the numbers 1-9 without repetition
- The game is won when the board is filled correctly 