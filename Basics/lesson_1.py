
# print("Hello world")
# print("    /|")
# print("   / |")
# print("  /  |")
# print("/____|")
# print(" /   |")

# write name
# print("my names amira")
# #*********************************************************

# print("there was a boy called Mohamed")
# print("he was 30 years old")
# print("he liked his name Mohamed")
# print("but wasn't happy about being 30")
# print("Mohamed has one brother")

# #**********************************************************
#data type
#variable ===> one value
# character_name = "khaled" #string
# age = 50 #integer,
# print("there was a boy called " +character_name)
# print("he was " + str(age) + " years old")
# print("he liked his name "+character_name)
# print("but wasn't happy about being "+str(age))
# print(character_name+" has one brother")

# #*****************************************************
#
# character_name = "Hisham"
# age = "20"
# print("there was a boy called " +character_name)
# print("he was " +age+ " years old")
# character_name = "Hossam"
# age = "35"
# print("he liked his name "+character_name)
# print("but wasn't happy about being "+age)
# print(character_name+" has one brother")

# #***********************************************************

# print("Welcome to Techmind")
# print("Welcome\nto\nArray") #new line   \t tab
# print("Welcome\" to Array")
# print("Welcome to Array")
# print("Welcome\t to\t Array")

# text = "Welcome to \"Array\""
# print(text)
# print(text+" its cool place"" because its the best coding school")

# #*******************************************************************************
# #**********************#
# #String functions used:#
# #**********************#
# string.lower()
# string.upper()
# string.islower()
# string.isupper()
# string.index
# len(string)
# string.replace()
# string[]
# #*********************************************************

text = "WeLcOmE tO ArRaY"

# print(text.lower())
# print(text.upper())
# print(text.isupper())
# print(text.islower())
# print(text.lower().islower())
# print(len(text))

# amira 5 ===> count number


# text = "Welcome to Array"
#       # 012345678910...  ===> location ==> index
# print(text[11])

# first_name = "Amira"
# last_name = "Fouda"
# print(first_name[0], last_name[0])

# text = "Welcome to Array"
# print(text.index("o"))

# text = "Welcome to Array"
# print(text.replace("Array","Tech mind"))

#*************************************************************************

# #**********************#
# #Numbers functions used:#
# #**********************#


# print(5)
# print(3.2564)
# print(-6.258)

# print(4+8)
# print(8-3)
# print(10/3)
# print(10//3)
# print(4*5)
# print(10%3) #return rest after division
# print(2*6+1)
# print(7*(2+3))


# num = 12
# print(num)

# print(str(num))

# print(str(num) + " my fav num")

# print(num + " my fav num")

# num = -5
# print(abs(num))

# print(pow(2,3)) #2^3

# print(max(2,100,50,3,9))
# print(min(2,9))

# print(round(3.7)) #approximate
# print(round(3.4)) #approximate
# import math   #pakages library
# from math import*
# print(floor(3.7)) #return lower whole num
# #
# print(ceil(3.2)) #return greater whole num
#
# print(sqrt(10))


#*************************************************************************

# #**********************#
# #Inputs functions used:#
# #**********************#

# input()

# input("Enter your name: ")

# name = input("Enter your name: ")
# print("Hello "+name)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello "+name + " your age is: "+age)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello "+name+ " and your age is "+age)

#*************************************************************************

# #*******************#
# #Building calculator#
# #*******************#

# #string
# num_1 = input("Enter your first no: ")
# num_2 = input("Enter your second no: ")
# result = int(num_1) + int(num_2)
# print(result)

# #integr
# num_1 = input("Enter your first no: ")
# num_2 = input("Enter your second no: ")
# result = int(num_1) + int(num_2)
# print(result)

#decimal
# num_1 = input("Enter your first no: ")
# num_2 = input("Enter your second no: ")
# result = float(num_1) + float(num_2)
# print(result)


#*************************************************************************
#1- variable ====> one value
# 2- list ===> int, str , bool, float name=[20, 35.6 , "amir", True]


#*************************************************************************

# #*****#
# #lists#
# #*****#

#I can change its values
# friends = [1,"array", True, False, [1.5, "Amira",True]]
# # print(friends)
#
# print(friends[4][0])

# friends =["example", "array", "python", "programming","CSS","HTML","JAVA"]
# # print(friends[-1])
# print(friends[:])
# start:stop:step
# friends[0] = "Amira"
# print(friends)

#
# Array = ["programming","python","tutorial","html","css"]
# tutorial = ["extend","list1","array"]

# print(Array + tutorial)
# #concatenation
# Array.extend(tutorial)
# print(Array)
# Array += tutorial
# print(Array)
# Array = Array + tutorial
# print(Array)

# Array = ["programming","python","tutorial","html","css"]

# #increase value in the last of list
# Array.append("Amira")
# print(Array)
#add value in the top of list
# Array.insert(1, "language")
# print(Array)
# Array = ["programming","python","tutorial","html","css"]
# #delete value from list
# Array.remove("programming")
# print(Array)
# #delete all values
# Array.clear()
# print(Array)
# # #remove the last value from list and store it away
# Array.pop()
# print(Array)
# Array = ["programming","python","tutorial","html","css"]
# print(Array)
# what_was_popped = Array.pop()
# print(Array)
# print(what_was_popped)


# Array = ["programming","python","tutorial","html","css"]
#
# print(Array.index("programming"))



# Array = ["programming","python","css","tutorial","html","css"]
# print(Array.count("css"))

# print(dir(Array))
# print(type(Array))
# Array.sort()
# print(Array)

# list1 = [3,40,10,1,9]
# list1.sort()
# print(list1)

# Array = ["programming","python","css","tutorial","html","css"]
# #shallow
# list_new = Array.copy()
# print(list_new)
# print(Array)
# list_new = Array
# print(list_new)
# list_new = Array.copy()
# Array.append("Amira")
# print(Array)
# print(list_new)
# list_new = Array.copy()
# Array.append(1)
# print(list_new)
# print(Array)

