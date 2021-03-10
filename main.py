#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Welcome
print('Welcome to the tip calculator')
# Input del total bill
total_bill = int(input('What is the total bill:\n'))
# Percentage bill
percentage_bill = float((input('What is the percentage bill to pay: 0.10, 0.12, 0.15? \n')))
# People to split the bill
split_bill = int(input('How many people ll pay the bill:\n'))
# Operation algorithm
new_percentage = 1.0 + percentage_bill
total_with_percentage = total_bill * new_percentage
total_operation = total_with_percentage / split_bill
result = round(total_operation, 3)
print('the total amount by person is ' + str(result))