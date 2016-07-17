number = int(input("Enter a number: "))

def fizz_buzz(number):
	'''Returns 'FizzBuzz' if a number is divisible by both 3 and 5.
	returns 'Fizz' if number is divisible by 3
	returns 'Buzz' if its divisible by 5 
	returns the number if its not divisible by 3 or 5		
	'''

	if number % 3 == 0 and number % 5 == 0:		
		return "FizzBuzz"
	elif number % 3 == 0:
		return "Fizz"
	elif number % 5 == 0:
		return "Buzz"
	else:
		return number	
		
	