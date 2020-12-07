# Strings in python are surrounded by either single or double quotation markname. Let's look at string formatting and some string methods

first_name = "jOhn"
last_name = "dOe"

# String Formatting
'''
  1. with %
  2. with .format()
  3. f-strings // only available for python 3.6+
'''
# print(f'My name is {first_name} {last_name}')

# concatenation
# name = first_name + " " + last_name
name = f'{first_name} {last_name}'

# String Methods
'''
  len(<string>)
  <string>.capitalize()
  <string>.upper()
  <string>.lower()
  <string>.swapcase()
  <string>.count(<string>)
  <string>.startswith(<string>)
  <string>.endswith(<string>)
  <string>.split(<string>)
  <string>.find(<string>)
  <string>.isalnum(<string>)
  <string>.isalpha(<string>)
  <string>.isnumeric(<string>)
'''

# Original String
print(f'Original        => {name}')

# finding length of a string
print(f'Length          => {len(name)}')

# Capitalize
print(f'Capitalize      => {name.capitalize()}')

# Upper Case
print(f'UpperCase       => {name.upper()}')

# Lower Case
print(f'LowerCase       => {name.lower()}')

# Swap case
print(f'swapcase        => {name.swapcase()}')

# Replace
print(f"replace (e,n)         => {name.replace('e', 'n')}")
print(f"replace (e,navan)     => {name.replace('e', 'navan')}")

# Count
sub_string = 'O'
print(f'count           => {name.count(sub_string)}')

# Starts with
print(f"startswith hello      => {name.startswith('hello')}")
print(f"startswith jo         => {name.startswith('jo')}")
print(f"startswith j          => {name.startswith('j')}")

# Ends with
print(f"endswith d      => {name.endswith('d')}")
print(f"endswith e      => {name.endswith('e')}")

# Split into a list
print(f'split           => {name.split()}')
print(f"split with 'o'  => {name.split('o')}")
print(f"split with 'h'  => {name.split('h')}")

# Find position
print(f"find n          => {name.find('n')}")
print(f"find x          => {name.find('x')}")

# Is all alphanumeric
print(f"isisalnum                 => {name.isalnum()}")
print(f"isisalnum 'hello123'      => {'hello123'.isalnum()}")
print(f"isisalnum 'hello123$'     => {'hello123$'.isalnum()}")

# Is all alphabetic
print(f"isalpha                   => {name.isalpha()}")
print(f"isalpha 'hello123'        => {'hello123'.isalpha()}")
print(f"isalpha 'hello123'        => {'hello'.isalpha()}")


# Is all numeric
print(f"isnumeric                 => {name.isnumeric()}")
print(f"isnumeric 'hello123'      => {'hello123'.isnumeric()}")
print(f"isnumeric '123'           => {'123'.isnumeric()}")
