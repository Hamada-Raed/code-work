import random

historical_loans = [
    {"loan_amount": 50000, "interest_rate": 5.5, "repayment_period": 60, "credit_score": 700, "income": 75000, "approved": True},
    {"loan_amount": 10000, "interest_rate": 4.5, "repayment_period": 24, "credit_score": 650, "income": 50000, "approved": False},
    {"loan_amount": 15000, "interest_rate": 6.0, "repayment_period": 36, "credit_score": 720, "income": 65000, "approved": True},
    {"loan_amount": 25000, "interest_rate": 7.0, "repayment_period": 48, "credit_score": 600, "income": 40000, "approved": False},
    {"loan_amount": 40000, "interest_rate": 5.0, "repayment_period": 60, "credit_score": 750, "income": 85000, "approved": True},
    {"loan_amount": 20000, "interest_rate": 6.5, "repayment_period": 48, "credit_score": 680, "income": 55000, "approved": False}
]

def get_loan_details():
    loan_amount = float(input("Enter the loan amount (in USD): "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    repayment_period = int(input("Enter the repayment period (in months): "))
    credit_score = int(input("Enter the applicant's credit score: "))
    income = float(input("Enter the applicant's annual income (in USD): "))
   
    return {
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "repayment_period": repayment_period,
        "credit_score": credit_score,
        "income": income
    }

def predict_loan_approval(loan_details):
    similar_loans = [loan for loan in historical_loans if abs(loan['credit_score'] - loan_details['credit_score']) <= 50]
   
    if not similar_loans:
        print("No similar loan applications found.")
        return None
   
    total_approved = sum(1 for loan in similar_loans if loan["approved"])
    approval_rate = total_approved / len(similar_loans)

    print(f"\nBased on {len(similar_loans)} similar applications with similar credit scores:")
    print(f"Approval rate: {approval_rate * 100:.2f}%")
   
    if random.random() < approval_rate:
        return "Predicted Outcome: Loan Approved"
    else:
        return "Predicted Outcome: Loan Rejected"

def suggest_improvements(loan_details):
    print("\nSuggestions to improve loan approval chances:")

    if loan_details['loan_amount'] > 50000:
        print("Consider reducing the loan amount to increase approval chances.")
    if loan_details['interest_rate'] > 6.0:
        print("A lower interest rate may improve the likelihood of approval.")
    if loan_details['repayment_period'] > 60:
        print("A shorter repayment period could reduce risk and increase approval chances.")
    if loan_details['credit_score'] < 650:
        print("A higher credit score (above 650) could significantly improve approval chances.")
    if loan_details['income'] < 60000:
        print("Higher income levels may increase the likelihood of approval.")

def main():
    loan_details = get_loan_details()
   
    prediction = predict_loan_approval(loan_details)
    if prediction:
        print(prediction)
   
    suggest_improvements(loan_details)

    while True:
        modify = input("\nDo you want to modify the loan parameters and test again? ").lower()
        if modify == 'yes':
            loan_details = get_loan_details()
            prediction = predict_loan_approval(loan_details)
            if prediction:
                print(prediction)
            suggest_improvements(loan_details)
        else:
            break
   
    print("\nThank you for using the loan evaluation tool!")

if __name__ == "__main__":
    main()
