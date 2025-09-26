# Lab 3 

# Part 1: Fibonacci Sequence

## Objective
Create a Python program that calculates and prints the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) up to a specified number of terms. 

---

## Requirements
1. **Prompt the user**  
   - Use the `input()` function to ask the user how many terms of the Fibonacci sequence they want.  

2. **Validate input**  
   - Ensure the user enters a **positive integer**.  
   - If the input is invalid, display an error message and prompt again.  

3. **Calculate and print**  
   - Use a **for loop** to generate and print the Fibonacci sequence up to the specified number of terms.

---


## Example Runs

```text
User input: “5”
Expected output: 0 1 1 2 3

User input: "cis1250"
Expected output: "Please enter a positive integer."
```

# Part 2: Word Frequency

## Objective
Write a Python program that takes a sentence as input and calculates the frequency of each word in the sentence using lists.

---

## Requirements
1. **Prompt the user**
   - Use the `input()` function to ask the user to enter a sentence. (Note that in the word_frequency.py file a function is provided to check if the input is a sentence. A sentence starts with a capital letter, contains at least one word and ends with a punctuation mark (period, question mark, exclamation mark).)
  
2. **Split the sentence into words**
   - Split the input sentence into a list of words using the [split()](https://docs.python.org/3/library/stdtypes.html#str.split) method.
  
3. **Create lists**
   - Create two empty lists to store words and their corresponding frequencies.
  
4. **Iterate through words and update frequencies**
   - Iterate through the list of words.
   - Check for existence: Check if the word is already in the list of words.
   - Update frequency: If the word exists, update its frequency in the corresponding list. Otherwise, append both the word and a frequency of 1 to the lists.
  
5. **Print results**
   - Print the word frequencies in a readable format.

## Example Runs

```text
Input: "To be or not to be, that is the question."
Output:
to: 2
be: 2
or: 1
not: 1
that: 1
is: 1
the: 1
question: 1

 
