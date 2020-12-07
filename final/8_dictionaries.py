# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# each element is a key-value pair

# Create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}


# Using constructor
person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(f"first name is {person['first_name']}")
print(f"Hi I'm {person['first_name']} {person.get('last_name')}. I'm {person['age']} years old")

# Add key/value
print()
person['email'] = 'john@example.com'
print(f"after adding email {person}")


# Get dict keys
print()
print(f"Keys are {person.keys()}")

# Get dict items
print()
print(f"Items will give key-val pairs => {person.items()}")

# Get dict items
print()
print(f"Values in dict => {person.values()}")


# Copy dict
print()
person2 = person.copy()
person2['city'] = 'Boston'
print(f"person 1 => {person} \nperson 2 {person2}")

# Remove item
print()
del(person['age'])
print(f"after deleting age {person}")

# removing el with pop()
print()
person.pop('email')
print(f"after popping email => {person}")

# removing last inserted item
print()
person.popitem()
print(f"after popItem => {person}")

# Clear
print()
person.clear()
print(f"after clearing {person}")

# Get length
print()
print(f"person2     => {person2}")
print(f"length of dic   => {len(person2)}")

# Lists can have dict as its el
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

'''

Lists can have list, set, tuple, dictionary, int, float, str
as its elements

Others do support heterogenous el.
'''

