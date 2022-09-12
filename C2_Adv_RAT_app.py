# RIGHT ANGLED TRIANGLE CALCULATOR

#-------------------------------------------------------------------------------------------------------

# --- Can it give you the measurements of the other sides when given one side only ? No this will be
#  impossible due to guessing many times until it gets the right numbers

# --- Can it give you the angle you need to use once it gives you the measurements ? Yes it can by using
# the measurements to calculate the angle. SOH CAH TOA

#-------------------------------------------------------------------------------------------------------
# WE USED RANDOM IN A FUNCTION

# controlling the loop using best of 3
# controlling the loop using recursion
import random

def right_angle():
	length = random.randint(1,7)
	width = random.randint(1,7)
	hypotenuse = random.randint(1,7)
	

	total_length = int(length)**2
	total_width = int(width)**2
	total_hypotenuse = int(hypotenuse)**2

	answer = total_length + total_width
	answer_2 = total_hypotenuse - total_width

	if answer == total_hypotenuse:
		print(f"Length is: {length},Width is:{width},hypotenuse is:{hypotenuse} This is a right angle triangle")

	else:
		print(f"Length is: {length},Width is:{width},hypotenuse is:{hypotenuse} This is NOT a right angle triangle")
		return right_angle()

right_angle()