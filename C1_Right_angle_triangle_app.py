# RIGHT ANGLED TRIANGLE CALCULATOR

#-------------------------------------------------------------------------------------------------------

# --- Can it give you the measurements of the other sides when given one side only ? No this will be
#  impossible due to guessing many times until it gets the right numbers

# --- Can it give you the angle you need to use once it gives you the measurements ? Yes it can by using
# the measurements to calculate the angle. SOH CAH TOA

#-------------------------------------------------------------------------------------------------------

# CREATE AN APP THAT WILL TAKE USER INPUT TO CALCULATE A RIGHT ANGLES TRIANGLE

length = input("Enter the length: ")
width = input("Enter the width: ")
hypotenuse = input("Enter the hypotenuse: ")

#formula for right angles triangle
#a^2 + b^2 = c^2
total_length = int(length)**2
total_width = int(width)**2
total_hypotenuse = int(hypotenuse)**2

answer = total_length + total_width
answer_2 = total_hypotenuse - total_width

if answer == total_hypotenuse and answer_2 == total_length:
	print("This is a right angle triangle")
else:
	print("This is NOT  a right angle triangle")






