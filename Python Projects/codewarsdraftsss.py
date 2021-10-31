def count_bits(n):
	return [i for i in bin(n)].count('1')

a = 0
while True:
	a = a + 1

	if a == 20:
		break

	print(a)