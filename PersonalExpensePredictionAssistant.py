def get_user_inputs():
    """Collects user inputs for income and expenses."""
    print("Welcome to the Personal Expense Prediction Assistant!\n")
    try:
        income = float(input("Enter your total monthly income: "))
        print("\nNow, enter your monthly expenses for the following categories:")
        
        rent = float(input("Rent: "))
        groceries = float(input("Groceries: "))
        utilities = float(input("Utilities (electricity, water, etc.): "))
        entertainment = float(input("Entertainment: "))
        others = float(input("Other expenses: "))
        
        return {
            "income": income,
            "expenses": {
                "Rent": rent,
                "Groceries": groceries,
                "Utilities": utilities,
                "Entertainment": entertainment,
                "Others": others
            }
        }
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return None


def calculate_expenses(data):
    """Calculates total expenses and provides suggestions."""
    total_expenses = sum(data['expenses'].values())
    remaining_income = data['income'] - total_expenses
    
    suggestions = []
    if remaining_income < 0:
        suggestions.append("You are overspending. Consider reducing your expenses.")
    elif remaining_income < data['income'] * 0.2:
        suggestions.append("Your savings are low. Try to save at least 20% of your income.")
    else:
        suggestions.append("You have a healthy balance. Keep up the good financial habits!")
    
    return {
        "total_expenses": total_expenses,
        "remaining_income": remaining_income,
        "suggestions": suggestions
    }


def display_summary(data, results):
    """Displays a summary of expenses and predictions."""
    print("\n===== Expense Summary =====")
    print(f"Monthly Income: ${data['income']:.2f}")
    print("\nExpenses Breakdown:")
    for category, amount in data['expenses'].items():
        print(f"  {category}: ${amount:.2f}")
    
    print(f"\nTotal Expenses: ${results['total_expenses']:.2f}")
    print(f"Remaining Income: ${results['remaining_income']:.2f}")
    print("\nSuggestions:")
    for suggestion in results['suggestions']:
        print(f"  - {suggestion}")


def main():
    """Main function to run the Personal Expense Prediction Assistant."""
    print("===== Personal Expense Prediction Assistant =====")
    user_data = get_user_inputs()
    
    if user_data:
        results = calculate_expenses(user_data)
        display_summary(user_data, results)
    else:
        print("Could not analyze expenses due to invalid input.")


if __name__ == "__main__":
    main()
