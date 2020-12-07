# Operators are used to perform operations on variables and values.

'''
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
'''


a, b = 10, 2.1

# Arithmetic Operators
sum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
powered = a ** b
floor_division = a//b

# String formatting
print('Sum is %s' % sum)
print('Difference is %s & product is %s' % (difference, product))
print('Quotient is {result} & remainder is {remainder}'.format(
    result=quotient, remainder=remainder))
print(
    f'a to the power b is {powered} & floor_division result is {floor_division}')

''' # Output
Sum is 12.1
Difference is 7.9 & product is 21.0
Quotient is 4.761904761904762 & remainder is 1.5999999999999996
a to the power b is 125.89254117941675 & floor_division result is 4.0
'''

# Assignment Operators
'''
=, +=, -=, *=, /=, %=, //=,**=

|=, &=, ^=, >>=, <<=
'''


# Comparison Operators
'''
==, !=, >, <, >=, <=
'''


# Logical Operators
'''
a = True
b = False
print(f'OR => {a or b}')
print(f'AND => {a and b}')
print(f'NOT => {not a}')
'''


# Identity Operators
'''
    is - returns true if both are same objects
         usage,
         a is b
    is - returns true if both are different objects
         usage,
         a is not b
'''


# Membership Operators
'''
    in - usage,
         a in b
         returns true if a is in b

    not in - usage,
         a not in b
         returns true if a is not in b
'''
'''
name = "John Doe"
print(f"IN => {'x' in name}")
print(f"NOT IN => {'x' not in name}")
'''


# Bitwise Operators
'''
& and
| or
^ xor
~ not
<< zero fill left shift
>> Signed right shift
'''