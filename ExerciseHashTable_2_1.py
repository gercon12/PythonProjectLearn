# Open the file "poem.txt" in read mode
with open("poem.txt", "r") as f:
    # Loop through each line in the file
    for line in f:
        print(line)  # Print the current line to the console (just for viewing)

# Create an empty dictionary to store word counts
word_count = {}

# Open the file "poem.txt" again in read mode
with open("poem.txt", "r") as f:
    # Loop through each line in the file
    for line in f:
        # Split the line into individual words (tokens) separated by spaces
        tokens = line.split(' ')
        # Loop through each word in the current line
        for token in tokens:
            # Remove any newline character '\n' from the word
            token = token.replace('\n', '')
            # If the word already exists in the dictionary, increase its count by 1
            if token in word_count:
                word_count[token] += 1
            # Otherwise, add the word to the dictionary with a count of 1
            else:
                word_count[token] = 1
print(word_count)