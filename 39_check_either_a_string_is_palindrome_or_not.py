# check either a number is palindrome or not

word = str(input("Enter a string:"))

reverseword = word[:: -1]
print(reverseword)
if reverseword == word:
    print("The string is palindrome", word)
else:
    print("The string is not palindrome", word)
