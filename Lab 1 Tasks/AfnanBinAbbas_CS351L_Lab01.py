import random
from collections import deque

# Non-AI Version: Player vs Computer
def player_vs_computer():
    print("Player vs Computer")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break

# AI Version with Binary Search: Computer vs Player
def binary_search_guess(low, high, secret_number):
    print("AI (Binary Search) guessing...")
    attempts = 0
    while low <= high:
        attempts += 1
        guess = (low + high) // 2
        print(f"AI guesses: {guess}")
        if guess < secret_number:
            low = guess + 1
            print("Too low!")
        elif guess > secret_number:
            high = guess - 1
            print("Too high!")
        else:
            print(f"AI found the number in {attempts} attempts.")
            return attempts

# BFS Version
def bfs_guess(secret_number):
    print("AI (BFS) guessing...")
    queue = deque([i for i in range(1, 101)])  # Initialize a queue with all possible guesses
    attempts = 0
    while queue:
        attempts += 1
        guess = queue.popleft()
        print(f"AI guesses: {guess}")
        if guess == secret_number:
            print(f"AI found the number in {attempts} attempts using BFS.")
            return attempts

# DFS Version
def dfs_guess(secret_number):
    print("AI (DFS) guessing...")
    stack = [i for i in range(1, 101)]  # Initialize a stack with all possible guesses
    attempts = 0
    while stack:
        attempts += 1
        guess = stack.pop()
        print(f"AI guesses: {guess}")
        if guess == secret_number:
            print(f"AI found the number in {attempts} attempts using DFS.")
            return attempts

# Custom Algorithm: Simulated Annealing
def simulated_annealing_guess(secret_number):
    print("AI (Simulated Annealing) guessing...")
    current_guess = random.randint(1, 100)
    attempts = 0
    temperature = 100  # Initial temperature

    def get_neighbor(guess):
        return max(1, min(100, guess + random.randint(-10, 10)))  # Get neighboring guess

    while temperature > 1:
        attempts += 1
        print(f"AI guesses: {current_guess}")
        if current_guess == secret_number:
            print(f"AI found the number in {attempts} attempts using Simulated Annealing.")
            return attempts
        new_guess = get_neighbor(current_guess)
        temperature *= 0.95  # Decrease temperature
        if abs(new_guess - secret_number) < abs(current_guess - secret_number):
            current_guess = new_guess  # Accept better guess
        else:
            # Probabilistic acceptance of worse guess
            if random.uniform(0, 1) < temperature:
                current_guess = new_guess

# Main function to test all algorithms
if __name__ == "__main__":
    secret_number = random.randint(1, 100)
    print(f"The secret number is: {secret_number}")

    # Player vs Computer (Non-AI Version)
    # Pplayer vs Computer
    # player_vs_computer()

    # AI Version with Binary Search
    # binary_search_guess(1, 100, secret_number)

    # # BFS Version
    # bfs_guess(secret_number)

    # # DFS Version
    dfs_guess(secret_number)

    # # Custom Algorithm (Simulated Annealing)
    simulated_annealing_guess(secret_number)
