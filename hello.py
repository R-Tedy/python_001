# ternary operators
print('hello Stedy')

age = 22

if age >= 18:
  message = 'eligible'
else :
  message = 'not eligible'

message = 'eligible' if age >= 18 else 'not eligible'
print(message)

# logical operators
high_income = False
good_credit = True

if high_income and good_credit:
  print('Eligible')
else:
  print('Not Eligible')

if high_income or good_credit:
  print('Eligible')
else:
  print('Not Eligible')

if not good_credit:
  print('Eligible')
else:
  print('Not Eligible')

# short-circuit operators - when one of the arguments is false the expression fails for and operators or true for or operators.
# logical operators are short circuit.

# Chaining comparison operators
if 18 <= age < 65 :
  print('eligible')

# for loops
# multiplying a number and a string repeats the string that number of times
for number in range(3):
  print('attempt', number + 1)

for number in range(1, 4):
  print('attempt', number)

for number in range(1, 10, 2):
  print('attempt', number)

# for else 
successful = True
for number in range(3):
  print('attempt')
  if successful:
    print('successful')
    break
else:
  print('attempted 3 times and failed')

# Nested loops
# the code bellow has an outer loop and an inner loop.
for x in range(5):
  for y in range(3):
    print(f"({x}, {y})")

# iterables
# therange object is iterable meaning it can be changed on execution
# range(), strings ,lists are iterable hence they can be used in a for loop

# while loops
# evaluates a condition and repeating a task.
number = 100
while number > 0:
  print(number)
  number //= 2

command = ''
while command.lower() != 'quite':
  command = input('>')
  print('ECO', command)

# infinite loops - loops that run forever
while True:
  command = input('>')
  if command.lower() == 'quite':
    break

# exercise
count = 0
for x in range(1, 10):
  if not x % 2:
    count += 1
    print(x)
print(f'we have {count} even numbers')

# functions
def hell0_functions():
  print('hi you')

hell0_functions()

# arguments
# parameter is the inpuctvariable while an argument is the actual input provided to a function.
def hell0_function(first_name, last_name):
  print(f'hi {first_name} {last_name}')

hell0_function('Roland', 'Stedy')

# types of functions
# 1 - Perform a tast
# 2 - Return a value
# all functions return none by default unless the return is specified
def greet(name):
  return f'Hi {name}'

message = greet('Stedy')

# keyword arguments
def increment(number,by):
  return number + by

print(increment(2, by=3))

# default arguments
# optional params after the requires params
def increment(number,by=3):
  return number + by

print(increment(2))

# *args, wait 
# toples
def multiply(*numbers):
  total = 1
  for number in numbers:
    total *= number
  return total

multiply(2,3,4,5)