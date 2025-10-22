# Naomi Puyleart
# 10/22/25
# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all the words are run together,
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    sep_sentence = ""
    #    Add your logic here
    sep_sentence = sep_sentence + sentence[0]

    for i in range(1, len(sentence)):
        char = sentence[i]
        if char.isupper():
            char = char.lower()
            sep_sentence = sep_sentence + " "

        sep_sentence = sep_sentence + char

    return sep_sentence.strip()

# Example usage

cap_sentence = input('Enter a string: ')

new_sentence = word_separator(cap_sentence)

print(new_sentence)