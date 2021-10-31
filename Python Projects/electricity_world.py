import csv
import pygal
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle

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
		try:
			percentage = row[54]
			new = float(percentage)
			cc_elec[code] = new
		except ValueError:
			pass
			
		
print(cc_elec)

wm_style = RotateStyle('#339966')
		
wm = World(style=wm_style)

wm.title = 'Percentaege of people who have access to electricity in the world in 2010'

wm.add('2010', cc_elec)

wm.render_to_file('world_electricity_access.svg')





	