# Program to Illustrate Different Set Operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


union = set1 | set2
print("The union is: ", union)

intersection = set1 & set2
print("The intersection is: ", intersection)

difference_set1 = set1 - set2
difference_set2 = set2 - set1
print("The difference of set1 is: ", difference_set1)
print("The difference of set2 is: ", difference_set2)


all_difference = set1 ^ set2
print("The symentric difference is: ", all_difference)





