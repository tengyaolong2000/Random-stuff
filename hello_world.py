import json

message = input('What is your favourite number?\n')

file_name = '/Users/tengyaolong/Desktop/Python_work/json_files/favourite_number.json'

with open(file_name, 'w') as file_object:
	json.dump(message, file_object)



import json

file_name = '/Users/tengyaolong/Desktop/Python_work/json_files/favourite_number.json'

with open(file_name, 'r') as f_object:
	number = json.load(f_object)

print('Your favourite number is ' + number + '!')


