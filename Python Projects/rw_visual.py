import matplotlib.pyplot as plt 
from random_walk import RandomWalk

while True:

	rw = RandomWalk()
	rw.fill_walk()

	x_value = rw.x_values
	y_value = rw.y_values


	point_numbers = list(range(rw.num_points))
	plt.scatter(x_value, y_value, s=1, c=point_numbers, cmap=plt.cm.Blues)

	plt.scatter(0, 0, s=10, c= 'green', edgecolor='none')
	plt.scatter(rw.x_values[-1], rw.y_values[-1], s=10, c='red', edgecolor='none')


	plt.show()


	