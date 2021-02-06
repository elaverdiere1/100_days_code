#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? $'))
tip_value = int(input('What percentage tip would you like to give? 10, 12, 15, or 20? '))
num_people = int(input('How many people to split the bill? '))
pay_value = (total_bill / num_people) * (1 + tip_value / 100)
print(f'Each person should pay: ${round(pay_value, 2)}') 
