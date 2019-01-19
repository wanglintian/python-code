def a(n):
	n[2] = 300
	print(n)
	return None
def b(n):
	n += 100
	print(n)
	return None

an = [1,2,3,4,5,6]
bn = 9

print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)