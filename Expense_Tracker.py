# Monthly Expense Tracker without OOPs

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses:"))
savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: {savings}")
spending_percentage = (monthly_expenses / monthly_income) * 100
print(f"You are spending {spending_percentage:.2f}% of your income.")
if spending_percentage > 50:
    print("You are spending too much! Consider reducing your expenses.")
elif spending_percentage < 30:
    print("Great job! You are managing your expenses well.")
else:
    print("You are spending a reasonable amount, but there's room for improvement.")