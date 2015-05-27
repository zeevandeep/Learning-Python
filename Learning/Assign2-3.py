balance =320000
annualInterestRate =0.2
monthlyInterestRate = annualInterestRate/12.0

low=balance/12
k=1+monthlyInterestRate
high=(balance * (k**12)) / 12.0
print('High %f' %high)
print ('low %f'%low)
PreviousBalance=balance
UpdatedBalance=1
precision=0.1
while (UpdatedBalance >= precision):
	
	MinimumMonthlyPayment=(high+low)/2	
	print ('MinimumMonthlyPayment%f'%MinimumMonthlyPayment)
	
	for x in range(1,13):	
	
		MonthlyUnpaidBalance = PreviousBalance - MinimumMonthlyPayment
	
		UpdatedBalance = MonthlyUnpaidBalance + monthlyInterestRate * MonthlyUnpaidBalance

		PreviousBalance = UpdatedBalance
		print(' PreviousBalance is %.2f' %PreviousBalance)

	print ('Next')

	if(UpdatedBalance < 0):
		
		high=MinimumMonthlyPayment
		PreviousBalance=balance

	elif(UpdatedBalance > precision):
		
		low=MinimumMonthlyPayment
		PreviousBalance=balance
		
print('Lowest payment: %.2f'%MinimumMonthlyPayment)

