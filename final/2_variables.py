'''
      What are Keywords, Identifiers and variables ?
'''

# A variable is a container for a value, which can be of various types

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1             # int
y = 1.2           # float
z = "John Doe"    # str
isLoggedIn = True  # bool - !!! Its True not true. Case Sensitive

# print(x)        # 1
# print(type(x))    # <class 'int'>

'''
print(x, type(x), y, type(y), z, type(z), isLoggedIn, type(isLoggedIn))
# 1 <class 'int'> 1.2 <class 'float'> John Doe <class 'str'> True <class 'bool'>
'''

# MASS ASSIGNMENT

a, b, c = 10, 2.1, "hello"
# print(a, b, c)  # 10 2.1 hello
