# 1) Swap two numbers without using a temporary variable:

# x = 10
# y = 5

# x = x + y
# y = x - y
# x = x - y

# print("after swapping x =",x ,"and y =",y)
# --------------------------------------------------------------------------------------------------------
# 2) write a program to print top two numbers in an array
# def Nmaxelements(list1, N): 
# 	final_list = [] 

# 	for i in range(0, N): 
# 		max1 = 0
		
# 		for j in range(len(list1)):	 
# 			if list1[j] > max1: 
# 				max1 = list1[j]; 
				
# 		list1.remove(max1); 
# 		final_list.append(max1) 
		
# 	print(final_list) 

# list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10] 
# N = 2
# Nmaxelements(list1, N)
# --------------------------------------------------------------------------------------------------------------
# 3) write a program to find sum of each digit in a given number in python 

# num = int(input("Enter a number: "))

# sum = 0

# while num > 0:
#     d = num%10
#     num = num//10
#     sum += d
    
# print("The sum of digits of number is",sum)
# ------------------------------------------------------------------------------------------------------------
# 4) How to remove an given element in an array using python
# x = ['mani', 'kumar']
# x.remove('kumar')
# print(x)
# ---------------------------------------------------------------------------------------------------------------
# 5) write a program for a factorial of a number in python
# def factorial(num):

#     if num == 1:
#         return num
#     else:
#         return num * factorial(num - 1)

# num = int(input("Enter a Number: "))

# if num < 0:
#     print("Factorial cannot be found for negative numbers")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     print("Factorial of", num, "is: ", factorial(num))
# -----------------------------------------------------------------------------------------------------------------
# 6) How to find the missing number in integer array 1 to 100
# def missing_numbers(num_list):
#       original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
#       num_list = set(num_list)
#       return (list(num_list ^ set(original_list)))

# print(missing_numbers([1,2,3,4,6,7,10]))
# ------------------------------------------------------------------------------------------------------------------
# 7) How to check if array contains a given number in python
 
# test_list = [ 1, 6, 3, 5, 3, 4 ] 

# print("Checking if 4 exists in list ( using  for loop ) : ") 

# for i in test_list: 
# 	if(i == 4) : 
# 		print ("Element Exists") 

# print("Checking if 4 exists in list ( using in ) : ") 

# if (4 in test_list): 
# 	print ("Element Exists") 
# -----------------------------------------------------------------------------------------------------------------------------
# 8) Write a program to findout characters in string how many times reapeated using python

# import collections
# str1 = 'manikumar'
# d = collections.defaultdict(int)
# for c in str1:
#     d[c] += 1

# for c in sorted(d, key=d.get, reverse=True):
#   if d[c] > 1:
#       print('%s %d' % (c, d[c]))
# --------------------------------------------------------------------------------------------------------------------------