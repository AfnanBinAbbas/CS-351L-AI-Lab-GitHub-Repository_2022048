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
    while queue:
        guess = queue.popleft()
        print(f"\tAI guesses: {guess}")
        feedback = input("\tIs the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print("\tAI found the number using BFS.")
            return
        elif feedback == 'h':
            queue = deque([x for x in queue if x < guess])
        elif feedback == 'l':
            queue = deque([x for x in queue if x > guess])

# DFS Version with user feedback
def dfs_guess():
    print("\tAI (DFS) guessing...")
    low, high = get_range()
    stack = [i for i in range(low, high + 1)]  # Initialize a stack with all possible guesses
    while stack:
        guess = stack.pop()
        print(f"\tAI guesses: {guess}")
        feedback = input("\tIs the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print("\tAI found the number using DFS.")
            return
        elif feedback == 'h':
            stack = [x for x in stack if x < guess]
        elif feedback == 'l':
            stack = [x for x in stack if x > guess]

# Custom Algorithm: Simulated Annealing (renamed variables for clarity)
def simulated_annealing_guess(secret_number):
    print("\tAI (Simulated Annealing) guessing...")
    current_guess = random.randint(1, 100)
    exploration_level = 100  # Initial exploration level (formerly temperature)

    def get_neighbor(guess):
        # Get neighboring guess by moving within the range [-10, +10]
        return max(1, min(100, guess + random.randint(-10, 10)))

    while exploration_level > 0.1:  # Stop when exploration level is very low
        print(f"\tAI guesses: {current_guess}")
        
        if current_guess == secret_number:
            print("\tAI found the number using Simulated Annealing.")
            return
        
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

# AI Version: Binary Search (Computer guesses player's number)
def ai_number_guessing_game():
    # Player selects a number and AI guesses using binary search
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    low = 1
    high = 100

    # AI guesses until the number is found
    while low <= high:
        guess = (low + high) // 2  # AI uses binary search to guess

        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number!")
            return
        elif feedback == 'h':
            high = guess - 1  # If too high, reduce the upper bound
        elif feedback == 'l':
            low = guess + 1  # If too low, increase the lower bound

    print("Something went wrong!")

# Main function to test the updated versions
if __name__ == "__main__":
    print("\tChoose an AI version to test:")
    print("\t1. BFS Guessing")
    print("\t2. DFS Guessing")
    print("\t3. Simulated Annealing")
    print("\t4. Player vs Computer (Non-AI)")
    print("\t5. AI Binary Search (AI guesses your number)")

    choice = input("\n\tEnter your choice (1-5): ").strip()
    
    if choice == '1':
        bfs_guess()
    elif choice == '2':
        dfs_guess()
    elif choice == '3':
        secret_number = int(input("\n\tEnter secret number (1-100): "))
        simulated_annealing_guess(secret_number)
    elif choice == '4':
        player_vs_computer()
    elif choice == '5':
        ai_number_guessing_game()
    else:
        print("Invalid choice.")
