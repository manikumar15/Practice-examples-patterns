# convert the uppercase to lowercase and lowercase to uppercase by using swapcase method.
# string="kumar"
# print(string.swapcase())

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# list=[1,3,4,5,67,8,9]
# list.insert(9,"manikumar")
# print(list)

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# list=[1,2,3,4,5,6,7]
# list.extend([8,9,10])
# print(list)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# list=[1,2,3,4,5,6,7]
# list.append(8)
# print(list)
# -----------------------------------------------------------------------------------------------------------------------------------------------
# string='python developer'
# s=string.replace('python','oracle')
# print(s)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# string="manikumar"
# s=''.join(reversed(string))
# print(s)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# s=[1,3,5,7,9,2,4,6,8]
# s.sort()
# print(s)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# s=[1,2,2]
# i=sum(s)
# print(i)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# import re
# s='+91-1234 +91-9573762293 +91-9573762283'
# v=re.findall('\+\w{2}-\w{10}',s)
# for i in v:
# 	print(i)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

# import time;
# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

# for i in range(10):
# 	print(i)
# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# a=60
# b=20
# c=30

# if (a >= b ) and (a >= c):
# 	largest=a
# elif (b >= a ) and (b >= c):
# 	largest=b
# else:
# 	largest=c

# print("largest number is:",a,b, "and" ,c, "is :","",largest)
# ----------------------------------------------------------------------------------------------------------
# string=input("enter a string:")
# length=len(string)
# print(length)
# for row in range(length):
# 	for col in range(row+1):
# 		print(string[col],end=" ")
# 	print()


# output:
# Enter a string:python
# length of string is : 6
# p
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n
# ----------------------------------------------------------------------------------------------------------------------------#

# num=int(input("enter a number:"))
# for i in range(num):
# 	print("* "*num)
# output:
# enter a number:10
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# ------------------------------------------------------------------------------------------------------------------------------#
# num=int(input("enter a number:"))
# for i in range(num):
# 	print("* "*i)
# output:
# enter a number:10
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *
# ---------------------------------------------------------------------------------------------------------------------------------#
# num=int(input("enter a number:"))
# for i in range(1,num+1):
# 	print(" "*(num-i)+"*  "*i)

# output:
# enter a number:10

#          *
#         *  *
#        *  *  *
#       *  *  *  *
#      *  *  *  *  *
#     *  *  *  *  *  *
#    *  *  *  *  *  *  *
#   *  *  *  *  *  *  *  *
#  *  *  *  *  *  *  *  *  *
# ---------------------------------------------------------------------------------------------------------------------------------#
# FIBBONACI :-
# n=int(input("enter a number:"))
# first=0
# second=1
# for i in range(n):
# 	print(first)
# 	temp=first
# 	first=second
# 	second=temp+second
# ---------------------------------------------------------------------------------------------------------------------------------#
# string=input('enter a palindrome string:')
# revstring=string[::-1]
# if string==revstring:
# 	print("palindrome")
# else:
# 	print("not palindrome")
# ---------------------------------------------------------------------------------------------------------------------------------#
# Armstrong Number:
# num = int(input("Enter a number: "))
# sum=0
# temp=num
# while temp>0:
# 	digit=temp%10
# 	sum += digit ** 3
# 	temp//=10

# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
# -----------------------------------------------------------------------------------------------------------
# check number is even or odd:
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("even")
# else:
#    print("{0} is odd".format(num))
# ------------------------------------------------------------------------------------------
# check number is prime or not:
# num = int(input("enter a number: "))
 
# for i in range(2,num):
# 	if num%i==0:
# 		print("not prime")
# 		break
# else:
# 	print("prime")
# ----------------------------------------------------------------------------------------------------------
# s = "hai mani how are you"
# l = list(s)
# l[4] = 'M'
# s = "".join(l)
# print(s)

# o/p:
# hai Mani how are you
# -------------------------------------------------------------------------------------------------------------
# ADD TWO NUMBERS IN PYTHON:
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# sum=num1 + num2
# print("sum of {0} and {1} is {2}".format(num1,num2,sum))
# --------------------------------------------------------------------------------------------------------------------
# import math
# print(math.factorial(5)) 
# #-----------------------------------------------------------------------------------------------------------
# def factorial(num):
# 	if num == 1:
# 		return(num)
# 	else:
# 		return(num*factorial(num-1))
# num=int(input("enter a number:"))
# if num<0:
# 	print("negative numbers cant print")
# elif num==0:
# 	print("factorial of 0 is 1")
# else:
# 	print("factorial of",num,"is",factorial(num))
# ----------------------------------------------------------------------------------------------------------------------------------
# Python Program for simple interest
# num1=10
# num2=10
# num3=30

# interest=(num1 * num2 * num3)/100
# print(interest)
# ----------------------------------------------------------------------------------------------------------------------------------
# string remove duplicate words in python
# text=input("enter a string:")
# words=text.split(',')
# words=list(set(words))
# duplicatestext=','.join(words)
# print(duplicatestext)
# ---------------------------------------------------------------------------------------------------------------------------
# ADDING TWO LISTS:-
# List1 = [1, 2, 3]
# List2 = [1, 2, 3]
# total = []
 
# for i in range(3):
#     total.append(List1[i] + List2[i])
 
# print("\nThe total Sum of Two Lists =  ", total)

#  output:-
# 	The total Sum of Two Lists =   [2, 4, 6]
# ------------------------------------------------------------
# ADD an ELEMENT TO LIST
# l=[1,2,3]
# new = [x+1 for x in l]
# print(new)

# output:-
# [2, 3, 4]
# -----------------------------------------------------------
# MULTIPLICATION TABLE :-
# n= int(input("enter a number:"))
# for i in range(1,11):
# 	print(n,'x',i,'=',n*i)
# -------------------------------------------------------------------------------------
# MULTIPLICATION TABLE USING FUNCTION:-
# n = int(input("Input a number: "))
# def hi(n):
# 	for i in range(1,11):
#    		print(n,'x',i,'=',n*i)
# hi(n)
# ------------------------------------------------------------------------------------------------------------
# REMOVE DUPLIACTE ELEMENTS FROM LIST:-
# t = [1, 2, 3, 1, 2, 5, 6, 7, 8]

# x=list(set(t))
# print(x)
# ----------------------------------------------------------------------------------
# import re
# e=re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','ayushiwashere@gmail.com')
# e.group()    
# print(e)      
# ------------------------------------------------------------------------
# list = ["1", "4", "0", "6", "9"]
# list = [int(i) for i in list]
# list.sort()
# print (list)
# --------------------------------------------------------------------------------------------------
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# print(A0)
# ----------------------------------------------------------------------------------------------
# a= lambda x,y : x+y 
# print(a(7,86))
# -------------------------------------------------------------------------------------------------
# numbers=[2,4,6,8]
# product=1
# for number in numbers:
# 	product=product*number
# print('the product is :',product)
# ----------------------------------------------------------------------------------------------
# fruits=['apple','mango','orange']
# s=[fruit.upper() for fruit in fruits]
# print(list(enumerate(s)))
# ----------------------------------------------------------------------------------
# m=int(input("enter your first num:"))
# n=int(input("enter your second num:"))
# sum=m * n
# print("the product of {0} and {1} is : {2}".format(m,n,sum))
# --------------------------------------------------------------------------------
