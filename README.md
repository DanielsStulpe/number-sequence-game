# Number Sequence Game

A turn-based strategy game built using Python and Tkinter. The player competes against a computer opponent using either the Min-Max or Alpha-Beta pruning algorithm.

## Features

* Intuitive graphical user interface using Tkinter
* Choice of AI algorithm: Min-Max or Alpha-Beta
* Choose who starts the game: Player or Computer
* Selectable sequence length (15 to 25 numbers)
* Visual feedback and score tracking
* Endgame screen displaying the winner and final scores

## Game Rules

* At the start, a number sequence is generated, and both players start with 100 points.
* Players take turns picking one number from the sequence.
* If a **even number** is picked: **twice its value is subtracted from the player's points**.
* If an **odd number** is picked: **its value is added to the opponent's points**.
* The game ends when the sequence is empty.
* The player with **fewer points** at the end wins.
* If both players have the same number of points, the game is a draw.

## How to Play

1. Launch the application.
2. Click "Play".
3. Choose an AI algorithm (Min-Max or Alpha-Beta).
4. Choose who plays first (Player or Computer).
5. Select the sequence length (between 15 and 25).
6. Take turns picking numbers from the sequence.
7. The game ends when no numbers remain.

## Requirements

* Python 3.x
* Tkinter (comes pre-installed with standard Python distributions)

## Installation

1. Clone the repository or download the source files.
2. Ensure `node.py` and `algorithms.py` are located in the same directory as `main.py`.
3. Run the game with:

```bash
python main.py
```

## File Structure

```
/your_project_directory
│
├── main.py              # Main application and GUI
├── node.py              # Game logic and scoring rules
├── algorithms.py        # AI algorithms: Min-Max and Alpha-Beta
```

## License

This project is intended for educational and demonstration purposes only.
