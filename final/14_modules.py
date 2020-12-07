# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

'''
We've imported json module in the prev. section
There are some core modules which comes pre-installed with python
some of them are - datetime, time, json, ...
'''

# basic usage
import datetime
print(f'today => {datetime.date.today()}')

# we can also import specific parts of a module
from json import dumps
card = {"company": "Tata", "model": "nexon", "type": "EV"}
cardJson = dumps(card)

# lets create our own module. Create a new file helpers.py
from helpers import snakeCase
val = "First name"
print(f"snake case of {val} => {snakeCase(val)}")

#using 3rd party modules
'''
We use pip to install packages / modules

Sample usage (in shell)

pip install uuid
'''
import uuid
print(uuid.uuid1())
print(uuid.uuid4())
