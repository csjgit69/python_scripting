import random

###################################################
"""
#1
Write a Python function miles_to_feet that takes a parameter miles and returns the number of feet in miles miles.
"""
# Miles to feet conversion formula
def miles_to_feet(miles):
    return miles * 5280
print ("# 1: ")
miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
expected = "13 miles equals 68640 feet."
print ("Expected output: ", expected)

print ("****")
##################################################

###################################################
"""
#2
Write a Python function total_seconds that takes three parameters hours, 
minutes and seconds and returns the total number of seconds for hours hours, minutes minutes and seconds seconds. 
"""
# Hours, minutes, and seconds to seconds conversion formula
def total_seconds(hours, minutes, seconds):
    return (hours*60*60)+(minutes*60)+seconds

print ("# 2: ")
hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " +
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) +
      " seconds.")
expected = "#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds."
print ("Expected output: ", expected)

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " +
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) +
      " seconds.")
expected = "#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds."
print ("Expected output: ", expected)

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " +
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) +
      " seconds.")
expected = "#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds."
print ("Expected output: ", expected)
print ("****")
##################################################

###################################################
"""
#3
Write a Python function rectangle_perimeter that takes two parameters width and height corresponding to the 
lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches.
"""
# Rectangle perimeter formula
def rectangle_perimeter(width,height):
    return (width*2)+(height*2)

print ("# 3: ")
width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")
expected = "A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches."
print ("Expected output: ", expected)

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")
expected = "A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches."
print ("Expected output: ", expected)

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")
expected = "A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches."
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
#4
Write a Python function rectangle_area that takes two parameters width and height corresponding to the lengths of the sides of a 
rectangle and returns the area of the rectangle in square inches.
"""
# Rectangle perimeter formula
def rectangle_area(width,height):
    return width*height

print ("# 4: ")
width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
expected = "A rectangle 4 inches wide and 7 inches high has an area of 28 square inches."
print ("Expected output: ", expected)

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
expected = "A rectangle 7 inches wide and 4 inches high has an area of 28 square inches."
print ("Expected output: ", expected)

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
expected = "A rectangle 10 inches wide and 10 inches high has an area of 100 square i"
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
#10
Write a Python function rectangle_area that takes two parameters width and height corresponding to the lengths of the sides of a 
rectangle and returns the area of the rectangle in square inches.
"""
# Rectangle perimeter formula
def point_distance(x_0, y_0, x_1, y_1):
    return (((x_0-x_1)**2) + ((y_0-y_1)**2))**0.5

print ("# 10: ")
x_0, y_0, x_1, y_1 = 2, 2, 5, 6
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" +
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")
expected = "The distance from (2, 2) to (5, 6) is 5.0."
print ("Expected output: ", expected)

x_0, y_0, x_1, y_1 = 1, 1, 2, 2
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" +
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")
expected = "The distance from (1, 1) to (2, 2) is 1.41421356237."
print ("Expected output: ", expected)

x_0, y_0, x_1, y_1 = 0, 0, 3, 4
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" +
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")
expected = "The distance from (0, 0) to (3, 4) is 5.0."
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
#11
Challenge: Write a Python function triangle_area that takes the parameters x_0, y_0, x_1,y_1, x_2, and y_2 (all numbers), 
and returns the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). 
(Hint: use the function point_distance as a helper function and apply Heron's formula.) 
"""
# Rectangle perimeter formula
def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    len_a = point_distance(x_0,y_0,x_1,y_1)
    len_b = point_distance(x_1,y_1,x_2,y_2)
    len_c = point_distance(x_2,y_2,x_0,y_0)
    semi_prem = 0.5 * (len_a + len_b + len_c)
    area = (semi_prem * (semi_prem - len_a) * (semi_prem - len_b) * (semi_prem - len_c)) ** 0.5
    # print(">>>",len_a, len_b, len_c, semi_prem, area)
    return area

def test(x_0, y_0, x_1, y_1, x_2, y_2):
    """Tests the triangle_area function."""
    print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + "),")
    print("(" + str(x_1) + "," + str(y_1) + "), and")
    print("(" + str(x_2) + "," + str(y_2) + ") has an area of")
    print(str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

print ("# 11: ")
x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" +
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) +
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")
expected = "A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5."
print ("Expected output: ", expected)

x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" +
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) +
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")
expected = "A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5."
print ("Expected output: ", expected)

x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" +
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) +
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")
expected = "A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50."
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
#12
Write a Python function print_digits that takes an integer number in the range [0,100), 
(i.e., at least 0, but less than 100) and prints the message "The tens digit is %, and the ones digit is %.", 
where the percent signs should be replaced with the appropriate values. 
(Hint: Use the arithmetic operators for integer division // and remainder % to find the two digits. 
Note that this function should print the desired message, rather than returning it as a string."""
# Rectangle perimeter formula
def print_digits(num):
    tens = (num // 10) % 10
    ones = num % 10
    print("The tens digit is {}, and the ones digit is {}.".format(tens,ones))
    return 0

print ("# 12: ")
print_digits(42)
expected = "Expected 4, 2."
print ("Expected output: ", expected)

print_digits(99)
expected = "Expected 9, 9."
print ("Expected output: ", expected)

print_digits(5)
expected = "Expected 0, 5."

print ("****")
###################################################

###################################################
"""
#13
Challenge:Powerball is lottery game in which 6 numbers are drawn at random. 
Players can purchase a lottery ticket with a specific number combination and, 
if the number on the ticket matches the numbers generated in a random drawing, the player wins a massive jackpot. 
Write a Python function powerball that takes no arguments and prints the message "Today's numbers are %, %, %, %, and %. 
The Powerball number is %.". The first five numbers should be random integers in the range [1,60), i.e., at least 1, but less than 60. 
In reality, these five numbers must all be distinct, but for this problem, we will allow duplicates. 
The Powerball number is a random integer in the range [1,36), i.e., at least 1 but less than 36. 
Note that this function should print the desired message, rather than returning it as a string.
"""
# Rectangle perimeter formula
def powerball():
    d1 = random.randrange(1,60)
    d2 = random.randrange(1,60)
    d3 = random.randrange(1,60)
    d4 = random.randrange(1,60)
    d5 = random.randrange(1,60)
    d6 = random.randrange(1,60)
    print("Today's numbers are {}, {}, {}, {}, and  {}. The Powerball number is {}.".format(d1,d2,d3,d4,d5,d6))
    return 0

print ("# 12: ")

powerball()
powerball()
powerball()
expected = "Expected 0, 5."

print ("****")
###################################################


def q5 (x):
    
    return -5*(x**5)+67*(x**2)-47

print("Q5 0:",q5(0))
print("Q5 1:",q5(1))
print("Q5 2:",q5(2))
print("Q5 3:",q5(3))


def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    FV=PV(1+rate)^periods
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    future_value = present_value * ((1+rate_per_period)**periods)
    return future_value

print("$1000 at 2% compounded daily for 4 years yields $", future_value(500, .04, 10, 10))
print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))

def elt_area (side):
    s1 = side**2
    v1 = (3**0.5)

    return (v1*s1)/4

print("equilateral triangle area:",elt_area(2))
print("equilateral triangle area:",elt_area(5))