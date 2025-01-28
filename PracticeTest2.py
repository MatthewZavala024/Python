
###Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number

# def check(s):    
#     lower_valid = 0
#     upper_valid = 0
#     number_valid = 0
#     for i in s:
#         if i.islower():
#             lower_valid += 1
#         if i.isupper():
#             upper_valid += 1 
#         if i.isdigit():
#             number_valid += 1
#     if lower_valid > 0 and upper_valid > 0 and number_valid > 0:
#         print("Valid string")
#     else:
#         print("Not valid")



###Write a function to take in a list and find all the possible combinations from the three digits within the list. Function name is combo(li). 
# li = [1, 2, 3]

# def combo(li): 
#     for i in range(3): 
#         for j in range(3): 
#             for k in range(3): 
#                 if (i!=j and j!=k and i!=k): 
#                     print(li[i], li[j], li[k])





###Write a function that takes in a list that contains different data types and adds any that are strings to its own list.
###Print the new list that contains only those strings.

# li = [1, 2.0, 2 + 5j, True, 'string', (0, 1), {"Best_Class": 'Python', "Bool": 'True'}]

# string_list = []
# for item in li:
#     if type(item) == str:
#         string_list.append(item)
# print(string_list)




######Write a function to count the uppercase letters and lowercase characters. Name of function: count(string).
# string = "How many Uppercase Letters are in this String? How many Lowercase Letters are in this String?"
# def count(string):
#     lcount = 0
#     ucount = 0
#     for i in string:
#         if i.isupper():
#             ucount += 1
#         elif i.islower():
#             lcount += 1
#     print("Number of lowercase is:",  lcount)
#     print("Number of uppercase is:",  ucount)


###Write a script to convert a string to a list based off of periods. 
# string = "This is sentence one. This is sentence two. This is sentence three"
# def split_period(string):
#     string = string.split(".")







