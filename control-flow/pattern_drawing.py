# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in each column
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after finishing a row
    print()
    
    # Increase the row counter
    row += 1
