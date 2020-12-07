# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('sample.txt', 'w')

# Get file info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('sample.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('sample.txt', 'r+')
text = myFile.read(100)
print(text)
