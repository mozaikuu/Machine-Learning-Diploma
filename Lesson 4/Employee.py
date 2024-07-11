# class Employee:
#
#     def __init__(self, name, age, department, is_manager,rating): #attribute
#         self.name = name
#         self.age = age
#         self.department = department
#         self.is_manager = is_manager
#         self.rating = rating




# class Student:
#     def __init__(self, name , age, gpa, major):
#         self.name = name
#         self.age = age
#         self.gpa = gpa
#         self.major = major





# class Employee:
#     def __init__(self, name, age, department, is_manager, rating):
#         self.name = name
#         self.age = age
#         self.department = department
#         self.is_manager = is_manager
#         self.rating = rating  # from 1:5
# #
#     def is_excellent(self):
#         if self.rating >= 4.5:
#             return True
#         else:
#             return False

class Employee:
    def __init__(self, name, age, department, is_manager, rating, salary):
        self.name = name
        self.age = age  #60 >=  +500
        self.department = department
        self.is_manager = is_manager
        self.rating = rating  # from 1:5
        self.salary = salary
#

    # def bonus(self):
    #     if self.age >= 60:
    #         self.salary += 500
    #         print("Salary increase to " +str(self.salary))
    #     else:
    #         print("no bonus added, salary is still " +str(self.salary))