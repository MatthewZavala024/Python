###Write code that will print a string of the decimal value and the hex value of the binary value provided. Function name: Do not put function call in answer.
# value='110010' 
# base_10=int(value,2)
# print(f'Base 10: {base_10} \nHex: {hex(base_10)}')
# print(base_10)




###Write Python code that will find the first instance of the user name "root" in a string. DO NOT PUT FUNCTION CALL IN ANSWER.
###def find_string(string):
###Example input:
# string='find the root in the sentence; not the second root'
# print(string.find('root'))



###Write python code that will remove every other character in a string. DO NOT PUT FUNCTION CALL IN ANSWER. 
# string = "This is a string"
# print(string[::2])



###Write a Python script to create HTML tags around the word. Use string formatting. DO NOT PUT FUNCTION CALL IN ANSWER.
# word = "python"
# element = "i"
# print(f"<{element}>{word}</{element}>")




###Write a function to format the string with the variables below. DO NOT PUT FUNCTION CALL IN ANSWER.
# word = "python"
# element = "i"
# print(f"<{element}>{word}</{element}>")




###Write a function to reverse a string and to reverse the words within the string. Function name: reverse(string):. DO NOT PUT FUNCTION CALL IN ANSWER.
# reverse(string = "Reverse this string")
# li = []
# word_list = string.split()
# for i in word_list[::-1]:
#     li.append(i)

# print(" ".join(li))
# print(string[::-1])




###Write a Python function to swap commas and dots in a string. The function should be called swap(num). DO NOT WRITE THE FUNCTION CALL IN ANSWER. 
# print(num.replace(".",",").replace(",",".").replace(".",",", 1))





###Write a Python function to swap cases in a given string. The function should be named swap_case(string). DO NOT WRITE FUNCTION CALL IN ANSWER. 
# string = "Python Is Cool"
# print(string.swapcase())



###Given a list of values, Write a python function that sums up the values in a list and prints the output. 
###The function should be named list_sum(myList). DO NOT PUT FUNCTION CALL IN ANSWER!
# myList = [1,2,3,4,5]
# myList = sum(myList)
# print(myList)




###Write a Python function to count the elements from a list of items
# def char_count(MyList):
#     for i in MyList:
#         print(len(str(i)))




###Write a function that takes a list of integers and concatenates the list into one number. Name of function: concat_list(myList).
# myList = [1, 2, 3, 4, 5]
# def concat_list(myList):
#     for i in myList:




###Write a function that takes a list of integers and counts the frequency of each of them. Function name: frequency_counter(myList).
# myList = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# import collections
# def frequency_counter(myList):
#     ctr = collections.Counter(myList)
#     print(ctr) 






###Write a function to construct the following pattern, using a nested for loop. 
###Name of function: startNo. n is the number of starts for the pattern. DO NOT PUT FUNCTION CALL IN ANSWER.
# def star(n):
#     for i in range(n):
#         for j in range(i):
#             print('* ', end="")
#         print('')
#     for i in range(n, 0, -1):
#         for j in range(i):
#             print('* ', end="")
#         print('')





###Write a Python function that iterates the integers num = 20. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
###For numbers that are multiples of three and five, print "FizzBuzz". Function name is fizzbizz(num). DO NOT PUT FUNCTION CALL IN ANSWER. 
# def fizzbizz(num):
#     for i in range(num):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#             continue
#         elif i % 3 == 0:
#             print("Fizz")
#             continue
#         elif i % 5 == 0:
#             print("Buzz")
#             continue
#         print(i)







##Write a Python function to check whether an alphabet is a vowel or consonant. Name of function is word(). DO NOT PUT FUNCTION CALL IN ANSWER. 
# Enter a letter: L
# def word(letter):
#     if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
#         print(f"{letter} is a vowel.") 
#     else:
#         print(f"{letter} is a consonant.")




###Write a function to find the median of three values. Function name med_num(num1, num2, num3). DO NOT PUT FUNCTION CALL IN ANSWER. 
# def med_num(num_1, num_2, num_3):
#     if num_1 > num_2:
#         if num_1 < num_3:
#             median = num_1
#         elif num_2 > num_3:
#             median = num_2
#         else:
#             median = num_3
#     else:
#         if num_1 > num_3:
#             median = num_1
#         elif num_2 < num_3:
#             median = num_2
#         else:
#             median = num_3
#     print("The median is", median)





###Write a function to construct the following pattern, using a nested loop number. Name of function: nums().
# def nums(num):
#     for i in range(num + 1):
#         print(str(i) * i)




###Write a function to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
###Function name: squared(num). DO NOT INCLUDE FUNCTION CALL IN ANSWER.
# squared(n = 5) :
# def squared(num):
#     di = dict()
#     for i in range(1, num + 1):
#         di[i] = i * i
#     print(di)




###Write a Python function to concatenate the following dictionaries to create a new one. Function name: con(dic1, dic2, dic3). DO NOT PUT FUNCTION CALL IN ANSWER
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# def con(dic1, dic2, dic3):
#     dic4 = {}

#     for d in (dic1, dic2, dic3):
#         dic4.update(d)
#     print(dic4)





###Write a Python function to print the keys and values as seen below. Function name: key_value(di). DO NOT PUT FUNCTION CALL IN ANSWER.
# def key_value(di):
#     for k, v in di.items():
#         print(k, v)



###Write a Python function to sort a dictionary by value. Return a list. Function name: s(di). DO NOT PUT FUNCTION CALL IN ANSWER. 
# di = {5: 1, 4: 3, 2: 2, 6: 9, 3: 4}
# def s(di):
#     return sorted(di.values())




###Write a function to find the largest of three numbers. Function name: myFunc(num1, num2, num3). DO NOT PUT FUNCTION CALL IN ANSWER.
# myFunc(10, 20, 30)
# def myFunc(num1, num2, num3):
#     greatestNum = 0
#     #find max of two
#     if num1 < num2:
#         greatestNum = num2
#         if num2 < num3:
#             greatestNum = num3
#         else:
#             greatestNum = num2
#     #find max of two
#     elif num1 > num2:
#         greatestNum = num1
#         if num1 > num3:
#             greatestNum = num1
#         else:
#             greatestNum = num3
#     print(f"{greatestNum}")