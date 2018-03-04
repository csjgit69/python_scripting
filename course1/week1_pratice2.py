###################################################
"""
#1
Given a template that pre-defines a variable 𝚖𝚒𝚕𝚎𝚜,
write an assignment statement that defines a variable 𝚏𝚎𝚎𝚝 whose value is the number of feet in 𝚖𝚒𝚕𝚎𝚜 miles.
# Compute the number of feet corresponding to a number of miles.
"""
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1
# miles = 13
# expected = 68640

# Test 2
# miles = 57
# expected = 300960

# Test 3
miles = 82.67
expected = 436497.6

# Test output
feet = miles * 5280
print ("# 1: ")
# Student should not change this code.
print(str(miles) + " miles equals " + str(feet) + " feet.")
print ("Expected output: ", expected)
print ("****")

##################################################

###################################################
"""
#2
Given a template that pre-defines three variables 𝚑𝚘𝚞𝚛𝚜, 𝚖𝚒𝚗𝚞𝚝𝚎𝚜 and 𝚜𝚎𝚌𝚘𝚗𝚍𝚜, 
write an assignment statement that updates the variable 𝚝𝚘𝚝𝚊𝚕_𝚜𝚎𝚌𝚘𝚗𝚍𝚜 to have a value corresponding 
to the total number of seconds for 𝚑𝚘𝚞𝚛𝚜 hours, 𝚖𝚒𝚗𝚞𝚝𝚎𝚜 minutes and 𝚜𝚎𝚌𝚘𝚗𝚍𝚜 seconds.
"""

# Test 1
# hours = 7
# minutes = 21
# seconds = 37
# expected = 26497

# Test 2
# hours = 10
# minutes = 1
# seconds = 7
# expected = 36067

# Test 3
hours = 1
minutes = 0
seconds = 1
expected = 3601

total_seconds = (hours*60*60)+(minutes*60)+seconds
###################################################
# Test output
print ("# 2: ")
# Student should not change this code.
print(str(hours) + " hours, " + str(minutes) + " minutes, and " +
      str(seconds) + " seconds totals to " + str(total_seconds) + " seconds.")
print ("Expected output: ", expected)
print ("****")

###################################################

###################################################
"""
# 3
Given a template that pre-defines the variables 𝚠𝚒𝚍𝚝𝚑 and 𝚑𝚎𝚒𝚐𝚑𝚝 that are the lengths of the sides of a rectangle, 
write an assignment statement that defines a variable 𝚙𝚎𝚛𝚒𝚖𝚎𝚝𝚎𝚛 whose value is the perimeter of the rectangle in inches.
"""
# Test 1
# width = 4
# height = 7
# expected = 22

# Test 2
# width = 7
# height = 4
# expected = 22

# Test 3
width = 10
height = 10
expected = 40

perimeter = width*height

print ("# 3: ")
# Student should look at the following comments and compare to printed output.
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has a perimeter of " + str(perimeter) + " inches.")
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
# 4
Given a template that pre-defines the variables 𝚠𝚒𝚍𝚝𝚑 and 𝚑𝚎𝚒𝚐𝚑𝚝 that are the lengths of the sides of a rectangle, 
write an assignment statement that defines a variable 𝚊𝚛𝚎𝚊 whose value is the area of the rectangle in square inches.
"""
# Test 1
# width = 4
# height = 7
# expected = 28

# Test 2
# width = 7
# height = 4
# expected = 28

# Test 3
width = 10
height = 10
expected = 100

area = width * height

print ("# 4: ")
# Student should not change this code.
print("A rectangle " + str(width) + " inches wide and " + str(height) +
      " inches high has an area of " + str(area) + " square inches.")
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
# 5
Given a template that pre-defines the constant 𝙿𝙸 and the variable 𝚛𝚊𝚍𝚒𝚞𝚜 corresponding to the radius of a circle in inches, 
write an assignment statement that defines a variable 𝚌𝚒𝚛𝚌𝚞𝚖𝚏𝚎𝚛𝚎𝚗𝚌𝚎 whose value is the circumference of a circle 
with radius 𝚛𝚊𝚍𝚒𝚞𝚜 in inches
"""
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1
# radius = 8
# expected = 50.24

