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