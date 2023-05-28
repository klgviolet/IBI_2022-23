# Initialize generation and rabbit count variables
generation = 1
rabbits = 2

# While rabbits are less than or equal to 100
while rabbits <= 100:
    # Calculate next generation rabbits count
    new_rabbit_pairs = rabbits // 2
    new_rabbits = new_rabbit_pairs * 2
    
    # Update total rabbits count
    rabbits += new_rabbits
    
    # Increment generation number
    generation += 1

# Print the generation number and total rabbits
print("Over 100 rabbits have been born in generation " + str(generation) + " with a total of " + str(rabbits) + " rabbits.")
