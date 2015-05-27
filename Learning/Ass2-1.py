balance=4842
anuualInterestRate=0.2
monthlyPaymentRate=0.04
monthlyInterestRate = anuualInterestRate/12.0
Paid = 0
PreviousBalance=balance
for x in xrange(1,13):
	print ('Month: %d' %x)
	MinimumMonthlyPayment = monthlyPaymentRate * PreviousBalance
	
	print ('Minimum monthly payment: %.2f' %MinimumMonthlyPayment)
	MonthlyUnpaidBalance = PreviousBalance - MinimumMonthlyPayment
	UpdatedBalance = MonthlyUnpaidBalance + monthlyInterestRate * MonthlyUnpaidBalance
	print ('Remaining balance %.2f' %UpdatedBalance)
	PreviousBalance = UpdatedBalance
	Paid+=MinimumMonthlyPayment
print ('Total Paid: %.2f' %Paid)
print(' Remaining balance: %.2f'%UpdatedBalance)


#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)