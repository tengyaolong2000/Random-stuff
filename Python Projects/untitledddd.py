from pygal.maps.world import COUNTRIES

def get_country_code(countryname):
	'''Return the Pygal 2-digit code for a given country'''
	for digit, country in COUNTRIES.items():
		if countryname.lower() == country.lower():
			print(digit)
	
		else:
			print('Nuttin')

get_country_code('zimbabwe')

def get_country_code(countryname):
	'''Return the Pygal 2-digit code for a given country'''
	for digit, country in COUNTRIES.items():
		if countryname.lower() == country.lower():
			return(digit)
	return None

print(get_country_code('Afghanistan'))

print(get_country_code('United Arab Emirates'))

