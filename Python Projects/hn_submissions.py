import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

#Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

#Process information about each submission.
submission_ids = r.json()


submission_dicts = []

for submission_id in submission_ids[0:30]:
	#Make a seperate API call for each submission.
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) +'.json')

	submission_r = requests.get(url)
	
	response_dict = submission_r.json()

	submission_dict = {
		'title': response_dict['title'],
		'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
		'comments': response_dict.get('descendants', 0)
	}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)





#Make visualisation
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.truncate_label = True
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most commented articles on Hacker News of all time.'
y_values, x_values = [], []
for submission_dict in submission_dicts:
	y_values.append(submission_dict['comments'])
	x_values.append(submission_dict['title'])

chart.add('hello', y_values)
chart.x_labels = x_values
chart.render_to_file('hackernews.svg')

