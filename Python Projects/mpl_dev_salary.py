import matplotlib.pyplot as plt
import pandas as pd 

filename = '/Users/tengyaolong/Desktop/Python_work/csv_files/data_dev.csv'

data = pd.read_csv(filename)
age = data['Age']
all_devs = data['All_Devs']
python = data['Python']
javascript = data['JavaScript']
overall_median = 57287

plt.style.use('seaborn')
plt.title('Graph of Developer Salary with age')
plt.xlabel('Age')
plt.ylabel('Salary')

plt.plot(age, all_devs, label='All Developers', linewidth=1.7)
plt.plot(age, python, label='python', linewidth=1.7)
plt.plot(age, javascript, label='JavaScript', linewidth=1.7)

plt.fill_between(age, python, overall_median,
				where=(python <= overall_median),
				interpolate=True, alpha=0.25)
plt.tight_layout()
plt.legend()

plt.show()



