#Personal Expense Tracker 1.3V (Not A Published Version)

#Version 1.0(11/13/2026 - 10:30 am):
#This is a beginner personal expense tracker that can only add info not delete any.
#NEW UPDATE! Version 1.1: added saving info by JSON.(11/20/2026 - 12:20 pm)
#NEW UPDATE! Version 1.2: added Transaction Delete option.(11/20/2026 - 12:26 pm)
#NEW UPDATE! Version 1.3: added Transaction Date and Time.(11/20/2026 - 12:50 pm)
import json
import datetime

try:
    with open("transaction.json", "r") as data:
        transactions = json.load(data)
except FileNotFoundError:
    transactions = []

categories = [
        "Food",
        "Transport",
        "Education",
        "Entertainment",
        "Other"
    ]

def save_transactions():
    with open("transaction.json", "w") as f:
        json.dump(transactions, f, indent=4)

def add_income():
    """This function is for getting our income value from the
       user and putting the amount and description of our transaction
       into a dict called income."""
    print("\n=====Add Income=====")
    try:
        #Always use float for money values!
        amount = float(input("Enter income amount: "))
        if amount <= 0 :
            print("Error. Amount must be greater than zero!")
            return
        description = input("Enter description: ")

        now = datetime.datetime.now()
        now = now.strftime("%H:%M:%S %m-%d-%Y")
        income = {
            #We add a type value here so we can separate expense and income later.
            "type" : "income",
            "amount": amount,
            "description": description,
            "date": str(now)
        }
        transactions.append(income)

        save_transactions()

        print("Income successfully added!")
    except ValueError:
        print("Please enter a valid number!")

def add_expense():
    """This function works similar to the previous one but
       the only difference is that we have another key in
       our dict here named category that we will use in our
       Expenses_By_Category function later."""
    print("\n=====Add Expense=====")
    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Error. Amount must be greater than zero!")
            return
        print("Available categories: ")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        choice = int(input("Choose a category: "))
        if choice < 1 or choice > len(categories):
            print("Invalid category!")
            return
        description = input("Enter description: ")

        now = datetime.datetime.now()
        now = now.strftime("%H:%M:%S %m-%d-%Y")
        expense = {
            "type": "expense",
            "amount": amount,
            #Note that in here we write choice-1 because in category list our first value counts as 0.
            "category": categories[choice-1],
            "description": description,
            "date": str(now)
        }
        transactions.append(expense)
        print("Expense successfully added!")

        save_transactions()

    except ValueError:
        print("Please enter a valid number!")

def calculate_balance():
    """This function has a very simple job, it will only
       calculate our current balance, it changes base of
       our income and expense value."""
    balance = 0
    #Now we can separate expense and income by their type.
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        elif transaction["type"] == "expense":
            balance -= transaction["amount"]
    return balance

def show_history():
    """We use this function to show every transaction we made one by one."""
    print("\n=====TRANSACTION HISTORY=====")
    if len(transactions) == 0:
        print("No transaction found.")
        return
    for i, transaction in enumerate(transactions, start=1):
        print(f"\n Transaction #{i}")
        print(f"Type: {transaction["type"]}")
        print(f"Amount: {transaction["amount"]}")
        print(f"Description: {transaction["description"]}")
        print(f"Transaction Date: {transaction["date"]}")
        #Another usage of type:
        if transaction["type"] == "expense":
            print(f"Category: {transaction["category"]}")

def financial_summary():
    """This function is related to our income and expense values
       and also to our calculate_balance function which is used
       here to show our current balance."""
    print("\n=====Financial Summary=====")
    total_income = 0
    total_expense =0
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        elif transaction["type"] == "expense":
            total_expense += transaction["amount"]
    balance = calculate_balance()
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"\nCurrent Balance: {balance}")

def expenses_by_category():
    """This function is for showing how much our expenses
       are based on their categories"""
    print("\n=====Expenses By Category=====")
    for category in categories:
        total = 0
        for transaction in transactions:
            #VERY IMPORTANT!
            """Note that in this code we appended a dict to a list and we
               can not use key or values separately like we do it with dicts.
               So the only way to print a value from a key in a list is to write
               the code like this:
               
               print(transactions[index]['type'])
               
               if we write it in the normal way(without mentioning index) it will
               give us an error. But in here instead of index we used a variable
               named transaction (with out 's') and for that reason we can write 
               the code like this without any index part."""

            if transaction["type"] == "expense" and transaction["category"] == category:
                total += transaction["amount"]
                print(f"{category}: {total}")

def delete_transaction():
    #This function is exactly the show_history function with a delete option at the end.
    print("\n=====DELETE TRANSACTION=====")
    if len(transactions) == 0:
        print("No transaction found.")
        return
    for i, transaction in enumerate(transactions, start=1):
        print(f"\n Transaction #{i}")
        print(f"Type: {transaction["type"]}")
        print(f"Amount: {transaction["amount"]}")
        print(f"Description: {transaction["description"]}")
        if transaction["type"] == "expense":
            print(f"Category: {transaction["category"]}")
        print(f"Transaction Date: {transaction["date"]}")

    try:
        del_choice = int(input("Enter the number of the transaction you want to delete: "))
        if del_choice > 0:
            transactions.pop(del_choice - 1)
            print(f"\nDeleted transaction number {del_choice} successfully!")
            save_transactions()
        else:
            print("Error. Enter a number bigger than 0.")
            return
    except ValueError:
        print("Please enter a valid number!")




def main():
    """In our final function which is the main function we
       write an input, and we call our other functions that
       we wrote based on users choice from the main menu."""
    while True:
        print("\n=====Personal Expense Tracker=====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Transaction History")
        print("4. Financial Summary")
        print("5. Expenses By Category")
        print("6. Delete Transaction")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_history()
        elif choice == "4":
            financial_summary()
        elif choice == "5":
            expenses_by_category()
        elif choice == "6":
            delete_transaction()
        elif choice == "7":
            print("Good-Bye!")
            break
        else:
            print("Invalid option! Choose between 1 and 6.")
main()