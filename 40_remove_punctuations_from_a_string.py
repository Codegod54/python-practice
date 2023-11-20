# Program to Remove Punctuations From a String
sentence = str(input("Enter a sentence:"))
filter_comma = sentence.replace(",", "")
filter_fullstop = filter_comma.replace(".", "")
filter_questionmark = filter_fullstop.replace("?", "")
filter_exclamation = filter_questionmark.replace("!", "")
filter_semicolon = filter_exclamation.replace(";", "")
print(filter_semicolon)
