def fib(n):
	if n<=2:
		f=1
	else:
		f = fib(n-1) + fib(n-2)
	return f

x = fib(6)

print(x)