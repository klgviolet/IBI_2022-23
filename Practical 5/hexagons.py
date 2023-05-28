# For each，the number on each side is equal to his number.
def number(n):
    return n * (2 * n - 1)
for n in range(1, 6):
    # Call the function to calculate the hexagonal number
    hexagonal_number = number(n)
    print("The #" + str(n) + " hexagonal number is: " + str(hexagonal_number))
