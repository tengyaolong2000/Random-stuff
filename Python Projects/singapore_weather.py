import csv
import matplotlib.pyplot as plt 
from datetime import datetime
import numpy as np


filename = '/Users/tengyaolong/Desktop/Python_work/Python Projects/DAILYDATA_S24_202101.csv'

with open(filename) as f_obj:
	reader = csv.reader(f_obj)
	header = next(reader)
	print(header)

	maximum = []
	minimum = []
	dates = []

	for row in reader:
		max = float(row[-4])
		min = float(row[-3])
		maximum.append(max)
		minimum.append(min)
		
		date = row[1]+ '-' +row[2] + '-' + row[3]
		list_of_dates = []
		list_of_dates.append(date)
		for list in list_of_dates:
			dates.append(datetime.strptime(list, "%Y-%m-%d"))

print(len(dates))
print(len(maximum))


fig = plt.figure(dpi=128, figsize=(10,6))

plt.plot(dates, maximum, c='red', linewidth=2)
plt.plot(dates, minimum, c='blue', linewidth=2)
plt.fill_between(dates, maximum, minimum, facecolor='yellow')

fig.autofmt_xdate()
plt.ylabel('Temperature (Celsius)', fontsize=16)
plt.xlabel('Date', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()