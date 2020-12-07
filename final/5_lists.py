# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(f'numbers           => {numbers}')
print(f'fruits            => {fruits}')


# Type
print()
print(f'type              => {type(numbers)}')


# Lists can be created using constructors too
print()
c_list = list((7,8,9));
print(f'with constr.      => {c_list}')


# List can have values of any datatype
items = [1, 2, "three", "four", 5.0, True]
print(f'items             => {items}')


# List can also have another list as member
print()
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [1, 8, 9]

new_list = [list_1, list_2, list_3, 1, "lorem"]
print(f'new list          => {new_list}')


# List ALLOW duplicates
print()
list_4 = [1, 1, 2, 3]
print(f'List with dups    => {list_4}')


# access value from list
print()
print(f'el @ index 0      => {list_4[0]}')
print(f'el @ index 1      => {list_4[1]}')
print(f'el @ index -1     => {list_4[-1]}')
print(f'el @ index -2     => {list_4[-2]}')


# List Slicing
# from a start_index to end_index - 1
new_list = ['a', 'b', 'c', 'd', 'e']
print()
print(f'New List          => {new_list}')
print(f'new_list[0:2]     => {new_list[0:2]}')
print(f'new_list[0:-1]    => {new_list[0:-1]}')
print(f'new_list[0:]      => {new_list[0:]}')
print(f'new_list[:]       => {new_list[:]}')
print(f'new_list[1:]      => {new_list[1:]}')
print(f'new_list[::2]     => {new_list[::2]}')
print(f'new_list[1::2]    => {new_list[1::2]}')



# List methods / operations on lists
print()
print("===> Methods <===")
print()

# Append to list
fruits.append('Mangoes')
print(f'append Mangoes                => {fruits}')

# Remove from list
fruits.remove('Grapes')
print(f'remove Grapes                 => {fruits}')

# Insert into position
fruits.insert(2, 'Strawberries')
print(f'insert @ 2 Strawberries       => {fruits}')

# Change value
fruits[0] = 'Blueberries'
print(f'change @0 Blueberries         => {fruits}')

# Remove with pop
fruits.pop(2)
print(f'pop @2                        => {fruits}')

# Reverse list
fruits.reverse()
print(f'reverse                       => {fruits}')

# Sort list
fruits.sort()
print(f'sort                          => {fruits}')

# Reverse sort
fruits.sort(reverse=True)
print(f'sort reverse                  => {fruits}')

# join
print()
print(f"join                => {''.join(fruits)}")
print(f"join with ' '       => {' '.join(fruits)}")
print(f"join with ', '      => {', '.join(fruits)}")
print(f"join with 'XoXo'    => {'XoXo'.join(fruits)}")


# converting string to list
print()
name = "John Doe"
name_list = list(name)

print(f'{name} converted to list is ==> {name_list}')

# reversing a string in python
name_list.reverse()
print(f'Reverse of list ==> {name_list}')
print(f"Joined string ==> {''.join(name_list)}")

