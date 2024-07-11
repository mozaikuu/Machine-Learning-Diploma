# *****#
#Tuples#  ()
# *****#
# I can't change its values
coordinates = (23, 45, 35, 50)
print(coordinates)

print(coordinates[0])

# coordinates[0]= 55
print(coordinates)

list_of_tuples = [(2,3), (5,6), (3,7)]
print(list_of_tuples)

# list_of_tuples[1][1]=2
print(list_of_tuples)

# *************************************************************************

# *********#
# Functions#
# *********#

print("hello user")
def say_hi():
    print("hello user1")

print("hello user2")

say_hi()



def say_hi():
    print("hello user")

print("first")
say_hi()
print("second")


def say_hi(name):
    print("hello " + name)

say_hi("Samer")


def say_hi(name, age):
    print("hello " + name + " your age is "+ str(age))

say_hi("Mohamed","30")


def say_hi(name, age):
    print("hello " + name + " your age is "+ str(age))

say_hi("Amira", 25)


def say_hi(name, age):
    print("hello " + name + " your age is "+str(age))

say_hi("Amira", 25)



def cube(num):
    num*num*num

# cube(3)
# print(cube(3))

def cube(num):
    return num*num*num
# cube(3)
print(cube(3))

def sq(num):
    return num*num

print(sq(3))


def cube(num):
    return num*num*num

result = cube(4)

print(result)


def sum(num_1, num_2):
    return num_1 + num_2

print(sum(2,4))


def sub(num_1, num_2):
    return num_1 - num_2

print(sub(2,4))



def sub(num_1, num_2):
    return num_1 - num_2

print("Hello")

print(sub(9,4))

# ********************************************************************

# I wake up
# if I feel hungry
#    I cool breakfast
#
# I leave my house
# If it's cloudy
#   I take my umbrella
# otherwise
#   I take my sunglasses
#
#
# Im at a restaurant
# if I want beef
#   I order a burger
# otherwise if I want pasta
#   I order spaghetti
# otherwise
#   I order a salad


is_hungry = False

# if is_hungry == True:  #===>check condition
if is_hungry:
    print("go eat")


is_hungry = True

if is_hungry == True:  #condition =True
    print("go eat")
else:
    print("do not eat")



is_hungry = True
wants_to_eat = True

if is_hungry and wants_to_eat:
    print("go eat")
else:
    print("do not eat")




is_hungry = False
wants_to_eat = True

if is_hungry and wants_to_eat:
    print("go eat")
elif is_hungry and not wants_to_eat:  #not + false == True
    print("eat so you can servive")
else:
    print("do not eat")




is_hungry = False
wants_to_eat = True

if is_hungry and wants_to_eat:  #False+False ==> wrong
    print("go eat")
elif is_hungry and not wants_to_eat:  #False+True ==> wrong
    print("eat so you can servive")
elif not is_hungry and wants_to_eat:  #True+True ===> Correct
    print("do not eat you are not hungry")
else:
    print("do not eat")



is_hungry = False
wants_to_eat = False

if is_hungry and wants_to_eat:
    print("go eat")
elif is_hungry and not wants_to_eat:
    print("eat so you can servive")
elif not is_hungry and wants_to_eat:
    print("do not eat you are not hungry")
else:
    print("do not eat")


# *************************************************************

# Comparison Operators
# x==x, x<=y, x>=y, x!=y
print(max(100,500,1000,30))
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(2, 15, 10))


print(max(2, 4, 200, 2000))

def match_string(str1, str2):
    if str1 == str2:
        print("the strings do match")
#
#
match_string("Coding","coding")


def match_string(str1, str2):
    if str1 == str2:
        print("the strings do match")
    else:
        print("the strings don't match")
#
match_string("Coding","Amira")
#

def match_string(str1, str2):
    if str1 != str2:
        print("the strings don't match")
    else:
        print("the strings do match")

match_string("Amira","Amira")


# ***************************************************************
# Build Calculator

num1 = float(input("Please enter the first number: "))
operator = input("Please enter the operator: ")  # +,-,*,/
num2 = float(input("Please enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Wrong operator please try again")


# *******************************************************
#
# Dictionaries
# variable = "Amira"
# list = [1,2,"coding"]
# tuple = (14,2)
#
# "key" : "value"
#
# "mar" : "march"
# {key:value}

# key must be unique
conver_month ={

    "jan" : "january", #0
    "feb" : "febraury", #1
    "mar" : "march" #2
}
#
print(conver_month["mar"])



conver_month ={

    "jan" : "january",
    "jan" : "febraury",
    "mar" : "march"
}

print(conver_month["jan"])


conver_month ={

    "jan" : "january",
    "feb" : "febraury",
    "mar" : "march"
}

print(conver_month.get("0"))



conver_month ={

    "jan" : "january",
    "feb" : "febraury",
    "mar" : "march"
}
print(conver_month.get("0","the value doesn't exist"))
print(dir(conver_month))
print(type(conver_month))



conver_month ={

    0 : 2.5,
    1 : True,
    "mar" : ["march","march is the third month",1,5,7]
}

print(conver_month.get("mar","the value doesn't exist"))
