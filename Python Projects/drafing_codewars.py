import string


def pig_it(text):
	
	punctuations= string.punctuation 
	
	split_text = text.split()

	translation = ''


	for word in split_text:

		list_word = word.split()
		
		for j in list_word:
			new_list_word = [k for k in j[1:]]

			if j[0] not in punctuations:

				new_list_word.append(j[0] + 'ay')
				new_word = ''.join(new_list_word)
			
			else:
				new_list_word.append(j[0])
				new_word = ''.join(new_list_word)


		translation += new_word + ' '


	return translation.strip()
		



x = pig_it('Quis custodiet ipsos custodes ?')
print(x)
