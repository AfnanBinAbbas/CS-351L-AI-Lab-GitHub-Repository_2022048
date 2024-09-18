import random
import os
import time
import sys
import heapq  # Importing heapq for the priority queue

# Function to create the game grid
def create_grid(size):
    return [[' ' for _ in range(size)] for _ in range(size)]  # Create an empty grid filled with spaces

# Function to place the snake and food on the grid
def place_snake_and_food(grid):
    snake = [(0, 0)]  # Starting position of the snake
    grid[0][0] = 'S'  # 'S' marks the starting point of the snake
    food_x, food_y = random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)
    
    # Ensure food is not placed on the snake
    while (food_x, food_y) in snake:
        food_x, food_y = random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)
    
    grid[food_x][food_y] = 'F'  # 'F' marks the food
    return snake, (food_x, food_y)

# Function to print the grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print('-' * (len(grid) * 4 + 1))  # Print top border line
    for row in grid:
        print('| ' + ' | '.join(row) + ' |')  # Print row with borders between cells
        print('-' * (len(grid) * 4 + 1))  # Print horizontal line after each row

# Function to check if the snake has collided with itself or the wall
def is_game_over(snake, grid_size):
    head_x, head_y = snake[0]
    return (head_x < 0 or head_x >= grid_size or
            head_y < 0 or head_y >= grid_size or
            (head_x, head_y) in snake[1:])  # Check for collision with itself

# Function to update the grid with the snake's position
def update_grid(grid, snake, food):
    for x, y in snake:
        grid[x][y] = 'S'  # Mark the snake's body
    food_x, food_y = food
    grid[food_x][food_y] = 'F'  # Mark the food

# Heuristic function for A* algorithm: calculates the Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm function to find the shortest path to the food
def a_star(snake, food, grid_size):
    start = snake[0]  # The head of the snake is the starting point
    goal = food

    # Priority queue to keep track of nodes to explore (using heapq)
    open_list = []
    heapq.heappush(open_list, (0, start))  # Add the start node with priority 0

    # Dictionaries to store the cost to reach each node and the path taken
    g_score = {start: 0}  # Cost from start to current node
    parent = {start: None}  # To reconstruct the path

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible directions: up, down, left, right

    while open_list:
        _, current = heapq.heappop(open_list)  # Get the node with the lowest f(n)

        # If we reach the goal (food), stop the search
        if current == goal:
            break

        # Explore neighboring positions (up, down, left, right)
        for direction in directions:
            next_x = current[0] + direction[0]  # Calculate next x-coordinate
            next_y = current[1] + direction[1]  # Calculate next y-coordinate
            next_state = (next_x, next_y)  # Form the next state (position)

            # Check if the next position is valid (not out of bounds and not itting the snake)
            if (0 <= next_x < grid_size and 0 <= next_y < grid_size and
                next_state not in snake):  # Valid position
                tentative_g_score = g_score[current] + 1  # Cost of moving to the next position

                # If the next state has not been explored or we found a cheaper path to it
                if next_state not in g_score or tentative_g_score < g_score[next_state]:
                    g_score[next_state] = tentative_g_score  # Update the cost to reach this state
                    f_score = tentative_g_score + heuristic(next_state, goal)  # Calculate the total cost f(n)
                    heapq.heappush(open_list, (f_score, next_state))  # Add the state to the open list
                    parent[next_state] = current  # Set the current state as the parent of the next state

    # Reconstruct the path from start to goal
    path = []
    current = goal  # Start from the goal (food) and work backwards
    while current is not None:
        path.append(current)  # Add current position to the path
        current = parent.get(current)  # Move to the parent of the current state
    path.reverse()  # Reverse the path to start from the beginning (start to goal)

    return path

# Main function to run the Snake Game
def snake_game():
    size = int(input("Enter the grid size (e.g., 6 for a 6x6 grid): "))
    grid = create_grid(size)
    snake, food = place_snake_and_food(grid)

    while True:
        print_grid(grid)
        print("Snake's head is at:", snake[0])
        print("Food is at:", food)

        # Use A* to find the path to the food
        path = a_star(snake, food, size)

        # Move the snake along the path
        if len(path) > 1:  # If there is a path to the food
            snake.insert(0, path[1])  # Move to the next position in the path
        else:
            print("No path to food found!")
            break

        # Check if the snake has eaten the food
        if snake[0] == food:
            # Place new food
            food_x, food_y = random.randint(0, size - 1), random.randint(0, size - 1)
            while (food_x, food_y) in snake:  # Ensure food is not placed on the snake
                food_x, food_y = random.randint(0, size - 1), random.randint(0, size - 1)
            food = (food_x, food_y)  # Update food position
        else:
            # Remove the tail of the snake
            snake.pop()

        # Update the grid
        grid = create_grid(size)  # Reset grid
        update_grid(grid, snake, food)  # Update grid with snake and food

        # Delay for a short period to control game speed
        time.sleep(0.2)

        # Check for game over
        if is_game_over(snake, size):
            print("Game Over! You collided with the wall or yourself.")
            break

# Run the game
snake_game()
