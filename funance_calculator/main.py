currency: str = "€"


def calculator_finances(
    monthly_income: float,
    tax_rate: float,
    currency: str,
    rent: float,
    bills: float,
    groceries: float,
    memberships: float,
) -> None:
    """
    This function calculates the monthly savings of a person based on their monthly income and expenses.
    """
    total_monthly_expenses: float = monthly_expenses(
        rent, bills, groceries, memberships
    )

    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_income: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_income - yearly_tax
    monthly_remaining: float = monthly_net_income - total_monthly_expenses
    yearly_expenses: float = total_monthly_expenses * 12

    print("-------------------------------")
    print(f"Monthly Income: {currency} {monthly_income:,.2f}")
    print(f"Tax:{tax_rate: .0f}%")
    print(f"Monthly Tax: {currency} {monthly_tax:,.2f}")
    print(f"Monthly Net Income: {currency} {monthly_net_income:,.2f}")
    print("---")
    print(f"Monthly remaining: {currency} {monthly_remaining:,.2f} less expenses")

    print("---")
    print(f"Yearly Income: {currency} {yearly_income:,.2f}")
    print(f"Yearly Tax: {currency} {yearly_tax:,.2f}")
    print(f"Yearly Net Income: {currency} {yearly_net_income:,.2f}")
    print("---")
    print(
        f"Yearly Remaining: {currency} {yearly_net_income - yearly_expenses:,.2f} less expenses"
    )
    print("-------------------------------")
    print("")


def monthly_expenses(
    rent: float,
    bills: float,
    groceries: float,
    memberships: float,
) -> None:
    """
    This function calculates the monthly expenses of a person based on their monthly expenses.
    """
    total_expenses: float = rent + bills + groceries + memberships
    print("-------------------------------")
    print(f"Rent: {currency} {rent:,.2f}")
    print(f"Bills: {currency} {bills:,.2f}")
    print(f"Groceries: {currency} {groceries:,.2f}")
    print(f"Memberships: {currency} {memberships:,.2f}")
    print("---")
    print(f"Total Expenses: {currency} {total_expenses:,.2f}")
    print("-------------------------------")

    return total_expenses


def get_valid_input(prompt: str) -> float:
    while True:
        try:
            value = input(prompt)
            if len(value) > 8:
                raise ValueError("Input should not be longer than six numbers.")
            return float(value)
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")


def sum_expenses() -> None:
    """
    This function calculates the monthly savings of a person based on their monthly income and expenses.
    """
    if input("Do you want to change the currency? (y/n): ") == "y":
        currency: str = input("Enter the currency (USD): ").capitalize()
    else:
        currency: str = "€"
    print("")
    print("------Enter your monthly income------")
    print("")
    monthly_income: float = get_valid_input("Enter your monthly income: ")
    tax_rate: float = get_valid_input("Enter the tax rate (%): ")
    print("")
    print("------Enter your monthly expenses------")
    print("")
    rent: float = get_valid_input("Enter your rent: ")
    bills: float = get_valid_input("Enter your bills: ")
    groceries: float = get_valid_input("Enter your groceries: ")
    memberships: float = get_valid_input("Enter your memberships: ")

    calculator_finances(
        monthly_income, tax_rate, currency, rent, bills, groceries, memberships
    )


def main() -> None:
    """
    This function is the main function that calls the sum_expenses function.
    """
    sum_expenses()


if __name__ == "__main__":
    main()
