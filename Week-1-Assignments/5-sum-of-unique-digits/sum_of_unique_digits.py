def sum_of_unique_digits(A):
	'''Takes in a list of numbers and 
	returns the sum of all the unique digits in the numbers 
	'''
	integer_holder = 0
	string_holder = ''
	unique_digits_list = []
	sum_of_unique_digits = 0

	# eliminating duplicate numbers in list 'A'
	for i in range(len(set(A))):
		integer_holder = A[i]
		# convert integer to string
		string_holder = str(integer_holder)	
		
		# spliting numbers into single digits by looping through the 'string_holder'
		for digit in string_holder:			
			if int(digit) not in unique_digits_list:
				# adding single digit numbers to empty array as integers
				unique_digits_list.append(int(digit))	
				
				# looping through the array containing integers
				for num in range(len(unique_digits_list)):
					pass

				sum_of_unique_digits += unique_digits_list[num]
				
	return sum_of_unique_digits		
