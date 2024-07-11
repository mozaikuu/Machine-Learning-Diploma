#Example 1:
# Print the sum of 4 + 5.
# Print the result of subtracting 5 from 5.
# Multiply 3 by 5.
# Divide 10 by 2.
#///////////////////////////////////////////////////////////////
# Addition
print(4 + 5)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)

# Division
print(10 / 2)
# *********************************************************************************************************
# Example 2:
# Create a variable savings with the value of 100.
# Check out this variable by typing print(savings) in the script.
# ////////////////////////////////////////////////////////////////////////////////////////
# Create a variable savings
savings = 100

# Print out savings
print(type(savings))

# *************************************************************************************************************

#Example 3:
# Create a variable monthly_savings, equal to 10 and num_months, equal to 4.
# Multiply monthly_savings by num_months and save it to new_savings.
# Add new_savings to savings, saving the sum as total_savings.
# Print the value of total_savings.
#///////////////////////////////////////////////////////////////////////////
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Add new_savings to your savings
total_savings = savings + new_savings

# Print total_savings
print(total_savings)




#****************************************************************************************************************

#Example 4:
# Create a new float, half, with the value 0.5.
# Create a new string, intro, with the value "Hello! How are you?".
# Create a new boolean, is_good, with the value True.
#////////////////////////////////////////////////////////////////////
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True


#*******************************************************************************************************************

#Example 5:
# monthly_savings = 10
# num_months = 12
# intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
# Print the type of year_savings
# Assign sum of intro and intro to doubleintro
# Print out doubleintro
#////////////////////////////////////////////////////////////////////
monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings * num_months

# Print the type of year_savings
print(type(year_savings))

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)
#*******************************************************************************************************************

#Example 6:
# Definition of savings and total_savings
# savings = 100
# total_savings = 150
# # Fix the printout
# print("I started with $" + savings + " and now have $" + total_savings + ". Awesome!")
# # Definition of pi_string
# pi_string = "3.1415926"
# # Convert pi_string into float: pi_float
#/////////////////////////////////////////////////////////////////////////////////////////////
# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + 
      " and now have $" + str(total_savings) + 
      ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

#*******************************************************************************************************************

#Example 7:
# area variables (in square meters)
# hall = 11.25
# kit = 18.0
# liv = 20.0
# bed = 10.75
# bath = 9.50
# Create list areas
# Print areas
#//////////////////////////////////////////////////
# Area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
#*****************************************************************************************************************

#Example 8:
# Finish the code that creates the areas list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
# Print areas again; is the printout more informative this time?
# area variables (in square meters)
# hall = 11.25
# kit = 18.0
# liv = 20.0
# bed = 10.75
# bath = 9.50
# Adapt list areas
# areas = [hall, kit, "living room", liv, bed, "bathroom", bath]
# Print areas
#/////////////////////////////////////////////////////////////////////////
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, 
         "living room", liv, "bedroom", bed, 
         "bathroom", bath]

# Print areas
print(areas)
#**************************************************************************************************************

#Example 9:
# Can you tell which ones of the following lines of Python code are valid ways to build a list?
# A. [1, 3, 4, 2] B. [[1, 2, 3], [4, 5, 7]] C. [1 + 2, "a" * 5, 3]
# @possible_answers
# A, B and C =====> this is the correct answer
# B
# B and C
# C


#************************************************************************************************************

#Example 10:
# area variables (in square meters)
# hall = 11.25
# kit = 18.0
# liv = 20.0
# bed = 10.75
# bath = 9.50
# house information as list of lists
# house = 
# Print out house
# Print out the type of house
#///////////////////////////////////////////////////////////////////////////////
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

#****************************************************************************************************************

#Example 11:
# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Print out second element from areas
# print(areas[_])
# Print out last element from areas
# print(areas[__])
# Print out the area of the living room
# print(areas[_])
#//////////////////////////////////////////////////////////////////////////////////////////////////////
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

#***************************************************************************************************************

#Example 12:
# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Sum of kitchen and bedroom area: eat_sleep_area
# Print the variable eat_sleep_area
#////////////////////////////////////////////////////////////////////////////////////////////////////
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)
#**************************************************************************************************************

#Example 13:
# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
# Use slicing to create upstairs
# Print out downstairs and upstairs
#/////////////////////////////////////////////////////////////////////////////////////////////////
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
#*******************************************************************************************************************

#Example 14:
# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Alternative slicing to create downstairs
# Alternative slicing to create upstairs
#////////////////////////////////////////////////////////////////////////////////
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]

#*******************************************************************************************************************
#Example 15:

