# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
# def keyword is used to define a function
def sayHello(name):
    print(f'Hello world, my name is {name}')


sayHello("John Doe")


# deafault parameters
def greeting(person1, person2='world'):
    print(f'Hello {person2}, my name is {person1}')


greeting("Jane Doe")
greeting("Jane Doe", "John Smith")


# named parameters ; order of params can be changed in fn. call
def hello(name, age, designation):
    print(f"Hey there. I'm {name}, a {age} year old {designation}")


hello(age=20, name="John", designation="Developer")


# return values
def getSum(num1, num2):
    return num1 + num2


print(f'Sum of 3 and 4 is {getSum(3,4)}')


# python fns. can return multiple values
def getResults(num1, num2):
    return num1 + num2, num1 * num2


sum, product = getResults(3, 5)
print(f'Sum is {sum} & product is {product}')


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
fetchSum = lambda num1, num2: num1 + num2
print(f'fetchSum result => {fetchSum(2,3)}')