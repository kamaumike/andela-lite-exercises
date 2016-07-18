def sum_of_digits(A):
	'''Takes in a list of numbers and 
	returns the sum of all the digits in the numbers 
	'''
	sum_of_numbers = 0

	for i in range(len(A)):
		integer_holder = A[i]	# an integer at this point
		string_holder = str(integer_holder) # convert integer to string at this point in order to loop through
		
		# looping through the string
		for digit in string_holder:			
			sum_of_numbers += int(digit)

	return sum_of_numbers		
