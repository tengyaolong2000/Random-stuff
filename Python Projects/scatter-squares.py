import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=20, edgecolor='none', c=y_values, cmap=plt.cm.Reds)
#Set chart and label the axes
plt.title("Cube numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

#Set the range for each axis.
plt.axis([0, 5000, 0, 5000**3])




plt.show()

