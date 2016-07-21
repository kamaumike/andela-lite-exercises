def num_to_word(number):
	'''Returns the words of a digit'''

	dictionary_of_words = {
	0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
	5: 'five', 6: 'six', 7:'seven', 8:'eight', 9: 'nine'
	}
	

	to_string = str(number)
	to_integer = 0
	
	# Loop through the string of numbers
	for i in to_string:
		to_integer = int(i)
						
		if to_integer:	
			# Loop through the dictionary		
			for w in dictionary_of_words:
				# check if the single digit matches the key in the dictionary
				if to_integer == w:
					print dictionary_of_words[w] , 
