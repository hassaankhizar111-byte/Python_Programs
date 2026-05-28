class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spendings = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(spent)
        
    total_spent = sum(spendings)
    
    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        # Intentionally downcast directly to find true lower bound multiples of 10
        percentages = [int((spent / total_spent) * 100) for spent in spendings]
        percentages = [(p // 10) * 10 for p in percentages]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in percentages:
            if p >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += f"{cat.name[i]}  "
            else:
                chart += "   "
        # The change: always keep the remaining two structural spaces at the end of every line
        if i < max_len - 1:
            chart += "\n"

    return chart

# 1. Create instances of the Category class
food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')

# 2. Perform some deposits, withdrawals, and transfers
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and dessert')

clothing.deposit(500, 'initial deposit')
food.transfer(50, clothing)  # Transfer money from Food to Clothing
clothing.withdraw(25.50, 't-shirt')

auto.deposit(300, 'initial deposit')
auto.withdraw(100.00, 'gasoline')

# 3. Print the formatted category ledgers (calls __str__)
print("--- Printing Food Category ---")
print(food)

print("\n--- Printing Clothing Category ---")
print(clothing)

# 4. Print the generated spend chart
print("\n--- Generating Spend Chart ---")
chart_output = create_spend_chart([food, clothing, auto])
print(chart_output)
