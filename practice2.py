# LEAP YEAR:

# def check_year(year):
# 	if year%4==0 and year%100!=0 or year%400==0:
# 		print("leap year")
# 	else:
# 		print("not leap year")
# check_year(1972)
# check_year(1975)
# -----------------------------------------------------------------------
# import calendar
# print(calendar.isleap(1972))
# print(calendar.isleap(1975))
# ----------------------------------------------------------------

# REGULAR EXPRESSIONS:

# import re
# text = "Dummy python text"
# ans=re.sub("m","-",text)
# print(ans)

# ans2=re.sub("m|t","-",text)
# print(ans2)

# ans3=re.sub("m|t|o","-",text)
# print(ans3)
# ---------------------------------------------------------------------
# joim two lists and make an dictionary:

# key = ['a','b','c']
# value = [1,2,3]

# ans=dict(zip(key,value))
# print(ans)
# -----------------------------------------------------------------------------
# calendar :

# import calendar
# for day_name in calendar.day_name:
# 	print(day_name)

# for month_name in calendar.month_name:
# 	print(month_name)

# print(calendar.month(2019,2))
# -----------------------------------------------------------------------------------
# Date and time :

# from datetime import datetime
# print(datetime.now())

# print(datetime.now().time())

# print(datetime.now().date())
# -------------------------------------------------------------------------
# string = "hi hello mani"
# s=string.replace('h','p')
# print(s)

# s2=string.replace('h','p',1)
# print(s2)

# s3=string.replace('h','p',2)
# print(s3)
# ---------------------------------------------------------------------------
# string="hello mani"
# s1=string.startswith('h')
# s2=string.endswith('i')

# print(s1)
# print(s2)

# s3=string.title()
# print(s3)

# s4=string.count('m')
# print(s4)

# s5=len(string)
# print(s5)

# s6=string.count('')
# print(s6)
# -------------------------------------------------------------------------------------------
# list1=[1,2,3,4,5]
# for item in list1:
# 	if item==6:
# 		print("present")
# 		break
# else:
# 		print("not present")


# for item in list1:
# 	if item==2:
# 		print("present")
# 		break
# else:
# 		print("not present")
# --------------------------------------------------------------------------------------------
# from itertools import cycle
# list1=[1,2,3]
# cy=cycle(list1)
# for i in range(5):
# 	print(next(cy))
# -------------------------------------------------------------------------------------

# string="manikumar"
# star=''
# for i in range(10):
# 	star += '*'
# print(star + string + star)
# ----------------------------------------------------------------------------------
# import os
# import time


# s=0
# m=0

# while s<=60:
#     os.system('cls')
#     print (m, 'Minutes', s, 'Seconds')
#     time.sleep(1)
#     s+=1
#     if s==5:
#         m+=1
#         s=0
#         print("good bye")
#         break
