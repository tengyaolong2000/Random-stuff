import pygal
from random_walk import RandomWalk


rw = RandomWalk()

rw.fill_walk()

x_values = rw.x_values
y_values = rw.y_values





random_walk_graph = pygal.XY(stroke=False)

random_walk_graph.title = 'Random Walk'


rw = list(zip(x_values, y_values))
random_walk_graph.add('Ant', rw, dots_size=2, color='blue' )

random_walk_graph.render_to_file('pygal_rw.svg')