# house = [["hallway", 11.25],
#          ["kitchen", 18.0],
#          ["living room", 20.0],
#          ["bedroom", 10.75],
#          ["bathroom", 9.50]]
# What will house[-1][1] return? house, the list of lists that you created before, is already defined for you in the workspace. You can experiment with it in the IPython Shell.

# @possible_answers

# A float: the kitchen area
# A string: "kitchen"
# A float: the bathroom area ====>this is the correct answer
# A string: "bathroom"

#*******************************************************************************************************************

#Example 16:
# Create the areas list
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Correct the bathroom area(Update the area of the bathroom area to be 10.50 square meters instead of 9.50.)
# Change "living room" to "chill zone"
#//////////////////////////////////////////////////////////////////////////////
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

#******************************************************************************************************************

#Example 17:

# Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
# Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.

# Create the areas list and make some changes
# areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
#          "bedroom", 10.75, "bathroom", 10.50]
# Add poolhouse data to areas, new list is areas_1
# Add garage data to areas_1, new list is areas_2
#//////////////////////////////////////////////////////////
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
#***************************************************************************************************************

#Example 18:

# Remove the corresponding string(poolhouse) and its float from the areas list.
# areas = ["hallway", 11.25, "kitchen", 18.0,
#         "chill zone", 20.0, "bedroom", 10.75,
#          "bathroom", 10.50, "poolhouse", 24.5,
#          "garage", 15.45]
# Which of the code chunks will do the job for us?

# @possible_answers

# del(areas[10]); del(areas[11])
# del(areas[10:11])
# del(areas[-4:-2]) ======> this is the correct answer
# del(areas[-3]); del(areas[-4])

#************************************************************************************************************

#Example 19:

# Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy from areas
# Change the first item in areas_copy = 5
# Print areas and areas_copy
#////////////////////////////////////////////
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
#************************************************************************************************************
#Example 20:
# Create variables var1 and var2
# var1 = [1, 2, 3, 4]
# var2 = True
# Print out type of var1
# Print out length of var1
# Convert var2 to an integer: out2
#//////////////////////////////////////////////////
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
#****************************************************************************************************************

#Example 21:
# Create lists first and second
# first = [11.25, 18.0, 20.0]
# second = [10.75, 9.50]
# Paste together first and second: full
# Sort full in descending order: full_sorted
# Print out full_sorted
#////////////////////////////////////////////////////
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
#*************************************************************************************************************

#Example 22:

# string to experiment with: place
# place = "poolhouse"
# Use upper() on place: place_up
# Print out place and place_up
# Print out the number of o's in place
# Print out the number of o's in place_up
#////////////////////////////////////////////////
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
#***************************************************************************************************************

#Example 23:
# Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
# Print out how often 9.50 appears in areas
#////////////////////////////////////////////
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
#*****************************************************************************************************************

#Example 24:
# Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size: : 24.5 and 15.45
# Print out areas
# Reverse the orders of the elements in areas
# Print out areas
#//////////////////////////////////////////////////////////////////////////////
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
#******************************************************************************************************************

#Example 25:

# Import the math package
# Definition of radius
# r = 0.43
# Calculate Circumference as C
# Calculate Area as A
# Build printout
# print("Circumference: ")
# print("Area: " )
# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
#***************************************************************************************************************

#Example 26:

# Import radians function of math package
# Definition of radius
# r = 192500
# Travel distance of Moon over 12 degrees. Store in dist.
# Print out dist
#////////////////////////////////////////////////////////
# Import radians function of math package
from math import radians

# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)
#**************************************************************************************************************

#Example 27:

# Import the numpy package as np
# Create list baseball
# baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Create a numpy array from baseball: np_baseball
# Print out type of np_baseball
#////////////////////////////////////////
# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a NumPy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
#*************************************************************************************************************

#Example 28:
# declare constants 
# PI = 3.14
# GRAVITY = 9.8
# import constant file we created above
# print pi and gravity
#///////////////////////////////////
# import constant file we created above
import constant

print(constant.PI) # prints 3.14
print(constant.GRAVITY) # prints 9.8
#************************************************************************************************************

#Example 29:
# Calculate the Area of a Triangle
# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

#*********************************************************************
#Example 30:
# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
 
#///////////////////////////////////////////
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)



#*******************************************************************
#Example 31:
# Check if a Number is Positive, Negative or 0
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
#*****************************************************************************************

#Example 32:
# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

#*******************************************************************************************
#Example 33:
# Check Prime Number "num = 407"
num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

#***************************************************************************
#Example 34:
# Make a Simple Calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")


#****************************************************************************
#Example 35:
# Display Calendar of the given month and year
# Program to display calendar of the given month and year

# importing calendar module
import calendar

# yy = 2014  # year
# mm = 11    # month

# To take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

#****************************************************