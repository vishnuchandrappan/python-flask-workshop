# A Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.

fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits3 = ('Apples',)

# Get value
print(f'el @ index 1        => {fruits[1]}')

# tuple supprots slicing
print(f'Sliced fruits[:]    => {fruits[:]}')

# Can't change value
# fruits[0] = 'Pears'       # error

# deletion of tuple element is not supported
# del fruits[0]             # error

# Delete tuple
# del fruits

# Get length
print(f'length of tuple     => {len(fruits)}')

# combining tuples
print()
tup1 = (1,2,3)
tup2 = ('a','b','c')

print(f'{tup1} + {tup2} results in    => {tup1 + tup2}')

# repetition
print()
tup = ('a',)
print(f"repeating {tup} 4 times       => {tup * 4}")

# Checking membership
print()
print(f"check if 3 in {tup1}           => {3 in tup1}")
print(f"check if 31 in {tup1}          => {31 in tup1}")

# min, max, sum
print()
print(f"min and max of {tup1} is       => {min(tup1)} and {max(tup1)}")
print(f"Sum of {tup1} is               => {sum(tup1)}")

# Converting list to tuple
print()
list1 = [1,2,3]
new_tup = tuple(list1)

print(f'list is {list1} with type {type(list1)}')
print(f'tuple is {new_tup} with type {type(new_tup)}')
