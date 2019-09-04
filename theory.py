# what are datatypes:

# 1. integer ---> ex: 10,20,30
# 2. string  ---> ex: 'mani','kumar'
# 3. float   ---> ex: 10.2,23.4
# 4. boolean  --> ex: true or false
# -------------------------------------------------------------------------------
# what is QAUTH?
# OAuth doesnt share password data but instead uses authorization tokens to prove an identity between consumers and service providers.

# what is OAuth?

# OAuth(Open Authorization) is an open standard for tokenbased authentication and authorization on the Internet.
# OAuth, which is pronounced "oh-auth," allows an end users account information to be used by third-party 
# services, such as Facebook, without exposing the users password.
# 	OAuth 2.0 is an authorization type that enables you to approve an application that contacts another application 
# 	for you without exposing your password.

# what is Bearer Token?
# A bearer token is a security token. Any user with a bearer token can use it to access data resources without using a cryptographic key

# What is Pickle in python ?
# 	It is used for serializing and de-serializing a Python object structure.

# 	Pickling is a way to convert a python object (list, dict, etc.) into a character stream. 
# 	The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.

# 	pickle has two main methods. The first one is dump, which dumps an object to a file object 
# 	and the second one is load, which loads an object from a file object.

# what is self in python?
# 	self : self represents the instance of the class. By using the "self" keyword we can access the attributes
# 	and methods of the class in python.

# what are methods and attributes in python?

# 	class C:
#     def my_method(self): #here self is an attribures
#         print("I am a C")
	# c = C()
	# c.my_method() #here my_method is an method


# What is a class and an object?
# 	Object − Objects have states and behaviors. 
# 		Example: A dog has states - color, name, breed as well as behaviors – wagging the tail, barking, eating.
# 		An object is an instance of a class. 

# 	Class :− A class can be defined as a template/blueprint that describes 
# 			the behavior/state that the object of its type support.
# --------------------------------------------------------------------------------------------------------------------
# What is the difference between render and redirect in Django? 

# 	Both are totally different where the redirect gives the HttpResponseRedirect 
# 	for the argument you have passed. 

	# The render function Combines a given template
# 	with a given context dictionary and returns an HttpResponse object 
# 	with that rendered text. You request a page and the render function returns it.

# What is admin interface in Django?
	# The Django admin is a very powerful tool. We use it for day to day operations, browsing data and support

# 	Python. Django Admin Interface. Django provides a default admin interface which can be used 
# 	to perform create, read, update and delete operations on the model directly.
# ---------------------------------------------------------------------------------------------------------------------------------------

# what is monkey patching?
# 	Python is a dynamic programming language and therefore the classes in python 
# 	are mutable so that you can reopen them, modify, or even replace them. 
# 	In simple words, monkey patching is making changes to a module or class while the program is running. 
# 	It refers to reopening the existing classes or methods in class at runtime and changing their behavior
# 	according to the requirement. This code can be used whenever you need it. A Monkey Patch is a piece of Python
# 	code which extends or modifies other code at runtime.

# ----------------------------------------------------------------
# list  - Lists are mutable i.e they can be edited
# string - immutable
# tuple - Tuples are immutable (tuples are lists which can’t be edited).
# set  - mutable
# dictionary - mutable
# ---------------------------------------------
# PEP stands for Python Enhancement Proposal.
# -----------------------------------------------
#  How is memory managed in Python?
# Ans: Memory management in python is managed by Python private heap space. 
# 	All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap.
# 	 The python interpreter takes care of this instead.
# ------------------------------------------------------------------------------------------------------------------------------------
#  What are local variables and global variables in Python?
# Global Variables:

# Variables declared outside a function or in global space are called global variables. These variables can be accessed by any function in the program.

# Local Variables:

# Any variable declared inside a function is known as a local variable. This variable is present in the local space and not in the global space.
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# What are functions in Python?
# Ans: A function is a block of code which is executed only when it is called. To define a Python function, the def keyword is used.

# Example:-

# def Newfunc():
#  print("Hi, Welcome to Edureka")
# Newfunc(); 
# Output: Hi, Welcome to Edureka
# --------------------------------------------------------------------------------------------------------------------------
# What is __init__?
# Ans: __init__ is a method or constructor in Python. 
# 	This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# What is self in Python?
# Ans: Self is an instance or an object of a class.
# 	The self variable in the init method refers to the newly created object while in other methods, it refers to the object whose method was called
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Help() function: The help() function is used to display the documentation string and also 
# 	facilitates you to see the help related to modules, keywords, attributes, etc.
# Dir() function: The dir() function is used to display the defined symbols.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
#  How are classes created in Python? 
# Ans: Class in Python is created using the class keyword.

# Example:

# class Employee:
# def __init__(self, name):
# self.name = name
# E1=Employee("abc")
# print(E1.name)
# Output: abc
# -------------------------------------------------------------------------------------------------
# Flask is a “microframework” primarily build for a small application with simpler requirements. 
# 	In flask, you have to use external libraries. Flask is ready to use.
# Pyramid is built for larger applications. It provides flexibility and lets the developer use the right tools for their project. 
# 	The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.
# Django can also be used for larger applications just like Pyramid. It includes an ORM.
# ---------------------------------------------------------------------------------------------------------------------------------------------
