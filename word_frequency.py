#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# 1. Prompt the user: Ask the user to enter a sentence. ✓
user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")

# 2. Split the sentence. ✓
words = user_sentence.split()

# 3. Create lists to store words and their corresponding frequencies. ✓
unique_words = []
frequencies = []

# 4. Iterate through words and update frequencies ✓
for word in words:
    # Removes punctuation and turns all words lowercase.
    word = word.strip(".,!?").lower()  
    # If the word is in unique_words, find all indexes of the word and add one to it's position in the frequencies list each time.
    if word in unique_words:
        index = unique_words.index(word)
        frequencies[index] += 1
    
    # If the word is not in unique_words, add it to the list and update frequency of word to 1.
    else:
        unique_words.append(word)
        frequencies.append(1)

# Print results.
print("\nWord frequencies:")

# For the number of words in unique_words / For the length of the list unique_words, print word with it's designate frequency.
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")