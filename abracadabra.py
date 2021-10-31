responses = {}
polling_active = True

while polling_active:
	name = input('What is your name? \n')
	response = input("Are u good?")
	responses[name] = response

	repeat = input('Continue? Y/no')
	if repeat == 'no':
		break
	else:
		continue

