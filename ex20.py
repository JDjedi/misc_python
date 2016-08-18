def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "subtract"
	return a - b

def multiply(a, b):
	print "multiply"
	return a * b

def divide(a, b):
	print "divide"
	return a / b

age = add(20, 6)
height = subtract(74, 72)
weight = divide(245, 5)
weight2 = multiply(divide(245, 5), 5)

print age
print height
print weight
print weight2