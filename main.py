length = float(input('Please enter your length in feet\n'))
width = float(input('Please enter your width in feet\n'))
carpet_price = float(input('Enter the price of square yard for carpet (between $2.50 and $4.50)\n'))
area = length * width 
cost = area * carpet_price
SALES_TAX = 0.06
proccess = cost * SALES_TAX
total_cost = proccess + cost
print(f'You need {area} sq. yards to buy')
print(f'Subtotal is ${cost:.2f}')
print(f'The state sales tax is ${proccess:.2f}')
print(f'The total cost of the carpet for your room is ${total_cost:.2f}')