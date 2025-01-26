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
# li = []
# for i in range(3,5000):
#     if (i % 5 == 0 or i % 7 == 0) and i % 35 != 0:
#         li.append(i)
# print(sum(li))



###Write a script that if the string below equals "test" then print "The string is test" else print "The string is not test". DO NOT PUT FUNCTION CALL IN ANSWER. 
# string = "test"
# def s(string):
#     if (string == "test"):
#         print("The string is test")
#     else:
#         print("The string is not test")




###Write a script that if the string below equals "test" then print "The string is test" else print "The string is not test". DO NOT PUT FUNCTION CALL IN ANSWER. 
# for i in range(1, 30, 3):
#    print(i, end=" ")




###Write a code snippet that will continue to the next iteration of a loop if an even number is selected in a loop.  If the number is 5, pass. If the number reaches 15, break. If the number selected is a duplicate remove it from the list. DO NOT PUT FUNCTION CALL IN ANSWER. USE RETURN
# li = [26, 2, 3, 4, 5, 6, 7, 8, 10, 5, 11, 13, 14, 15, 20, 16, 17, 18, 25, 1 ]
# def flowStatement(li):
#     myList = []
#     for i in li:
#         if i == 5:
#             pass
#         elif i % 2 == 0:
#             continue
#         elif i == 15:
#             break
#         else:
#             myList.append(i)
#     return(myList)




###Write a script using a while loop to print out the numbers through 100 on one line.
# counter = 0
# while counter < 100:
#    print(counter, end=" ")




###Write a script to sort the dictionary based on values from below.
# names = {"name1": "Smith", "name2": "Jones", "name3": "Anderson"}
# values_list = sorted(names.values())
# print(values_list)



###From the dictionary below, write a script to get the value for key n2
# nums = {"n1": 1, "n2": 2, "n3": 3}
# print(nums.get("n2"))



###Write a function to print out the key and the values from the below dictionary. DO NOT PUT FUNCTION CALL IN ANSWER!
# def d(nums):
#     for k, v in nums.items():
#         print(f"key: {k}, value: {v}")




###Write a script to pop the number 2 from the list below.
# li = [0,1,2,3,4,5,6,7,8,9,10]
# li.pop(2)



###Write a script to iterate through a range from 25 to 1000000 and append it to a list. Then find the difference between the max and min value of the list. 
# my_list = list()
# for i in range(25, 1000000):
#      my_list.append(i)



###Bill was tasked to split based on username and domain name. Finish the script to accomplish that.
#Not Done yet





###Write a script to sort the list below
# li = [10, 12, 52, 2, 3, 65, 20]
# li.sort()




###Write a script to reverse the list below. Take a look at Insert! DO NOT WRITE FUNCTION CALL IN ANSWER.
# def rev(list):
#     reverse_list = []
#     for i in list:
#         reverse_list.insert(0, i)
#     print(reverse_list)




###Use Python3's built in sorted() method.
###Take the dictionary below named dict1 and sort it based on the keys.
###Concatenate the dictionary's values in the order of the sorted dictionary's keys. 
###The flag is the values without the "x's".
# dict1 = {"xxlx":"xx!xx", "xfx":"ExLx", "0":'xSx',"www.":"SxQxUxIxRxRx","python.org":'xRxExT',"pickle rick":'ExC'}
# x=sorted(list(dict1.items()))
# cat_key=''
# for i in x:
#     cat_key+=i[1]
# print(cat_key.replace('x',''))




###Suppose there is a file named text.txt, how would you open the file in append mode? 
# file = open("text.txt", "a")



###Write a script to open a file named info.txt in append mode. Write to the string "Python is fun" to the file. Use with.
###Only write to the file. Do not print anything.
# with open("info.txt", "a") as data_obj:
#     data_obj.write("Python is fun")



###Write a function to take the list parsed in as argument. Use the provided list to create an odd and even list from the original list. Print them using separate print statements. An example list that will be passed into the function is below. 
# num = [1,2,3,4,5,6,7,8,9,10]
# def func(num):
#     even_li = []
#     odd_li = []
#     for i in num:
#         if i % 2 == 0:
#             even_li.append(i)
#         else:
#             odd_li.append(i)
#     print(even_li)
#     print(odd_li)