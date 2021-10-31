import re
from re import search

Regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]){6,}$')
mo = Regex.search('1djkljaShl') 
x = mo.group()
print(x)
