import operator

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
	print("Remove Letter")
	base_string = str(raw_input("Enter String: "))
	letter_to_remove = str(raw_input("Enter the letter to remove from the String: " ))
	letter_to_remove = letter_to_remove[0]
	string_length = len(base_string)
	location = 0
	
	
	while (location < string_length): #by reference rather than by value
		if base_string[location] == letter_to_remove:
			base_string = base_string[:location] + base_string[location+1::]
			string_length -= 1
		location += 1
			
	print "Result: %s" % base_string
	return

def num_compare(): #Compare 2 numbers to determine the larger
	num1 = int(input("First Number: "))
	num2 = int(input("Second Number: "))
	if (num1 > num2):
		print ("%d is larger" % num1)
	elif (num2 > num1):
		print ("%d is larger" % num2)
	else:
		print "Equal"
	return

def print_string(): #Print the previously stored string
	print (saved_string)
	return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
	print ("Calculator")
	num1 = int(raw_input("Enter the 1st #: "))
	sign = str(raw_input("Enter the action: "))
	num2 = int(raw_input("Enter the 2nd #: "))
	if (sign == '+'):
		print num1 + num2
	if (sign == '-'):
		print num1 - num2
	if (sign == '*'):
		print num1 * num2
	if (sign == '/'):
		print num1 / num2
	return

def accept_and_store(): #Accept and store a string
	global saved_string
	saved_string = str(raw_input("Input String: "))
	return

def main(): #menu goes here
	opt_list = [accept_and_store, 
				calculator, 
				print_string, 
				num_compare, 
				remove_letter]

	while(True):
		print ("Select Option")
		print ("1\t Accept and Store")
		print ("2\t Calculator")
		print ("3\t Print String")
		print ("4\t Number Comparison")
		print ("5\t Remove Letter")

		option_chosen = int(input("Selection: "))
		option_chosen -= 1
		opt_list[option_chosen]()

	return

main()

