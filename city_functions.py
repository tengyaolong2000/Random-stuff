def return_city_country(city, country, population=0):
	name = city.title() + ', ' + country.title()
	if population:
		name += ' - population ' + str(population)
	return name


