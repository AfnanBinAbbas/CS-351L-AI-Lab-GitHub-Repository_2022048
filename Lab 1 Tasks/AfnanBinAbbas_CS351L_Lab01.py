import random
from collections import deque

# Non-AI Version: Player vs Computer
def player_vs_computer():
    print("\t Player vs Computer")
    low, high = get_range()
    secret_number = random.randint(low, high)
    attempts = 0
    while True:
        guess = int(input("\t Enter your guess: "))
        attempts += 1
        if guess < secret_number:
            print("\t Too low!")
        elif guess > secret_number:
            print("\t Too high!")
        else:
            print(f"\t Correct! You guessed the number in {attempts} attempts.")
            break

# Get range from user
def get_range():
    low = int(input("\t Enter the lower bound of the range: "))
    high = int(input("\t Enter the upper bound of the range: "))
    return low, high

# BFS Version with user feedback
def bfs_guess():
    print("\t AI (BFS) guessing...")
    low, high = get_range()
    queue = deque([i for i in range(low, high + 1)])  # Initialize a queue with all possible guesses
    attempts = 0
    while queue:
        attempts += 1
        guess = queue.popleft()
        print(f"\t AI guesses: {guess}")
        feedback = input("\t Is the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"\t AI found the number in {attempts} attempts using BFS.")
            return attempts
        elif feedback == 'h':
            queue = deque([x for x in queue if x < guess])
        elif feedback == 'l':
            queue = deque([x for x in queue if x > guess])

# DFS Version with user feedback
def dfs_guess():
    print("\t AI (DFS) guessing...")
    low, high = get_range()
    stack = [i for i in range(low, high + 1)]  # Initialize a stack with all possible guesses
    attempts = 0
    while stack and attempts<=10 :
        attempts += 1
        guess = stack.pop()
        print(f"\t AI guesses: {guess}")
        feedback = input("\t Is the guess too (h)igh, too (l)ow, or (c)orrect? ").lower()
        if attempts<=10 :
            if feedback == 'c':
                print(f"\t AI found the number in {attempts} attempts using DFS.")
                return attempts
            elif feedback == 'h':
                stack = [x for x in stack if x < guess]
            elif feedback == 'l':
                stack = [x for x in stack if x > guess]
        else :
            print('\t Sorry out of tries! Better luck next time..')
                
# Custom Algorithm: Simulated Annealing
def simulated_annealing_guess(secret_number):
    print("\t AI (Simulated Annealing) guessing...")
    current_guess = random.randint(1, 100)
    attempts = 0
    temperature = 100  # Initial temperature

    def get_neighbor(guess):
        return max(1, min(100, guess + random.randint(-10, 10)))  # Get neighboring guess

    while temperature > 1:
        attempts += 1
        print(f"\t AI guesses: {current_guess}")
        if current_guess == secret_number:
            print(f"\t AI found the number in {attempts} attempts using Simulated Annealing.")
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
    # get_range()
    # secret_number = random.randint(low, high)
    
    print("\t Choose an AI version to test:")
    print("\t 1. BFS Guessing")
    print("\t 2. DFS Guessing")
    print("\t 3. Simulated Annealing")
    print("\t 4. Player vs Comp (Non AI-ver.)")

    choice = input("\n\t Enter your choice (1-4): ").strip()
    
    if choice == '1':
        secret_number =  int(input("\n\t Enter secret number: "))
        print(f"\t The secret number is: {secret_number}")
        bfs_guess()
    elif choice == '2':
        secret_number =  int(input("\n\t Enter secret number: "))
        print(f"\t The secret number is: {secret_number}")
        dfs_guess()
    elif choice == '3':
        secret_number =  int(input("\n\t Enter secret number: "))
        print(f"\t The secret number is: {secret_number}")
        simulated_annealing_guess(secret_number)
    elif choice == '4':
        player_vs_computer()
    # elif choice == '5':
    else:
        print("Invalid choice.")
