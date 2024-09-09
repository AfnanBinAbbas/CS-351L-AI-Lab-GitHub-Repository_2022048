def interactive_dfs_guess():
    # Take input for range and length from the user
    min_digit = int(input("Enter the minimum digit (inclusive): "))
    max_digit = int(input("Enter the maximum digit (inclusive): "))
    num_length = int(input("Enter the length of the number to guess: "))
    
    # Generate the list of numbers based on the range
    numbers = [str(i) for i in range(min_digit, max_digit + 1)]
    
    attempts = [0]  # We use a list so the variable is mutable inside the recursive function
    
    # DFS function to explore combinations and interact with the user
    def dfs(guess, depth):
        # Increment the attempts counter for each guess
        attempts[0] += 1
        
        # Print the current path/guess being explored
        print(f"DFS exploring path: {guess} (Attempt #{attempts[0]})")
        
        if depth == num_length:
            # Ask user if this guess is correct
            print(f"Is your number {guess}? (yes/no)")
            response = input().lower()
            if response == "yes":
                print(f"Great! The AI guessed your number: {guess} in {attempts[0]} attempts.")
                return True
            return False
        
        # Try each number and go deeper
        for num in numbers:
            if dfs(guess + num, depth + 1):  # Recursive call to go deeper
                return True
        return False
    
    # Start the DFS with an empty guess
    if not dfs("", 0):
        print(f"Couldn't guess the number after {attempts[0]} attempts.")

# Start the guessing game
interactive_dfs_guess()
