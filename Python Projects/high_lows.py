import csv
from matplotlib import pyplot as plt 
from datetime import datetime

file_name = '/Users/tengyaolong/Desktop/ehmatthes-pcc-f555082/chapter_16/sitka_weather_2014.csv'

with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	for index, column_header in enumerate(header_row):
		print(index, column_header)


	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)
		high = int(row[1])
		highs.append(high)
		low = int(row[3])
		lows.append(low)



fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', linewidth=0.5, alpha=0.5)
plt.plot(dates, lows, c='blue', linewidth=0.5, alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

fig.autofmt_xdate()

plt.title('Daily high and low temperatures in 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()



