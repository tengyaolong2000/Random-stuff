
#prompt the user for username
username = input('What is your username?\n')

#find out if the username exists


file_name = '/Users/tengyaolong/Desktop/Python_work/text_files/verify_user.txt'

try:
	with open(file_name, 'r') as f_obj:
		list_username = f_obj.readlines()
		 
		if username + '\n' in list_username:
			print('Hello ' + username + '!')

		else:
			account = input('This username does not exist, would you like to create an account? (y/n) \n')
			if account == 'y':
				create_username = input('Please enter your username.\n')
				
				with open(file_name, 'a') as f_obj:
					f_obj.write(create_username + '\n')
					
			else:
				print('Ok, goodbye!')

except FileNotFoundError:
	with open(file_name, 'a') as f_obj:
		f_obj.write(username + '\n')
		print('User created!')

		
		
