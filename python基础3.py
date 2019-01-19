def fib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fib(n-1) + fib(n-2)
print(fib(4))
print(fib(30))

squares = []
for value in range(1,11):
		squares.append(value**2)
print(squares)

#汉诺塔
def hannuota(n,a,b,c):
	if n == 1:
		print(a,"-==->",c)
		return None
	hannuota(n-1, a, c, b)
	print(a,"-+->",c)
	hannuota(n-1,b, a, c)
a = "A"
b = "B"
c = "C"
n = 3
hannuota(n,a,b,c)