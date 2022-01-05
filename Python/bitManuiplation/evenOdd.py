# A simple method to know if number is odd or even

def evenOdd(n):
	if(n & 1==1):
		return f"{n} is odd"
	return f"{n} is even"

print(evenOdd(4))

#4 in binary is 0100 and 1 is 0001 since first bit is not set for
# even numbers it will alway will return 0


