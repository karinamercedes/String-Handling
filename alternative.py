# Write a program that reads in a string and makes each alternate character
# into an upper case character and each other alternate character a lower case character.
print("Welcome to the characters alteration program:")
sentence = "She sells seashells by the seashore"

#Empty string; is going to store my updated string
characters_alteration = ""

#Loop through the sentence
#I want upper and lower case alternately so I have to make every even index upper case and every other index lower case
for i in range(len(sentence)):
    if (i % 2) == 0:
        characters_alteration += sentence[i].upper()
    else:
        characters_alteration += sentence[i].lower()

#Output the "characters_alteration" sentence
print (characters_alteration)

#Now, try starting with the same string but making each alternative word lower and upper case.
# Tip: Using the split() and join() functions will help you here.

#A blank space and a new title between the two tasks to help readability
print("\nWelocome to the words alteration program:")

#Empty string; is going to store my updated string
words_alteration = ""

#Split the sentence into a list of smaller pieces.
#I'm not giving any value to it so it will automatically split the string using whitespace as the delimiter and create a list of the characters.
split_sentence = sentence.split()

#Loop through the split sentence
#I want lower and upper word alternately so I have to make every even index lower case and every other index upper case
for i in range(len(split_sentence)):
    if i % 2 == 0:
        split_sentence[i] = split_sentence[i].lower()
    else:
        split_sentence[i] = split_sentence[i].upper()

#Join the words back into a sentence
#I'm taking a list of strings(split_sentence) and joining them to create one string
#I specify that the character I want to use to join the list elements is just a blank space (" ")
words_alteration = " ".join(split_sentence)

#Output the "words_alteration" sentence
print(words_alteration)

# End-of-file (EOF)
