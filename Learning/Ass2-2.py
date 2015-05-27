balance =1000
annualInterestRate =0.2
monthlyInterestRate = annualInterestRate/12.0
Paid = 0
PreviousBalance=balance
Minimum=0
MonthlyUnpaidBalance=0
UpdatedBalance=1
MinimumMonthlyPayment = 10
while UpdatedBalance > 0:
	MinimumMonthlyPayment+=10
	PreviousBalance=balance
	for x in xrange(1,13):	
	
		MonthlyUnpaidBalance = PreviousBalance - MinimumMonthlyPayment
	
		UpdatedBalance = MonthlyUnpaidBalance + monthlyInterestRate * MonthlyUnpaidBalance

		PreviousBalance = UpdatedBalance
		print(' PreviousBalance is %.2f' %PreviousBalance)
	print ('Next')
	
print('Lowest payment: %d'%MinimumMonthlyPayment)








