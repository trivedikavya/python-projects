def get_user_input():
    """Function to collect user input from the console."""
    print("Welcome to Loan Eligibility Predictor!\n")
    try:
        income = float(input("Enter Applicant's Monthly Income: "))
        loan_amount = float(input("Enter Loan Amount Requested: "))
        credit_score = int(input("Enter Credit Score (300-850): "))
        employment_status = input("Are you employed? (yes/no): ").strip().lower()

        # Ensure valid inputs
        if credit_score < 300 or credit_score > 850:
            print("Credit score must be between 300 and 850.")
            return None
        if employment_status not in ['yes', 'no']:
            print("Employment status must be 'yes' or 'no'.")
            return None

        return {
            "income": income,
            "loan_amount": loan_amount,
            "credit_score": credit_score,
            "employment_status": employment_status
        }
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return None


def evaluate_loan_eligibility(data):
    """Function to determine loan eligibility based on simple rules."""
    if data['credit_score'] >= 700 and data['income'] > data['loan_amount'] and data['employment_status'] == 'yes':
        return "Loan Approved"
    else:
        return "Loan Rejected"


def main():
    """Main function to run the loan eligibility predictor."""
    print("===== Automated Loan Eligibility Predictor =====")
    user_data = get_user_input()

    if user_data:
        result = evaluate_loan_eligibility(user_data)
        print(f"\nResult: {result}")
    else:
        print("Could not evaluate loan eligibility due to invalid input.")


if __name__ == "__main__":
    main()
