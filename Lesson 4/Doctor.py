class Doctor:
    def studied_years(self):
        print("I studied 7 years")

    def works_where(self):
        print("I work in a hospital")

    def paid_by_who(self):
        print("I get paid by the Government")

# import math
# import json
#
# class Calculator:
#   def __init__(self):
#     self.history = []
#
#   def add(self, num1, num2):
#     result = num1 + num2
#     self.history.append({"operation": "add", "result": result, "operands": [num1, num2]})
#     return result
#
#   def subtract(self, num1, num2):
#     result = num1 - num2
#     self.history.append({"operation": "subtract", "result": result, "operands": [num1, num2]})
#     return result
#
#   def multiply(self, num1, num2):
#     result = num1 * num2
#     self.history.append({"operation": "multiply", "result": result, "operands": [num1, num2]})
#     return result
#
#   def divide(self, num1, num2):
#     result = num1 / num2
#     self.history.append({"operation": "divide", "result": result, "operands": [num1, num2]})
#     return result
#
#   def sqrt(self, num):
#     result = math.sqrt(num)
#     self.history.append({"operation": "sqrt", "result": result, "operands": [num]})
#     return result
#
#   def clear_history(self):
#     self.history = []
#
#   def save_history(self, file_path):
#     with open(file_path, "w") as f:
#       json.dump(self.history, f)
#
#   def load_history(self, file_path):
#     with open(file_path, "r") as f:
#       self.history = json.load(f)
#
