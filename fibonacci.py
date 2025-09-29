#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file) ✓
# Initalize y to True to enter while loop.
y = True

# Prompt the user for the number of terms. ✓
while y == True:    
  numterms = input("Enter the Number of Terms Wanted for Fibonacci Sequence: ")
    
  # Validate that the input is a positive integer. ✓
  if numterms.isdigit() and int(numterms) > 0:
      # Safe to convert to integer and break.
      numterms = int(numterms)  
      y == False
      break
  else:
    print("Oh no! What you have entered is not a positive integer. Please try again.\n")

# Initialize variables for fibonacci sequence computation.
a, b = 0, 1

print(f"\nFibonacci Sequence for {numterms} terms: ")

# Use a for loop to print the Fibonacci sequence up to that many terms. ✓
for x in range(int(numterms)) :
  print(a, end=" ")
  a, b = b, a + b
