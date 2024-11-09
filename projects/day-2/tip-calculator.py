print('Welcome to the tip calculator!')

bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
num_people = int(input('How many people to split the bill? '))

tip_total = bill * (tip / 100)
total = bill + tip_total
amount_per_person = round(total / num_people, 2)

print(f'Each person should pay: ${amount_per_person:.2f}')
