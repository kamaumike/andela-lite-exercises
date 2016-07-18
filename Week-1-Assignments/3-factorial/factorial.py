def factorial(n):
	'''Returns the factorial of a number'''	
	result = 1	
	for i in range(2, n+1):
		result *= i
	return	result
			
		