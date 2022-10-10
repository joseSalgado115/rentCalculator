income = input('Would you like to enter your hourly or yearly income? ')
if income.lower() == 'hourly':
    hourly_income = input('How much do you make an hour? ')
    monthly = (float(hourly_income) * 40 * 52)/12
    rent = monthly/3
    print('You can afford a rent payment of up to $'+ str(round(rent,2)))
elif income.lower() == 'yearly':
    yearly_income = input('How much do you make per year? ')
    monthly = float(yearly_income) / 12
    rent = monthly/3
    print('You can afford a rent payment of up to $' + str(round(rent,2)))
else:
    print('Please type either hourly or yearly next time.')
