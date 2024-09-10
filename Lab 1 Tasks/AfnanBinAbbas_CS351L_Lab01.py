import random
from collections import deque
import math

# Non-AI Version: Player vs Computer
def player_vs_computer():
    print("\tPlayer vs Computer")
    low, high = get_range()
    secret_number = random.randint(low, high)
    attempts = 0
    while True:
        guess = int(input("\tEnter your guess: "))
        attempts += 1
        if guess < secret_number:
            print("\tToo low!")
        elif guess > secret_number:
            print("\tToo high!")
        else:
            print(f"\tCorrect! You guessed the number in {attempts} attempts.")
            break

# Get range from user
def get_range():
    low = int(input("\tEnter the lower bound of the range: "))
    high = int(input("\tEnter the upper bound of the range: "))
    return low, high

# BFS Version with user feedback
def bfs_guess():
    print("\tAI (BFS) guessing...")
    low, high = get_range()
    queue = deque([i for i in range(low, high + 1)])  # Initialize a queue with all possible guesses
    attempts = 0
    while queue:
        attempts += 1
        guess = queue.popleft()
        print(f"\tAI guesses: {guess}")
        feedback = input("\tIs the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"\tAI found the number in {attempts} attempts using BFS.")
            return attempts
        elif feedback == 'h':
            queue = deque([x for x in queue if x < guess])
        elif feedback == 'l':
            queue = deque([x for x in queue if x > guess])
        if attempts >= 10:
            print("\tSorry, out of tries! Better luck next time.")
            break

# DFS Version with user feedback
def dfs_guess():
    print("\tAI (DFS) guessing...")
    low, high = get_range()
    stack = [i for i in range(low, high + 1)]  # Initialize a stack with all possible guesses
    attempts = 0
    while stack:
        attempts += 1
        guess = stack.pop()
        print(f"\tAI guesses: {guess}")
        feedback = input("\tIs the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"\tAI found the number in {attempts} attempts using DFS.")
            return attempts
        elif feedback == 'h':
            stack = [x for x in stack if x < guess]
        elif feedback == 'l':
            stack = [x for x in stack if x > guess]
        if attempts >= 10:
            print("\tSorry, out of tries! Better luck next time.")
            break

# Custom Algorithm: Simulated Annealing (renamed variables for clarity)
def simulated_annealing_guess(secret_number):
    print("\tAI (Simulated Annealing) guessing...")
    current_guess = random.randint(1, 100)
    attempts = 0
    exploration_level = 100  # Initial exploration level (formerly temperature)

    def get_neighbor(guess):
        # Get neighboring guess by moving within the range [-10, +10]
        return max(1, min(100, guess + random.randint(-10, 10)))

    while exploration_level > 0.1:  # Stop when exploration level is very low
        attempts += 1
        print(f"\tAI guesses: {current_guess}")
        
        if current_guess == secret_number:
            print(f"\tAI found the number in {attempts} attempts using Simulated Annealing.")
            return attempts
        
        new_guess = get_neighbor(current_guess)
        exploration_level *= 0.95  # Decrease exploration level

        # Acceptance probability
        current_diff = abs(current_guess - secret_number)
        new_diff = abs(new_guess - secret_number)
        
        if new_diff < current_diff:
            current_guess = new_guess  # Accept better guess
        else:
            acceptance_probability = math.exp((current_diff - new_diff) / exploration_level)
            if random.uniform(0, 1) < acceptance_probability:
                current_guess = new_guess

    print("\tAI did not find the exact number.")
    return attempts

# Main function to test the updated versions
if __name__ == "__main__":
    print("\tChoose an AI version to test:")
    print("\t1. BFS Guessing")
    print("\t2. DFS Guessing")
    print("\t3. Simulated Annealing")
    print("\t4. Player vs Comp (Non AI-ver.)")

    choice = input("\n\tEnter your choice (1-4): ").strip()
    
    if choice == '1':
        bfs_guess()
    elif choice == '2':
        dfs_guess()
    elif choice == '3':
        secret_number = int(input("\n\tEnter secret number (1-100): "))
        simulated_annealing_guess(secret_number)
    elif choice == '4':
        player_vs_computer()
    else:
        print("Invalid choice.")
