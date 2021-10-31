import json
import pygal
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle


filename = '/Users/tengyaolong/Desktop/Python_work/Python Projects/population_data.json'


def get_country_code(countryname):
	'''Return the Pygal 2-digit code for a given country'''
	for digit, country in COUNTRIES.items():
		if countryname.lower() == country.lower():
			return(digit)
	return None




with open(filename) as f_obj:
	pop_data = json.load(f_obj)

cc_populations = {}

for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		print(country_name + ' has a population of ' + str(population))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population
		
			
cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pop1[cc] = pop

	elif pop < 1000000000:
		cc_pop2[cc] = pop

	else:
		cc_pop3[cc] = pop

print(len(cc_pop1), len(cc_pop2), len(cc_pop3))



			


wm_style = RotateStyle('#339966')

wm = World(style=wm_style)


wm.title = 'World population in 2010 by country'
wm.add('0-10m', cc_pop1)
wm.add('10m-1bn', cc_pop2)
wm.add('>1bn', cc_pop3)



wm.render_to_file('americas.svg')

print(cc_populations)











	

