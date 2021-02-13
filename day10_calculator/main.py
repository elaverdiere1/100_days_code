import art

print(art.logo)

#add
def add(n1,n2):
  return n1 + n2
#subtract
def subtract(n1,n2):
  return n1 - n2
#multpily
def multiply(n1,n2):
  return n1 * n2
#divide
def divide(n1,n2):
  return n1 / n2

operators = {
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide,
}
# setting up the main body of the calculator
def calculator():
  num1 = float(input('What is the first number?: '))
  for x in operators:
    print(x)
# checking to continue
  exit_choice = True
  while exit_choice:
    symbol = input('Which operation do you want? Pick from the line above: ')
    num2 = float(input('What is the next number?: '))
    calc_function = operators[symbol]
    answer = calc_function(num1,num2)
    print(f'{num1} {symbol} {num2} = {answer}')
  
    if input(f'Type "y" to continue calculating with {answer}, or type "n" to start over: ') == 'y': 
      num1 = answer
    else:
      exit_choice = False
      calculator()

calculator()
