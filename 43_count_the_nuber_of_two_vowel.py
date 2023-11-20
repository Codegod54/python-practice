# Program to Count the Number of Each Vowel

sentence = str(input("Enter a sentence:"))

sentence = sentence.casefold()

count = 0

for character in sentence:
#    print(character)
    if (character in "aeiou"):
        count +=1
print("The number of vowels are:",count)




    