# # readable return boolean value True/ False
# workers_file = open("read and write",'r') # read
# print(workers_file.readable())
# workers_file.close()
#************************************************************
# #Read file
# workers_file = open("read and write",'r')
# print(workers_file.read())
# workers_file.close()

#**************************************************
#read line
# workers_file = open("read and write",'r')
# print(workers_file.readline())
# print(workers_file.readline())
# print(workers_file.readline())
# workers_file.close()
#******************************************************
# read lines
# workers_file = open("read and write",'r')
# print(workers_file.readlines())   #List
# workers_file.close()
# #**************************************************************
#read specifice line
# workers_file = open("read and write",'r')
# print(workers_file.readlines()[4])
# workers_file.close()
#*******************************************************************
#using for loop
# workers_file = open("read and write",'r')
# for worker in workers_file.readlines():
#     print(worker)
# workers_file.close()
# ****************************************************
# workers_file = open("read and write",'r')
# for worker in workers_file.readlines():
#     print(worker+ " is cool")
# workers_file.close()
#***************************************************************
# '''                     | r   r+   w   w+   a   a+
# ------------------------|--------------------------
# read                    |+    +        +         +
# write                   |     +    +   +    +    +
# create                  |          +   +    +    +
# truncate                |          +   +
# position at start       |+    +    +   +
# position at end         |                   +    +
# '''

#
# workers_file = open("read and write","a")
# workers_file.write("\nwelcome techmind")
# workers_file.close()


# workers_file = open("read and write","a")
# workers_file.write("\nHello")
# workers_file.close()


# workers_file = open("Techmind_group1","a+")
# workers_file.write("\nAhmed\nMouse\nYoussef")
# workers_file.close()


# workers_file = open("Shoot_kora.html","w")
# workers_file.write("<p>This is a paragraph of matches</p>")
# workers_file.close()

# workers_file = open("Techmind_group1","w")
# llll= ['''This is the first line
# This is the second line
# This is the third line''']
# workers_file.writelines(llll)
# workers_file.close()

#################################################################################

# my_string ="This is my string!"
# print(my_string[:0:-1])

import math
# *************************************************************************************
#   modules
# ***********
# import functions
#
# print(functions.roll_dice(5))

#*********************************************************************
# pip install docx
#**************************************************
#
# from Employee import Employee
# emp=Employee("Mousa",25,"CS",False)
# employee1 = Employee("Amira", 20, "Array", True)
# employee2 = Employee("Ahmed", 30, "Coding", False)
# employee3 = Employee("Islam", 35, "Cls", True)
# employee4 = Employee("AbdElaziz", 30, "Coding", False)
# print(emp.name,employee1.name,employee2.name,employee3.name)
# # print(employee1.age, employee2.age, employee2.department, employee1.is_manager,employee3.name,employee4.is_manager)
# from Employee import Student
# stud=Student("amira",25,3.5,"CS")
# print(stud.gpa)


# from Employee import Employee
#
# employee1 = Employee("Amira", 20, "Array", True, 5)
# employee2 = Employee("Ahmed", 30, "Coding", False, 3)
# # print(employee1.rating)
# print(employee1.is_excellent())
# print(employee2.is_excellent())

# from Employee import Employee
#
# employee1 = Employee("Amira", 20, "Array", True, 5, 60000)
# employee2 = Employee("Ahmed", 60 , "Coding", False, 3, 20000)
#
# print(employee1.salary)
# employee1.bonus()
# print(employee2.salary)
# employee2.bonus()

#*******************************************************************

# from Doctor import Doctor
#
# doctor1 = Doctor()
# #
# doctor1.studied_years()
# doctor1.works_where()
# doctor1.paid_by_who()

from Doctor import Doctor
from FamilyDoctor import FamilyDoctor

doctor1 = Doctor()
doctor2 = FamilyDoctor()

doctor2.what_specialization()
doctor2.studied_years()
doctor2.works_where()
doctor2.paid_by_who()

#
doctor1.studied_years()
doctor1.works_where()
doctor1.paid_by_who()
