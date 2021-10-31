

def decompose(n):
	list1 = [n]
	remainder = 0


	while list1:
		number = list1.pop()
		remainder += number**2
		
		for i in range(number-1, 0, -1):
			
			
			if remainder-(i**2) >= 0:
				remainder -= i**2

				list1.append(i)


				if remainder == 0:
					list1.sort()
					return list1

			
			
	return None
	

		

k = decompose(100)
print(k)



