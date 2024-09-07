def dfs_recursive_number_guessing_game(target, low, high):
    # If the range is invalid, return None
    if low > high:
        print("The number is not in the range.")
        return None
    
    # Make the middle guess
    guess = (low + high) // 2
    print(f"AI guesses: {guess}")
    
    if guess == target:
        print("Correct! The number is", guess)
        return guess
    elif guess < target:
        # Target is higher, recursively explore the right half
        return dfs_recursive_number_guessing_game(target, guess + 1, high)
    else:
        # Target is lower, recursively explore the left half
        return dfs_recursive_number_guessing_game(target, low, guess - 1)

# Example usage:
target_number = 37
dfs_recursive_number_guessing_game(target_number, 1, 100)