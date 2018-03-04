###################################################
"""
#1
Template - Compute the number of feet corresponding to a number of miles.
There are 5280 feet in a mile.
Write a Python statement that calculates and prints the number of feet in 13 miles.
Expected output 68640
"""
miles = 13
feetPmile = 5280
feet = miles * feetPmile
print ("# 1: ")
print ("there are ", feet, " in "+ str(miles) + " miles ")
print ("Expected output: 68640")
print ("****")
##################################################

###################################################
"""
#2
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
Hours, minutes, and seconds to seconds conversion formula
Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds. 
Expected output 26497
"""
hours = 7
minutes = 21 + (hours * 60)
seconds = 37 + (minutes * 60)

print ("# 2: ")
print ("total seconds equals", seconds)
print ("Expected output: 26497")
print ("****")
###################################################


###################################################
"""
# 3
Template - Compute the length of a rectangle's perimeter, given its width and height.
Rectangle perimeter formula
The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its sides. 
Write a Python statement that calculates and prints the length in inches of the perimeter of a rectangle with sides of length 4 and 7 inches. 
Expected output 22
"""
width = 4
height = 7
perimeter = (2*width) + (2 * height)
print ("# 3: ")
print ("The perimeter is: ", perimeter)
print ("Expected output: 22")
print ("****")
###################################################


###################################################
"""
# 4
Template - Compute the area of a rectangle, given its width and height.
Rectangle area formula
The area of a rectangle is wh, where w and h are the lengths of its sides. 
Note that the multiplication operation is not shown explicitly in this formula. 
This is standard practice in mathematics, but not in programming. 
Write a Python statement that calculates and prints the area in square inches of a rectangle with sides of length 4 and 7 inches.
Expected output 28
"""
width = 4
height = 7
area = width * height
print ("# 4: ")
print ("The area is: ", area)
print ("Expected output 28")
print ("****")
###################################################

###################################################
"""
# 5
Compute the circumference of a circle, given the length of its radius.
Circle circumference formula
The circumference of a circle is 2πr where r is the radius of the circle. 
Write a Python statement that calculates and prints the circumference in inches of a circle whose radius is 8 inches. 
Assume that the constant π=3.14. 
Expected output 50.24
"""
pie = 3.14
radius = 8
circumference = 2*pie*radius
print ("# 5: ")
print ("The circumference is: ", circumference)
print ("Expected output 50.24")
print ("****")
###################################################


###################################################
"""
# 6
Template - Compute the area of a circle, given the length of its radius.
Circle area formula
The area of a circle is πr^2 where r is the radius of the circle. (The raised 2 in the formula is an exponent.) 
Write a Python statement that calculates and prints the area in square inches of a circle whose radius is 8 inches. 
Assume that the constant π=3.14.
Expected output 200.96
"""
pie = 3.14
radius = 8
area = pie*(radius**2)
print ("# 6: ")
print ("Area of the circle is: ", area)
print ("Expected output: 200.96")
print ("****")
###################################################

###################################################
"""
# 7
Template - Compute the future value of a given present value, annual rate, and number of years.
Future value formula
Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest for y years is p(1 + 0.01r)^y. 
(Remember that you don't need to understand how this formula works, only how to translate it into Python.) 
Write a Python statement that calculates and prints the value of 1000 dollars compounded at 7 percent interest for 10 years.
Expected output: 1967.15135729
"""
principle = 1000
rate = 7
time = 10
value = principle * ((1+(0.01*rate))**time)
print ("# 7: ")
print ("The value after 10 years is: ", value)
print ("Expected output: 1967.15135729")
print ("****")
###################################################

###################################################
"""
# 8
Template - Compute a name tag, given the first and last name.
Name tag formula
Write a single Python statement that combines the three strings "𝙼𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜", "𝙹𝚘𝚎" and "𝚆𝚊𝚛𝚛𝚎𝚗" 
(plus a couple of other small strings) into one larger string "𝙼𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜 𝙹𝚘𝚎 𝚆𝚊𝚛𝚛𝚎𝚗." and prints the result. 
(Hint: Experiment with adding two strings in Python using the + operator.)
Expected output: My name is Joe Warren.
"""
str1 = "My name is"
str2 = "Joe"
str3 = "Warren"
print ("# 8: ")
print (str1,  str2 +" "+ str3 + ".")
print ("Expected output: My name is Joe Warren.")
print ("****")
###################################################

###################################################
"""
# 9
Template - Compute the statement about a person's name and age, given the person's name and age.
Name and age formula
Write a Python expression that creates the string "𝙹𝚘𝚎 𝚆𝚊𝚛𝚛𝚎𝚗 𝚒𝚜 𝟻𝟼 𝚢𝚎𝚊𝚛𝚜 𝚘𝚕𝚍." 
from several strings including "𝙹𝚘𝚎 𝚆𝚊𝚛𝚛𝚎𝚗" and the number 56 and then prints the result 
(Hint: Use the function 𝚜𝚝𝚛 to convert the number into a string.)
Expected output Joe Warren is 56 years old.
"""
str1 = "Joe Warren"

print ("# 9: ")
print (str1 + " is " + str(56) + " years old.")
print ("Expected output: Joe Warren is 56 years old.")
print ("****")
###################################################

###################################################

"""
# 10
Template - Compute the distance between the points (x0, y0) and (x1, y1).
Distance formula
Challenge: The distance between two points (x0,y0) and (x1,y1) is sqr((x0−x1)^2+(y0−y1)^2) 
Write a Python statement that calculates and prints the distance between the points (2,2) and (5,6). 
(Hint: Remember that a square root can be computed by raising a value to the 0.5 power.)
# Hint: You need to use the power operation ** .
Expected output 5.0
"""
x0 = 2
x1 = 5
y0 = 2
y1 = 6
distance = (((x0-x1)**2) + ((y0-y1)**2))**0.5
print ("# 10: ")
print ("The distance is: ", distance)
print ("Expected output 5.0")
print ("****")
###################################################
