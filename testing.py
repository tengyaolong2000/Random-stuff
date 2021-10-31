class Car():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print('This car has ' + str(self.odometer_reading) +' miles on it.')


	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You cannot roll back the odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles


class Battery():
	def __init__(self, battery_life = 70):
		self.battery_life = battery_life

	def describe_battery(self):
		print('This car has a battery of ' + str(self.battery_life) + ' kWh.')

	def upgrade_battery(self):
		if self.battery_life != 85:
			self.battery_life = 85
		


class ElectricCar(Car):

	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		
		self.battery_life = Battery()


	def get_range(self):
		if self.battery_life.battery_life == 70:
			range = 240
		elif self.battery_life.battery_life == 85:
			range = 360

		print('This car can travel an approximate range of ' + str(range) + ' km.')
 

my_tesla = ElectricCar('tesla', 'model s', '2021')

print(my_tesla.get_descriptive_name())

print(my_tesla.battery_life.describe_battery())

my_tesla.get_range()

my_tesla.battery_life.upgrade_battery()
my_tesla.get_range()









 