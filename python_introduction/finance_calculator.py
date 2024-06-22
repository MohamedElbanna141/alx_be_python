monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#(Monthly Savings = Income - Expenses)
monthly_savings = monthly_income - monthly_expenses

#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Monthly Savings
print("Your monthly savings are $", monthly_savings)

#Projected Savings
print("Projected savings after one year, with interest, is: $", int(projected_savings))