# Test 2
# radius = 3
# expected = 18.84

# Test 3
radius = 12.9
expected = 81.012

circumference = 2 * PI * radius

print ("# 5: ")
# Student should not change this code.
print("A circle with a radius of " + str(radius) +
      "inches has a circumference of " + str(circumference) + " inches.")
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
# 6
Given a template that pre-defines the constant 𝙿𝙸 and the variable 𝚛𝚊𝚍𝚒𝚞𝚜 corresponding to the radius of a circle in inches, 
write an assignment statement that defines a variable 𝚊𝚛𝚎𝚊 whose value is the area of a circle with radius 𝚛𝚊𝚍𝚒𝚞𝚜 in square inches.
"""
PI = 3.14

# Test 1
# radius = 8
# expected = 200.96

# Test 2
# radius = 3
# expected = 28.26

# Test 3
radius = 12.9
expected = 522.5274

area = PI*(radius**2)

print ("# 6: ")
# Student should enter formula on the next line.
print("A circle with a radius of " + str(radius) +
      " inches has an area of " + str(area) + " square inches.")
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
# 7
Given the pre-defined variables 𝚙𝚛𝚎𝚜𝚎𝚗𝚝_𝚟𝚊𝚕𝚞𝚎, 𝚊𝚗𝚗𝚞𝚊𝚕_𝚛𝚊𝚝𝚎 and 𝚢𝚎𝚊𝚛𝚜, 
write an assignment statement that define a variable 𝚏𝚞𝚝𝚞𝚛𝚎_𝚟𝚊𝚕𝚞𝚎 whose value is 𝚙𝚛𝚎𝚜𝚎𝚗𝚝_𝚟𝚊𝚕𝚞𝚎 dollars 
invested at 𝚊𝚗𝚗𝚞𝚊𝚕_𝚛𝚊𝚝𝚎 percent interest, compounded annually for 𝚢𝚎𝚊𝚛𝚜 years.
"""
# Test 1
# present_value = 1000
# annual_rate = 7
# years = 10
# expected = 1967.15135729

# Test 2
# present_value = 200
# annual_rate = 4
# years = 5
# expected = 243.33058048

# Test 3
present_value = 1000
annual_rate = 3
years = 20
expected = 1806.11123467

future_value = present_value * ((1+(0.01*annual_rate))**years)

print ("# 7: ")
# Student should enter formula on the next line.
print("The future value of $" + str(present_value) + " in " + str(years) +
      "years at an annual rate of " + str(annual_rate) + "% is $" + str(future_value) + ".")
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
#8
Give the pre-defined variables 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚕𝚊𝚜𝚝_𝚗𝚊𝚖𝚎, 
write an assignment statement that defines the variable 𝚗𝚊𝚖𝚎_𝚝𝚊𝚐 whose value is the string "My name is % %." 
where the percents should be replaced by 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 and 𝚕𝚊𝚜𝚝_𝚗𝚊𝚖𝚎. 
Remember that, in Python, you can use the + operator on strings to concatenate (i.e. join) them together into a single string.
"""
# Test 1
# first_name = "Joe"
# last_name = "Warren"
# expected = "My name is Joe Warren."

# Test 2
# first_name = "Scott"
# last_name = "Rixner"
# expected = "My name is Scott Rixner."

# Test 3
first_name = "John"
last_name = "Greiner"
expected = "My name is John Greiner."

name_tag = "My name is " + first_name + " " + last_name + "."

print ("# 8: ")
# Student should not change this code.
print(name_tag)
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
#9
Given the pre-defined variables 𝚗𝚊𝚖𝚎 (a string) and 𝚊𝚐𝚎 (a number), 
write an assignment statement that defines a variable 𝚜𝚝𝚊𝚝𝚎𝚖𝚎𝚗𝚝 whose value is the string "% 𝚒𝚜 % 𝚢𝚎𝚊𝚛𝚜 𝚘𝚕𝚍." 
where the percents should be replaced by 𝚗𝚊𝚖𝚎 and the string form of 𝚊𝚐𝚎.
"""
# Test 1
# name = "Joe Warren"
# age = 56
# expected = "Joe Warren is 56 years old."

