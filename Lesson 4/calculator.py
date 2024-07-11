from Class import Car

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b



def calculator():
  choice = ''
  while choice != 'no':
    print('''
    Please choose an operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Power
    ''')

    choice = input('Enter choice (no to exit): ')
    choice = choice.lower()
    if choice == 'no':
      break
    elif choice not in ['1', '2', '3', '4', '5']:
      print('Invalid choice. Please try again.')
      continue

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if choice == '1':
      print(num1, '+', num2, '=', add(num1, num2))
    elif choice == '2':
      print(num1, '-', num2, '=', subtract(num1, num2))
    elif choice == '3':
      print(num1, '*', num2, '=', multiply(num1, num2))
    elif choice == '4':
      print(num1, '/', num2, '=', divide(num1, num2))
    elif choice == '5':
      print(num1, '**', num2, '=', power(num1, num2))

if __name__ == '__main__':
  
  t = Thread(target=calculator)
  t.start()
  t.join()
  
  car = Car('model', 'year', 'color', 'price', 'mileage', 'engine', 'transmission')