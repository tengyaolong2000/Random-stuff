file_name = '/Users/tengyaolong/Desktop/Python_work/text_files/A Discourse on Method.txt'

with open(file_name, 'r') as f:
	contents = f.read()
number = contents.count('THE')
print(number)




