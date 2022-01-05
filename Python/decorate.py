# a simple method that demonstrate how decorators work

def decorateDivider(func):
	def handler(num1, num2):
		if(num2==0):
			return "cant't divide by 0"
		return func(num1,num2)
	return handler

@decorateDivider
def divide(n1,n2):
	return n1/n2

print(divide(6,0))


