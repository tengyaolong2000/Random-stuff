import csv
import pygal
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES

def get_country_code(countryname):
	'''Return the Pygal 2-digit code for a given country'''
	for digit, country in COUNTRIES.items():
		if countryname.lower() == country.lower():
			return(digit)
	return None


file_name = '/Users/tengyaolong/Desktop/Python_work/Python Projects/World_electricity_data.csv'

with open(file_name) as f_obj:
	contents = csv.reader(f_obj)
	next(contents)
	next(contents)
	next(contents)
	next(contents)
	header_row = next(contents)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	cc_elec = {}

	for row in contents:

		code = get_country_code(row[0])
		percentage = row[54]

		cc_elec[code] = percentage

wm = World()







	