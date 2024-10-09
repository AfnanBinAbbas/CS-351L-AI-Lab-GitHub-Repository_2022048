---

# Number Guessing Game with AI Search Algorithms

This project extends the traditional Number Guessing Game by incorporating various search algorithms, allowing the AI to guess the number based on user feedback.

## Game Versions

1. **Non-AI Version: Player vs Computer**  
   In this version, the player attempts to guess a randomly selected number by the computer. The computer gives feedback on whether the player's guess is too high, too low, or correct. The game continues until the player guesses the correct number.

2. **AI Version: Binary Search (Computer guesses player's number)**  
   In this version, the AI attempts to guess a number that the player is thinking of, using the binary search algorithm. The player provides feedback on whether the AI's guess is too high, too low, or correct. Binary search efficiently narrows down the range, making the AI's guessing process fast and accurate.
   
   - **Algorithm**: The AI guesses the middle number between the current low and high bounds. If the guess is too high, it adjusts the high bound; if too low, it adjusts the low bound, thus halving the search space in each step.
   
   - **How it works**:  
     1. Player thinks of a number between 1 and 100.  
     2. The AI guesses the middle value between the current low and high bounds.  
     3. The player provides feedback (`h` for too high, `l` for too low, `c` for correct).  
     4. The AI adjusts the bounds and continues guessing until it finds the correct number.  

3. **BFS Version: AI using Breadth-First Search (BFS)**  
   In this version, the AI uses BFS to guess the number. The AI goes through all possible numbers sequentially from the lowest to the highest, based on the player's feedback.
   
   - **Algorithm**: BFS maintains a queue of potential guesses, starting from the lowest value in the range. It systematically eliminates numbers that are too high or too low based on feedback.

4. **DFS Version: AI using Depth-First Search (DFS)**  
   In this version, the AI uses DFS to guess the number. The AI explores potential guesses by checking the highest values first (LIFO approach), adjusting its guesses based on the player's feedback.
   
   - **Algorithm**: DFS uses a stack to explore potential numbers. It guesses a number and pops the stack, removing numbers that are either too high or too low.

5. **Custom Algorithm: Simulated Annealing**  
   In this version, the AI uses Simulated Annealing to guess the number. It starts with a random guess and progressively refines the guess by exploring neighboring numbers. The AI can sometimes make worse guesses but gradually "cools down" to refine its guesses.

   - **Algorithm**:  
     1. The AI randomly guesses a number.  
     2. It calculates a neighboring guess by randomly moving within a defined range around the current guess.  
     3. The algorithm accepts better guesses and occasionally worse guesses to escape local optima, but over time it becomes more conservative (i.e., it "cools down").  
     4. The process continues until the AI finds the correct number or the temperature (exploration level) becomes too low.

## Code Structure

- **player_vs_computer()**: Implements the Non-AI version where the player guesses the computer's number.
- **ai_number_guessing_game()**: AI guesses the player's number using Binary Search.
- **bfs_guess()**: Implements the BFS algorithm where the AI guesses using breadth-first search.
- **dfs_guess()**: Implements the DFS algorithm where the AI guesses using depth-first search.
- **simulated_annealing_guess()**: AI uses Simulated Annealing to find the correct number.

## Features

- **User Feedback**: In each AI version, the player provides feedback to help the AI refine its guesses. Feedback options include:
  - `h`: Too high
  - `l`: Too low
  - `c`: Correct
  
- **Attempts Tracking**: In the Non-AI version, the game tracks the number of attempts it takes for the player to guess the number. For AI algorithms, this is done implicitly as the algorithms optimize their guessing strategies.

## How to Run

1. Clone the repository.
2. Run the Python file `number_guessing_game.py`.
3. Select the game version you want to play by entering the corresponding number (1-5).
4. Follow the on-screen instructions for the selected version.

```bash
python number_guessing_game.py
```

## Search Algorithms Used

1. **Binary Search**: An efficient search algorithm that repeatedly divides the search interval in half.
2. **Breadth-First Search (BFS)**: A search algorithm that explores all possible options level by level.
3. **Depth-First Search (DFS)**: A search algorithm that explores one branch of possibilities deeply before moving to the next.
4. **Simulated Annealing**: A probabilistic search algorithm that attempts to escape local optima by accepting worse solutions with a gradually decreasing probability.

## Future Improvements

- Implement more complex search algorithms such as Genetic Algorithms.
- Add a graphical interface for easier interaction.

---

This README file now includes details about the Binary Search AI version, along with a general overview of the project. Let me know if you'd like any further edits!
