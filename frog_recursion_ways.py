
def ways(n):
	if n == 1:
		return 2

	if n == 2:
		return 3

	if n >= 3:
		return ways(n-1) + ways(n-2)


x = ways(10)
print(x)

