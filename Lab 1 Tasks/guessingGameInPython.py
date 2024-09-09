def interactive_dfs_guess(min_digit, max_digit, num_length):
    # Generate the list of numbers based on the range
    numbers = [str(i) for i in range(min_digit, max_digit + 1)]
    
    # Function to simulate DFS and interact with the user
    def dfs(guess, depth):
        if depth == num_length:
            # Ask user if this guess is correct
            print(f"Is your number {guess}? (yes/no)")
            response = input().lower()
            if response == "yes":
                print(f"Great! The AI guessed your number: {guess}")
                return True
            return False
        
        for num in numbers:
            if dfs(guess + num, depth + 1):
                return True
        return False
    
    # Start the DFS with an empty guess
    if not dfs("", 0):
        print("Couldn't guess the number.")

# Example usage
min_digit = 0  # Minimum digit (inclusive)
max_digit = 9  # Maximum digit (inclusive)
num_length = 3  # Length of the number to guess

interactive_dfs_guess(min_digit, max_digit, num_length)