
import pygal
from die import Die 


die_1 = Die()
die_2 = Die()
die_3 = Die()

dice = [die_1, die_2]


results = []

for roll_number in range(100000):
	results.append(die_1.roll() * die_2.roll())




frequencies = [results.count(value) for value in range(1, die_1.num_sides*die_2.num_sides+1)]



hist = pygal.Bar()

hist.title = 'Results of rolling three dice 10000 times'
hist.x_labels = [values for values in range(1, die_1.num_sides*die_2.num_sides+1)]

hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('dice', frequencies)
hist.render_to_file('die_visual.svg')


