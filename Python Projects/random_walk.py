from random import choice

class RandomWalk():

	def __init__(self, num_points=5000, x_values=[0], y_values=[0]):
		self.num_points = num_points

		#All walks start at (0, 0).

		self.x_values = x_values
		self.y_values = y_values


	def get_step(self):
		
		
			direction = choice([1, -1])
			distance = choice([0, 1, 2, 3, 4])
			step = direction * distance
			return step


			

	def fill_walk(self):
		"""Calculate all the points in the walk"""

		#Keep taking steps until the walk reaches the desired length
		while len(self.x_values) < self.num_points:

			x_step = self.get_step()
			y_step = self.get_step()

			if x_step and y_step == 0:
				continue

			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			self.x_values.append(next_x)
			self.y_values.append(next_y)





