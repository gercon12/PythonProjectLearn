import string  # Import the 'string' module to access string-related constants like punctuation

# ---------- FIRST VERSION: index as key (includes all words, even duplicates) ----------

poem = {}  # Create an empty dictionary to store words with their position as key

# Open the text file in read mode with UTF-8 encoding
with open('poem.txt', 'r', encoding="utf-8") as file:
    words = file.read().split()  # Read the entire file and split it into individual words

    # Loop through each word along with its index
    for i, word in enumerate(words):
        # Remove punctuation from the word and convert it to lowercase
        clean_word = word.strip(string.punctuation).lower()
        # If the cleaned word is not empty
        if clean_word:
            # Store the word in the dictionary with its index as the key
            poem[i] = clean_word

# Print the resulting dictionary
print(poem)
# Print the total number of words stored (same as total number of words in the text)
print(len(poem))

print("-------------------------------------------------------------")

# ---------- SECOND VERSION: word as key (only unique words, numbered in order of first appearance) ----------

poem = {}  # Create a new empty dictionary
cont = 0   # Counter to assign incremental numbers to unique words

# Open the text file again
with open('poem.txt', 'r', encoding="utf-8") as file:
    words = file.read().split()  # Split the text into words again

    # Loop through each word
    for word in words:
        # Remove punctuation from the word (case is preserved)
        clean_word = word.strip(string.punctuation)
        # If the word has not been seen before
        if clean_word not in poem:
            # Store it in the dictionary with the current counter value
            poem[clean_word] = cont
            # Increase the counter for the next new word
            cont += 1

# Print the resulting dictionary of unique words
print(poem)
# Print the total number of unique words
print(len(poem))




