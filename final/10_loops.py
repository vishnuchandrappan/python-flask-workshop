# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
friends = ['Chandler', 'Joey', 'Phoebe', 'Monica']


# Simple for loop
for person in friends:
    print(f'Hey its me, {person}')

# Control Statements break, continue
# Break
print()
for person in friends:
    print(f'Hey its me, {person}')
    if person == 'Joey':
        break

# Continue
for person in friends:
    print(f'\nHey its me, {person}')
    if person != 'Joey':
        continue
    print("How u doing ?")

# range only argument => 0 to arg-1
print()
for i in range(len(friends)):
    print(f"person @ index {i} ==> {friends[i]}")

# range(a,b) => a to b-1
print()
for i in range(0, 11):
    print(f'Number: {i}')

# range(a,b,c) => a to b-1 => a, a+c, a+2c, a+3c, ...
print()
for i in range(0, 11, 2):
    print(f'Even Number: {i}')
print()
for i in range(1, 11, 2):
    print(f'Odd Number: {i}')

# While loops execute a set of statements as long as a condition is true.
print()
count = 0
while count < 10:
    print(f'Count: {count}')
    count += 1

size = 5
# nested loop
print()
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("  ", end="")
        else:
            print("* ", end="")
    print()

print()
for i in range(size):
    for j in range(size):
        if (i + j) % 2 != 0:
            print("  ", end="")
        else:
            print("* ", end="")
    print()

# some common patterns
'''
*
* *
* * *
* * * *
* * * * *
'''
print()
for i in range(size):
    print("* "*(i+1))

'''
* * * * *
* * * *
* * *
* *
*
'''
print()
for i in range(size, 0, -1):
    print("* "*i)

'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
print()
for i in range(size):
    print(f"{'  '*(size-i-1)}{'* '*((i*2)+1)}")
