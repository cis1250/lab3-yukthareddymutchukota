#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file) ✓
# Prompt the user for the number of terms. ✓
numterms = int(input("Enter the Number of Terms Wanted for Fibonacci Sequence: "))

# Validate that the input is a positive integer. ✓
while numterms <= 0 :
  int(input(f"Oh no! The number you have entered is not a positive integer. Please try again. \nEnter the Number of Terms Wanted for Fibonacci Sequence: "))

# Initialize variables for fibonacci sequence computation.
a, b = 0, 1

print(f"\nFibonacci Sequence for {numterms} terms: ")

# Use a for loop to print the Fibonacci sequence up to that many terms. ✓
for x in range(numterms) :
  print(a, end=" ")
  a, b = b, a + b
