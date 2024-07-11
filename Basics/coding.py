#Example 1:
# Print the sum of 4 + 5.
# Print the result of subtracting 5 from 5.
# Multiply 3 by 5.
# Divide 10 by 2.
# *******************************
# Addition
print(4+5)

# Subtraction
print(5-5)

# Multiplication
print(3*5)

# Division
print(10/2)

# *********************************************************************************************************
# Example 2:
# Create a variable savings with the value of 100.
# Check out this variable by typing print(savings) in the script.
# ****************************************************************************
# Create a variable savings
savings = 100

# Print out savings
print(savings)


# *************************************************************************************************************

#Example 3:
# Create a variable monthly_savings, 
#equal to 10 and num_months, equal to 4.
# Multiply monthly_savings by num_months 
#and save it to new_savings.
# Add new_savings to savings, saving the sum as 
#total_savings.
# Print the value of total_savings.
monthly_savings = 10
num_months = 4
new_savings = monthly_savings * num_months
total_savings = savings + new_savings
print(total_savings)


#****************************************************************************************************************

#Example 4:
# Create a new float, half, with the value 0.5.
# Create a new string, intro, 
#with the value "Hello! How are you?".
# Create a new boolean, is_good, 
#with the value True.
half = 0.5
intro = "Hello! How are you?"
is_good = True

#*******************************************************************************************************************

#Example 5:
monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings 
#and num_months
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
savings = 100
total_savings = 150
# # Fix the printout
# print("I started with $" + savings + 
# " and now have $" + total_savings + ". Awesome!")
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")
# # Definition of pi_string
pi_string = "3.1415926"
# # Convert pi_string into float: pi_float
pi_float = float(pi_string)

#*******************************************************************************************************************

#Example 7:
# area variables (in square meters)
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
# Finish the code that creates the areas list. 
#Build the list so that the list first contains 
#the name of each room as a string and then its 
#area. In other words, add the strings "hallway",
# "kitchen" and "bedroom" at the appropriate 
#locations.
# Print areas again; is the printout more 
#informative this time?
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
# Print areas
print(areas)

#**************************************************************************************************************

#Example 9:
# Can you tell which ones of the following lines
# of Python code are valid ways to build a list?
# A. [1, 3, 4, 2] B. [[1, 2, 3], [4, 5, 7]] 
# C. [1 + 2, "a" * 5, 3]
# @possible_answers
# A, B and C
# B
# B and C
# C

# answer
# A, B and C


#************************************************************************************************************

#Example 10:
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# house information as list of lists
house = [["hallway", hall], ["kitchen", kit], ["living room", liv], ["bedroom", bed], ["bathroom", bath]]
# Print out house
print(house)
# Print out the type of house
print(type(house))


#****************************************************************************************************************

#Example 11:
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
areas = ["hallway", 11.25, "kitchen",
18.0, "living room", 20.0, "bedroom", 
10.75, "bathroom", 9.50]
# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]
# Print the variable eat_sleep_area
print(eat_sleep_area)

#**************************************************************************************************************

#Example 13:
# Create the areas list
#Use slicing to create a list, downstairs, 
# that contains the first 6 elements of areas.
# Do a similar thing to create a new variable, 
# upstairs, that contains the last 4 elements of 
# areas.
# Print both downstairs and upstairs using print()
areas = ["hallway", 11.25, "kitchen", 
18.0, "living room", 20.0, "bedroom", 
10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs = areas[:6]
# Use slicing to create upstairs
upstairs = areas[6:]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

#*******************************************************************************************************************

#Example 14:
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, 
"living room", 20.0, "bedroom", 10.75, 
"bathroom", 9.50]
# Alternative slicing to create downstairs

# Alternative slicing to create upstairs


#*******************************************************************************************************************
#Example 15:

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
# What will house[-1][1] return? house, 
# the list of lists that you created before,
#  is already defined for you in the workspace. 
# You can experiment with it in the IPython Shell.

# @possible_answers

# A float: the kitchen area
# A string: "kitchen"
# A float: the bathroom area
# A string: "bathroom"

#*******************************************************************************************************************

