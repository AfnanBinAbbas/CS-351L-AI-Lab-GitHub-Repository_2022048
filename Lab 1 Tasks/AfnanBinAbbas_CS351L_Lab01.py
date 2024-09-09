import random
from collections import deque

# Non-AI Version: Player vs Computer
def player_vs_computer():
    print("Player vs Computer")
    low, high = get_range()
    secret_number = random.randint(low, high)
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

# Get range from user
def get_range():
    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    return low, high

# BFS Version with user feedback
def bfs_guess():
    print("AI (BFS) guessing...")
    low, high = get_range()
    queue = deque([i for i in range(low, high + 1)])  # Initialize a queue with all possible guesses
    attempts = 0
    while queue:
        attempts += 1
        guess = queue.popleft()
        print(f"AI guesses: {guess}")
        feedback = input("Is the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"AI found the number in {attempts} attempts using BFS.")
            return attempts
        elif feedback == 'h':
            queue = deque([x for x in queue if x < guess])
        elif feedback == 'l':
            queue = deque([x for x in queue if x > guess])

# DFS Version with user feedback
def dfs_guess():
    print("AI (DFS) guessing...")
    low, high = get_range()
    stack = [i for i in range(low, high + 1)]  # Initialize a stack with all possible guesses
    attempts = 0
    while stack:
        attempts += 1
        guess = stack.pop()
        print(f"AI guesses: {guess}")
        feedback = input("Is the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"AI found the number in {attempts} attempts using DFS.")
            return attempts
        elif feedback == 'h':
            stack = [x for x in stack if x < guess]
        elif feedback == 'l':
            stack = [x for x in stack if x > guess]

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
            if random.uniform(0, 1) < temperature:
                current_guess = new_guess

# Main function to test the updated versions
if __name__ == "__main__":
    print("Choose an AI version to test:")
    print("1. BFS Guessing")
    print("2. DFS Guessing")
    print("3. Simulated Annealing")

    choice = input("Enter your choice (1-3): ").strip()

    secret_number = random.randint(1, 100)
    print(f"The secret number is: {secret_number}")

    if choice == '1':
        bfs_guess()
    elif choice == '2':
        dfs_guess()
    elif choice == '3':
        simulated_annealing_guess(secret_number)
    else:
        print("Invalid choice.")
