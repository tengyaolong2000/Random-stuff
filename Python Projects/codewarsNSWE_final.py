

def split_join(list, dot_directions):
	#join the list with . and split the list at e.g NORTH.SOUTH and then further split the resultant list at . to obtain result
	join_list = '.'.join(list)
	split_list = join_list.split(dot_directions)
	
	result = []
	for i in split_list:
		x_list = i.split('.')
		
		for x in x_list:
			result.append(x)

	while '' in result:
		result.remove('')

	return result

def dirReduc(arr):
	fourth_cycle = arr
	
	for i in range(len(arr)):
		
		first_cycle = split_join(fourth_cycle, 'NORTH.SOUTH')
		second_cycle = split_join(first_cycle, 'SOUTH.NORTH')
		third_cycle = split_join(second_cycle, 'EAST.WEST')
		fourth_cycle = split_join(third_cycle, 'WEST.EAST')
	
	return fourth_cycle
	


	
	
	




		
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])

	