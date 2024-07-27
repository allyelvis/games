import random

# Create a 5x5 grid
grid_size = 5
treasure_x = random.randint(0, grid_size - 1)
treasure_y = random.randint(0, grid_size - 1)

print("Welcome to the Treasure Hunt Game!")
print("You have to find the treasure hidden in the grid.")
print(f"The grid size is {grid_size}x{grid_size}.")

while True:
    x = int(input("Enter your guess for the X coordinate (0-4): "))
    y = int(input("Enter your guess for the Y coordinate (0-4): "))
    
    if x == treasure_x and y == treasure_y:
        print("Congratulations! You found the treasure!")
        break
    else:
        print("No treasure here, try again!")
