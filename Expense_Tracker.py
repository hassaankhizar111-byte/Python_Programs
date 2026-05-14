def get_expenses(expense_name):
    amount = input(f"Enter your monthly {expense_name} expenses: ")
    return amount

monthly_income = int(input("Enter your monthly income: "))

clothing_expenses = get_expenses("clothing")
food_expenses = get_expenses("food")
rent_expenses = get_expenses("rent")
transportation_expenses = get_expenses("transportation")

monthly_expenses = (
    int(clothing_expenses) + 
    int(food_expenses) + 
    int(rent_expenses) + 
    int(transportation_expenses)
)

savings = monthly_income - monthly_expenses
print("\n ===Expense Report=== ")
print(f"Monthly Income: {monthly_income}")
print(f"Monthly Expenses: {monthly_expenses}")
print(f"Savings: {savings}")

expense_percentage = (monthly_expenses / monthly_income) * 100
print(f"Percentage of Income spend: {expense_percentage:.2f}% of your income.")

if expense_percentage  > 50 :
    print("You are spending too much ")
elif expense_percentage < 30 :
    print("You are spending less than 30% of your income, good job!")
else:
    print("You are spending a reasonable amount, but there's room for improvement.")
