def dirReduc(arr):
	while True:
		for ar in arr:
			if ar  == 'NORTH':
				try:
					if arr[arr.index('NORTH')+1] == 'SOUTH':

						#always delete South first then North to preserve the correct North+1 index
						del arr[arr.index('NORTH')+1] 
						del arr[arr.index('NORTH')]
				except ValueError:
					pass
				try:
					if arr[arr.index('NORTH')-1] == 'SOUTH' and arr[arr.index('NORTH')] != 0:
						del arr[arr.index('NORTH')-1]
						del arr[arr.index('NORTH')]
				except ValueError:
					pass

			if ar == 'WEST':
				try:
					if arr[arr.index('WEST')+1] == 'EAST':

						#same as above but for West
						del arr[arr.index('WEST')+1] 
						del arr[arr.index('WEST')]
				except ValueError:
					pass
				try:
					if arr[arr.index('WEST')-1] == 'EAST' and arr[arr.index('WEST')] != 0:
						del arr[arr.index('WEST')-1]
						del arr[arr.index('WEST')]
				except ValueError:
					pass
		try:
			if arr[arr.index('NORTH')+1] != 'SOUTH' and (arr[arr.index('NORTH')-1] != 'SOUTH' and arr[arr.index('WEST')] != 0) and arr[arr.index('WEST')+1] != 'EAST' and (arr[arr.index('WEST')-1] != 'EAST' and arr[arr.index('WEST')] != 0):
				break
		except ValueError:
			#ValueError means it is reduced also as there is no North, South, East or West or the combination of any of those left
			break
		except IndexError:
			break

	return arr

y = dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
print(y)




