#Example 16:
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, 
"living room", 20.0, "bedroom", 10.75, 
"bathroom", 9.50]
# Correct the bathroom area(Update the area of 
# the bathroom area to be 10.50 square meters
#  instead of 9.50.)
# Change "living room" to "chill zone"

#******************************************************************************************************************

#Example 17:

# Use the + operator to paste the list 
# ["poolhouse", 24.5] to the end of the areas list. 
# Store the resulting list as areas_1.
# Further extend areas_1 by adding data 
# on your garage. Add the string "garage" 
# and float 15.45. Name the resulting list 
# areas_2.

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, 
"chill zone", 20.0,
"bedroom", 10.75, "bathroom", 10.50]
# Add poolhouse data to areas, new list is areas_1
# Add garage data to areas_1, new list is areas_2

#***************************************************************************************************************

#Example 18:

# Remove the corresponding string(poolhouse) and 
# its float from the areas list.
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
# Which of the code chunks will do the job for us?

# @possible_answers

# del(areas[10]); del(areas[11])
# del(areas[10:11])
# del(areas[-4:-2])
# del(areas[-3]); del(areas[-4])

#************************************************************************************************************

#Example 19:

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy from areas

# Change the first item in areas_copy = 5

# Print areas and areas_copy

#************************************************************************************************************
#Example 20:
# Create variables var1 and var2
# var1 = [1, 2, 3, 4]
# var2 = True
# Print out type of var1
# Print out length of var1
# Convert var2 to an integer: out2

#****************************************************************************************************************

#Example 21:
# Create lists first and second
# first = [11.25, 18.0, 20.0]
# second = [10.75, 9.50]
# Paste together first and second: full
# Sort full in descending order: full_sorted
# Print out full_sorted

#*************************************************************************************************************

#Example 22:

# string to experiment with: place
# place = "poolhouse"
# Use upper() on place: place_up
# Print out place and place_up
# Print out the number of o's in place
# Print out the number of o's in place_up

#***************************************************************************************************************

#Example 23:
# Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
# Print out how often 9.50 appears in areas

#*****************************************************************************************************************

#Example 24:
# Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size: : 24.5 and 15.45
# Print out areas
# Reverse the orders of the elements in areas
# Print out areas

#******************************************************************************************************************

#Example 25:
# Import the math package. Now you can access the constant pi with math.pi.
# Calculate the circumference of the circle and store it in C.
# Calculate the area of the circle and store it in A.
#//////////////////////////////////////////////////////////
# Import the math package
# Definition of radius
# r = 0.43
# Calculate Circumference as C
# Calculate Area as A
# Build printout
# print("Circumference: ")
# print("Area: " )

#***************************************************************************************************************

#Example 26:

# Import radians function of math package
# Definition of radius
# r = 192500
# Travel distance of Moon over 12 degrees. Store in dist.
# Print out dist

#**************************************************************************************************************

#Example 27:

# Import the numpy package as np
# Create list baseball
# baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Create a numpy array from baseball: np_baseball
# Print out type of np_baseball

#*************************************************************************************************************

#Example 28:
# declare constants 
# PI = 3.14
# GRAVITY = 9.8
# import constant file we created above

# print pi and gravity

#************************************************************************************************************
#Example 29:
#Calculate the Area of a Triangle
# If a, b and c are three sides of a triangle. Then, 5,6,7
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))
#****************************************************************************

#Example 30:
# Python program to swap two variables
# x = 5
# y = 10
# create a temporary variable and swap the values

#***********************************************************************
#Example 31:
# Check if a Number is Positive, Negative or 0

#*******************************************************************************
#Example 32:
# Check Leap Year 2000
# A leap year is exactly divisible by 4 except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400. For example,
# 2017 is not a leap year
# 1900 is a not leap year
# 2012 is a leap year
# 2000 is a leap year
#**********************************************************************************************
#Example 33:
# Check Prime Number "num = 407"
#**********************************************************
#Example 34:
# Make a Simple Calculator

# This function adds two numbers


# This function subtracts two numbers

# This function multiplies two numbers

# This function divides two numbers

#Select Operation from 1 : 4


# using while

    # take input from the user
    
    # check if choice is one of the four options

       
        # check if user wants another calculation
        # break the while loop if answer is no
 
#********************************************************************************************
#Example 35:
# Display Calendar of the given month and year
#****************************************************




