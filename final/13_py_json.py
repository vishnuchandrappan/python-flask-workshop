# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
# JSON - JavaScript Object notation
# we need to import json module
import json

# Sample JSON
userJson = '{"first-name": "John","last-name": "Doe","email": "john@example.com"}'

# Parsing to dictionary
user = json.loads(userJson)
print(f'user => {user} >> type = {type(user)}')


# converting dictionary to JSON
task = {'id': 1, 'content': 'Learn python', 'completed': False}
taskJson = json.dumps(task)

print(f'taskJson => {taskJson} >> type {type(taskJson)}')
