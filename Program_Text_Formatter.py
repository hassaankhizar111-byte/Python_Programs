# Step 1: Get input from user
sentence = input("Enter a sentence: ")

# Step 2: Split sentence into words
words = sentence.split()  # ['Python', 'is', 'amazing', 'for', 'coding']

# Step 3: Process each word
for i in range(len(words)):
    word = words[i]
    
    # Remove first and last character
    if len(word) > 2:  # to avoid empty words
        word = word[1:-1]
    else:
        word = ""  # if word length is 1 or 2
    
    # Reverse every second word (index 1,3,5...)
    if i % 2 == 1:
        word = word[::-1]
    
    words[i] = word

# Step 4: Join words back into a sentence
formatted_sentence = " ".join(words)

print("Formatted sentence:", formatted_sentence)
