# Number Guessing Game with Search Algorithms

## Project Overview

This project is an extension of the classic **Number Guessing Game**, where different search algorithms are applied to allow an AI to guess a secret number. In addition to the Non-AI version where a player guesses a number, this project includes AI-driven versions using search algorithms such as **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Simulated Annealing**. The goal is to explore how various search techniques perform in the context of a number-guessing problem.

## Features

The following versions of the Number Guessing Game have been implemented:

1. **Non-AI Version: Player vs Computer**
   - The player attempts to guess a secret number chosen by the computer. The computer provides feedback on whether the guess is too high or too low.

2. **AI Version: BFS (Breadth-First Search)**
   - The AI uses the BFS algorithm to guess the number, gradually narrowing down the range based on feedback from the user.

3. **AI Version: DFS (Depth-First Search)**
   - The AI uses the DFS algorithm to guess the number, exploring possible guesses deeply before moving to the next possible option.

4. **Custom AI Algorithm: Simulated Annealing**
   - The AI uses the Simulated Annealing algorithm to guess the number. This technique introduces randomness, allowing the AI to explore different guesses and reduce its uncertainty over time.

## Algorithms Explanation

1. **Non-AI Version: Player vs Computer**
   - The player interacts with the game by providing guesses, while the computer gives feedback (e.g., "too high" or "too low"). The game continues until the player correctly guesses the number.

2. **Breadth-First Search (BFS)**
   - BFS is implemented using a queue that contains all possible numbers within the provided range. The AI makes its guesses in a level-order manner, progressively narrowing down the list based on feedback.
   
3. **Depth-First Search (DFS)**
   - DFS uses a stack to explore possible numbers. The AI dives deep into one set of possible guesses, backtracking when necessary based on user feedback.

4. **Simulated Annealing**
   - In this custom AI approach, the AI starts with a random guess and explores neighboring guesses, adjusting its exploration level (analogous to temperature) over time. The exploration level decreases, reducing the randomness and helping the AI converge toward the correct answer.

## Code Structure

- The code is modular and well-commented to clarify how each algorithm works.
- Print statements are used to show the number of attempts each algorithm takes to guess the correct number.
- Separate functions have been created for each version of the game:
  - `player_vs_computer()`: Non-AI version.
  - `bfs_guess()`: BFS-based AI version.
  - `dfs_guess()`: DFS-based AI version.
  - `simulated_annealing_guess()`: Custom AI version using Simulated Annealing.

## How to Run the Game

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/number-guessing-game
   ```

2. Navigate to the project directory:
   ```bash
   cd number-guessing-game
   ```

3. Run the Python script:
   ```bash
   python number_guessing_game.py
   ```

4. Choose which version of the game you would like to play:
   - **Option 1**: AI using Breadth-First Search (BFS)
   - **Option 2**: AI using Depth-First Search (DFS)
   - **Option 3**: AI using Simulated Annealing
   - **Option 4**: Non-AI Player vs Computer version

5. For AI versions, provide feedback on whether the AI's guess is too high (`h`), too low (`l`), or correct (`c`).

## Future Extensions

- Implement additional algorithms such as **Genetic Algorithms**, **Monte Carlo Search**, or other optimization techniques.
- Add a graphical user interface (GUI) for better user interaction.
- Introduce a scoring system based on how quickly the AI guesses the number.

## License

This project is open-source and available under the MIT License.

## Author

Afnan Bin Abbas - (https://github.com/AfnanBinAbbas)

---

This project demonstrates how various search algorithms can be applied to simple games like Number Guessing, offering a fun way to explore the performance of different strategies.
