def dirReduc(arr):
	hello = True
	while hello:
		for ar in arr:
			if ar  == 'NORTH':
				if arr[arr.index('NORTH')+1] == 'SOUTH':
					if arr.index('NORTH') != -1:

					#always delete South first then North to preserve the correct North+1 index
						del arr[arr.index('NORTH')+1] 
						del arr[arr.index('NORTH')]
				
				elif arr[arr.index('NORTH')-1] == 'SOUTH':
					if arr.index('NORTH') != 0:
						del arr[arr.index('NORTH')-1]
						del arr[arr.index('NORTH')]

			if ar == 'WEST':

				if arr[arr.index('WEST')+1] == 'EAST':
					if arr.index('WEST') != -1:

					#same as above but for West
						del arr[arr.index('WEST')+1] 
						del arr[arr.index('WEST')]
				
				elif arr[arr.index('WEST')-1] == 'EAST':
					if arr.index('WEST') != 0:
						del arr[arr.index('WEST')-1]
						del arr[arr.index('WEST')]
		try:			
			if 	arr.index('NORTH') != -1 and arr.index('WEST')  != -1:
				try:
					if arr[arr.index('NORTH')+1] != 'SOUTH' and (arr[arr.index('NORTH')-1] != 'SOUTH' and arr[arr.index('NORTH')] != 0) and arr[arr.index('WEST')+1] != 'EAST' and (arr[arr.index('WEST')-1] != 'EAST' and arr[arr.index('WEST')] != 0):
						hello = False
				except ValueError:
					#ValueError means it is reduced also as there is no North, South, East or West or the comboniation of any of those left
					hello = False
		except ValueError:
			try:
				if 	arr.index('NORTH') != -1  and arr.index('NORTH') != 0:
					if arr[arr.index('NORTH')+1] != 'SOUTH' and arr[arr.index('NORTH')-1] != 'SOUTH':
						hello = False
			except ValueError:
				if arr.index('WEST')  != -1 and arr.index('WEST') != 0:
					if arr[arr.index('WEST')+1] != 'EAST' and arr[arr.index('WEST')-1] != 'EAST':
						hello = False
	return arr

y = dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
print(y)