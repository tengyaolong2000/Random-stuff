def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)


def hello(n):
    return

x = hello('A')
print(x)

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

