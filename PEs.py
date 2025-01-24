###Write python script that will remove all white space from a string.
###Then replace each instance of "x" with an "a" and each instance of "^" with an "s". 
###Use your code on the string below to receive the flag for this challenge. 
###s = '       ^mxrtypxnt^\n\r'
# s = '       ^mxrtypxnt^\n\r'
# format = s.strip()
# print(format.replace("x", "a").replace("^","s"))



###Write a script to print out "Follow The White Rabbit Neo......Wake Up"
# neo = 'FoLLow THE whiTe RabbIT NEO......WaKe uP'
# print(neo.title())


###Write a script will print out "the matrix has you. you need to get out!!!!"
# neo = "The MATRIX has you. YOU NEed to GET out!!!!"
# print(neo.lower())


###Using format string and the variables below.
###Output:
###John is 50 years old.
###name = "John"
###age = 50
# name = "John"
# age = 50
# print(f"{name} is {age} years old.")




###Write a python script to get the "w" from the string below.
###string = "Howdy"
# string = "Howdy"
# print(string[2:3])



###Write a python script to reverse the string. 
###string = "Howdy"
# string = "Howdy"
# print(string[::-1])



###Write python code that will remove every other character in a string.
###string = "This is a string."
# string = "This is a string."
# print(string[:17:2])



###Write a script to uppercase the string.
###string = "hello"
# string = "hello"
# print(string.upper())



###Write Python code that will replace "sad" with "fun".
# string = "Python is sad!"
# print(string.replace("sad", "fun"))



###What is the index position of fun in the string below.
###string = "Python is a fun class!"
# string = "Python is a fun class!"
# print(string.index("fun"))



##Use the .format() to format the string to put x in the string.
### x = 100.0
# print(f"Python is {x}% the best programming language")



###Please slice the string to get "It is all around us." from the string below.
###string = "The Matrix is everywhere. It is all around us. Even now in this very room."
# string = "The Matrix is everywhere. It is all around us. Even now in this very room."
# print(string[26:46])



###Write the script to get rid of the whitespace from the string below.
###string = "\t\tGet rid of this tab"
# string = "\t\tGet rid of this tab"
# print(string.strip())



###Based on the variable below, write a script to round the number 3 decimal places. 
###x = 10.23654785
# x = 10.23654785
# print(f"{x:.3f}")



###Write a for loop to enumerate through the list and start at 0 below:
# li = [1,2,3,4,5]
# for i in enumerate(li):
#     print(i)



###Write a script to iterate through a range of 0 to 100000. If the number is divisible by 2, continue. else add the number to a count and print out the count. 
# count = 0
# for i in range(0,1000000):
#     if i % 2 == 0:
#         continue
#     else:
#         count += i
# print(count)




###Write a python script that finds all the numbers between 3(inclusive) and 5000(exclusive) that are evenly divisible by 5 or evenly divisible by 7 but not evenly divisible by 35.
li = []

for i in range(3,5000):
    if (i % 5 == 0 or i % 7 == 0) and i % 35 != 0:
        li.append(i)
print(sum(li))