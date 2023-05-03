import random

# Read words from the local dictionary file
with open('words_alpha.txt') as f:
    words = f.readlines()
words = [word.strip() for word in words]

# Filter the words by length and select random ones
seven_letter_words = [word for word in words if len(word) == 7]
random_seven_letter_words = random.sample(seven_letter_words, 4)

# Print the random words
for word in random_seven_letter_words:
    print(word)


