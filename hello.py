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