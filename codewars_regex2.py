import re
from re import search

regex = re.compile(r'^(?=.*[a-zA-Z0-9])([a-zA-Z0-9])+$')

x = regex.search("PassW0rd")
mo = x.group()
if mo:
	print('True')