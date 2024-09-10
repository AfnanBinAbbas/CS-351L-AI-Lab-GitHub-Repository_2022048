import random
from collections import deque
import math

# ================================
# Non-AI Version: Player vs Computer
# ================================
# This function allows the player to guess a number chosen by the computer.
# The computer randomly selects a secret number within a user-defined range,
# and the player tries to guess it with feedback on whether their guess is too high or too low.
def player_vs_computer():
    print("\tPlayer vs Computer")
    
    # Get the range of numbers from the player
    low, high = get_range()
    
    # The computer selects a random number within the provided range
    secret_number = random.randint(low, high)
    attempts = 0
    
    # Player keeps guessing until they find the correct number
    while True:
        guess = int(input("\tEnter your guess: "))
        attempts += 1
        
        # Provide feedback based on the guess
        if guess < secret_number:
            print("\tToo low!")
        elif guess > secret_number:
            print("\tToo high!")
        else:
            # Correct guess
            print(f"\tCorrect! You guessed the number in {attempts} attempts.")
            break

# =======================
# Get range from user
# =======================
# This helper function asks the player for the lower and upper bounds of the guessing range.
def get_range():
    low = int(input("\tEnter the lower bound of the range: "))
    high = int(input("\tEnter the upper bound of the range: "))
    return low, high

# ================================
# BFS Version: AI Guessing
# ================================
# The AI uses the Breadth-First Search (BFS) algorithm to guess the number.
# The AI gets feedback after each guess and narrows down the possible guesses based on that.
def bfs_guess():
    print("\tAI (BFS) guessing...")
    
    # Get the range for the secret number
    low, high = get_range()
    
    # Initialize a queue with all possible guesses (BFS explores level by level)
    queue = deque([i for i in range(low, high + 1)])
    attempts = 0
    
    # AI guesses until it finds the correct number or runs out of guesses
    while queue:
        attempts += 1
        guess = queue.popleft()  # Guess the next number in the queue
        print(f"\tAI guesses: {guess}")
        
        # Get feedback from the user (player sets if guess is too high, low, or correct)
        feedback = input("\tIs the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            # AI guessed correctly
            print(f"\tAI found the number in {attempts} attempts using BFS.")
            return attempts
        elif feedback == 'h':
            # AI removes all guesses higher than the current guess
            queue = deque([x for x in queue if x < guess])
        elif feedback == 'l':
            # AI removes all guesses lower than the current guess
            queue = deque([x for x in queue if x > guess])
        
        # Optional: Limit to a certain number of attempts
        if attempts >= 10:
            print("\tSorry, out of tries! Better luck next time.")
            break

# ================================
# DFS Version: AI Guessing
# ================================
# The AI uses Depth-First Search (DFS) to guess the number.
# DFS guesses by going deeper into the possible guesses (stack-based approach).
def dfs_guess():
    print("\tAI (DFS) guessing...")
    
    # Get the range for the secret number
    low, high = get_range()
    
    # Initialize a stack with all possible guesses (DFS explores deeply first)
    stack = [i for i in range(low, high + 1)]
    attempts = 0
    
    # AI guesses until it finds the correct number or reaches the attempt limit
    while stack:
        attempts += 1
        guess = stack.pop()  # Guess the last number in the stack (LIFO)
        print(f"\tAI guesses: {guess}")
        
        # Get feedback from the user (player sets if guess is too high, low, or correct)
        feedback = input("\tIs the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            # AI guessed correctly
            print(f"\tAI found the number in {attempts} attempts using DFS.")
            return attempts
        elif feedback == 'h':
            # AI removes all guesses higher than the current guess
            stack = [x for x in stack if x < guess]
        elif feedback == 'l':
            # AI removes all guesses lower than the current guess
            stack = [x for x in stack if x > guess]

        # Optional: Limit to a certain number of attempts
        if attempts >= 10:
            print("\tSorry, out of tries! Better luck next time.")
            break

# ========================================
# Simulated Annealing: AI Guessing
# ========================================
# The AI uses Simulated Annealing to guess the number.
# This method introduces randomness (exploration_level) to allow the AI to explore better guesses and avoid local minima.
def simulated_annealing_guess(secret_number):
    print("\tAI (Simulated Annealing) guessing...")
    
    # Initial random guess
    current_guess = random.randint(1, 100)
    attempts = 0
    exploration_level = 100  # Initial exploration level (controls randomness)

    # Function to get a neighboring guess by shifting the current guess
    def get_neighbor(guess):
        return max(1, min(100, guess + random.randint(-10, 10)))

    # AI guesses while exploration level is significant
    while exploration_level > 0.1:
        attempts += 1
        print(f"\tAI guesses: {current_guess}")
        
        if current_guess == secret_number:
            # AI guessed correctly
            print(f"\tAI found the number in {attempts} attempts using Simulated Annealing.")
            return attempts
        
        # Get a neighboring guess
        new_guess = get_neighbor(current_guess)
        
        # Decrease exploration level gradually to reduce randomness
        exploration_level *= 0.95
        
        # Calculate the differences between the current/new guess and the secret number
        current_diff = abs(current_guess - secret_number)
        new_diff = abs(new_guess - secret_number)
        
        # Accept better guesses or sometimes worse guesses based on acceptance probability
        if new_diff < current_diff:
            current_guess = new_guess
        else:
            # Calculate acceptance probability for worse guesses
            acceptance_probability = math.exp((current_diff - new_diff) / exploration_level)
            if random.uniform(0, 1) < acceptance_probability:
                current_guess = new_guess

    print("\tAI did not find the exact number.")
    return attempts

# ================================
# Main Function to Test the Game
# ================================
# This function presents the user with a menu to select one of the AI versions or the player vs computer mode.
if __name__ == "__main__":
    print("\tChoose an AI version to test:")
    print("\t1. BFS Guessing")
    print("\t2. DFS Guessing")
    print("\t3. Simulated Annealing")
    print("\t4. Player vs Computer (Non-AI Version)")

    # Get the user's choice
    choice = input("\n\tEnter your choice (1-4): ").strip()
    
    # Execute the corresponding function based on the user's choice
    if choice == '1':
        bfs_guess()
    elif choice == '2':
        dfs_guess()
    elif choice == '3':
        # Simulated Annealing requires a secret number
        secret_number = int(input("\n\tEnter secret number (1-100): "))
        simulated_annealing_guess(secret_number)
    elif choice == '4':
        player_vs_computer()
    else:
        # Handle invalid choices
        print("Invalid choice.")
