# Budget Tracker

class BudgetTracker:
    def __init__(self):
        self.transactions = []  

    def add_transaction(self, amount, category, description):
        transaction = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.transactions.append(transaction)

    def view_balance(self):
        balance = sum([transaction['amount'] for transaction in self.transactions])
        return balance

    def generate_report(self):
        report = {}
        for transaction in self.transactions:
            category = transaction['category']
            amount = transaction['amount']
            if category in report:
                report[category] += amount
            else:
                report[category] = amount
        return report
def show_menu():
    print("\nMenu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Report")
    print("5. Save & Exit")

def add_income(budget_tracker):
    amount = float(input("Enter income amount: "))
    description = input("Enter description: ")
    budget_tracker.add_transaction(amount, "Income", description)
    print("Income added successfully!")

def add_expense(budget_tracker):
    amount = -float(input("Enter expense amount: "))
    category = input("Enter category (e.g., food, rent, transport): ")
    description = input("Enter description: ")
    budget_tracker.add_transaction(amount, category, description)
    print("Expense added successfully!")

def view_balance(budget_tracker):
    balance = budget_tracker.view_balance()
    print(f"Current Balance: ${balance:.2f}")

def view_report(budget_tracker):
    report = budget_tracker.generate_report()
    print("\nExpense Report by Category:")
    for category, total in report.items():
        print(f"{category}: ${total:.2f}")
import json

def save_data(budget_tracker, filename="budget_data.json"):
    with open(filename, 'w') as f:
        json.dump(budget_tracker.transactions, f)
    print("Data saved successfully!")

def load_data(budget_tracker, filename="budget_data.json"):
    try:
        with open(filename, 'r') as f:
            budget_tracker.transactions = json.load(f)
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No previous data found, starting fresh.")
def main():
    budget_tracker = BudgetTracker()
    load_data(budget_tracker)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_income(budget_tracker)
        elif choice == '2':
            add_expense(budget_tracker)
        elif choice == '3':
            view_balance(budget_tracker)
        elif choice == '4':
            view_report(budget_tracker)
        elif choice == '5':
            save_data(budget_tracker)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
