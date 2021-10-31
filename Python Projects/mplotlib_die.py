import matplotlib.pyplot as plt 
from die import Die 

die_1 = Die()
die_2 = Die()

x_values = list(range(2, die_1.num_sides + die_2.num_sides +1))

sum = []
for value in range(1000):
	sum.append(die_1.roll()+die_2.roll())

y_values = [sum.count(value) for value in range(2, 13)]

print(y_values)


plt.scatter(x_values, y_values, edgecolor='none', c=x_values, cmap=plt.cm.Reds)
plt.xlabel('Sum of die')
plt.ylabel('Frequency of sum')
plt.title('Graph of sum of 2 random die rolls against frequency of the sum')

plt.show()