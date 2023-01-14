
#Author: Filip Navrkal 

class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.budget = 0
        self.goal_name = ""
        self.goal_amount = 0
    
    def set_income(self):
        self.income = int(input("Enter your monthly income: "))
        self.budget += self.income
    
    def add_expense(self):
        expense_name = input("Enter the name of the expense: ")
        expense_amount = int(input("Enter the amount of the expense: "))
        self.expenses[expense_name] = expense_amount
        self.budget -= expense_amount
    
    def set_goal(self):
        self.goal_name = input("Enter the name of your goal item: ")
        self.goal_amount = int(input("Enter the cost of your goal item: "))
    
    def check_budget(self):
        return self.budget
    
    def display_info(self):
        print()
        print("Monthly Income: €", self.income)
        print("Remaining budget after expenses: €", self.check_budget())
        print("Expenses:")
        for expense_name, expense_amount in self.expenses.items():
            print(f"{expense_name} - {expense_amount} €")
        print()
        print("Goal Item: ", self.goal_name)
        print("Goal Item Price: €", self.goal_amount)
        if self.check_budget() < self.goal_amount:
            months_to_save = (self.goal_amount - self.check_budget())/self.income
            months_to_save = int(months_to_save) + (1 if (months_to_save % 1) > 0 else 0)
            print(f"You need to save for {months_to_save} months to afford your goal item.")
        else:
            remaining = self.check_budget() - self.goal_amount
            print(f"You can afford your goal item, you will have {remaining} € remaining, after you buy it.")

tracker = BudgetTracker()
tracker.set_income()
while True:
    add_expense = input("Do you want to add an expense (y/n)? ")
    if add_expense.lower() == 'n':
        break
    tracker.add_expense()
tracker.set_goal()
tracker.display_info()


