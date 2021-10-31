import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

filename = '/Users/tengyaolong/Desktop/Python_work/csv_files/data.csv'

data = pd.read_csv(filename)
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']


language_counter = Counter()

for language in lang_responses:
	language_counter.update(language.split(';'))

languages = []
popularity = []


for language, number in language_counter.most_common(15):
	languages.append(language)
	popularity.append(number)

languages.reverse()
popularity.reverse()

plt.style.use('fivethirtyeight')
plt.barh(languages, popularity)

plt.title('Top 15 Most common programming languages')
plt.xlabel('Popularity')
plt.tight_layout()

plt.show()