# Test 2
# name = "Scott Rixner"
# age = 40
# expected = "Scott Rixner is 40 years old."

# Test 3
name = "John Greiner"
age = 46
expected = "John Greiner is 46 years old."

statement = name + " is " + str(age) + " years old."

print ("# 9: ")
# Student should not change this code.
print(statement)
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
# 10
Challenge: Given the variables 𝚡_𝟶, 𝚢_𝟶, 𝚡_𝟷, and 𝚢_𝟷, 
write an assignment statement that defines a variable 𝚍𝚒𝚜𝚝𝚊𝚗𝚌𝚎 whose values is the distance between the points (x0,y0) and (x1,y1).
"""
# Test 1
# x_0 = 2
# y_0 = 2
# x_1 = 5
# y_1 = 6
# expected = 5.0

# Test 2
# x_0 = 1
# y_0 = 1
# x_1 = 2
# y_1 = 2
# expected = 1.41421356237

# Test 3
x_0 = 0
y_0 = 0
x_1 = 3
y_1 = 4
expected = 5.0

distance = (((x_0-x_1)**2) + ((y_0-y_1)**2))**0.5

print ("# 10: ")
# Student should not change this code.
print("The distance from (" + str(x_0) + ", " + str(y_0) +
      ") to (" + str(x_1) + ", " + str(y_1) + ") is " + str(distance) + ".")
print ("Expected output: ", expected)
print ("****")
###################################################

###################################################
"""
# 11
Challenge:Heron's formula states the area of a triangle is
 sqrt(s(s−a)(s−b)(s−c)) where a, b and c are the lengths of the sides of the triangle 
 and s=1/2(a+b+c) is the semi-perimeter of the triangle. 
 Given the variables 𝚡_𝟶, 𝚢_𝟶, 𝚡_𝟷, 𝚢_𝟷, 𝚡_𝟸, and 𝚢_𝟸, write a Python program that computes a variable 𝚊𝚛𝚎𝚊 
 whose value is the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). 
 (Hint: our solution uses five assignment statements.) 
"""
# Test 1
# x_0, y_0 = 0, 0
# x_1, y_1 = 3, 4
# x_2, y_2 = 1, 1
# expected = 0.5

# Test 2
# x_0, y_0 = -2, 4
# x_1, y_1 = 1, 6
# x_2, y_2 = 2, 1
# expected = 8.5

# Test 3
x_0, y_0 = 10, 0
x_1, y_1 = 0, 0
x_2, y_2 = 0, 10
expected = 50.0

len_a = (((x_0-x_1)**2) + ((y_0-y_1)**2))**0.5
len_b = (((x_1-x_2)**2) + ((y_1-y_2)**2))**0.5
len_c = (((x_2-x_0)**2) + ((y_2-y_0)**2))**0.5
semi_prem = 0.5 * (len_a + len_b + len_c)
area = (semi_prem * (semi_prem - len_a) * (semi_prem - len_b) * (semi_prem - len_c) )**0.5

print ("# 11: ")
# Student should not change this code.
print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + ")," +
      "(" + str(x_1) + "," + str(y_1) + "), and" +
      "(" + str(x_2) + "," + str(y_2) + ") has an area of " + str(area) + ".")
print ("Expected output: ", expected)
print ("****")

s = 0.035274

print(1/s)
#(𝟾 + (𝟷 + (𝟸 * 𝟺) - 𝟹))
###################################################
