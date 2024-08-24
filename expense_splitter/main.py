def get_valid_input(prompt: str) -> float:
    while True:
        try:
            value = input(prompt)
            if len(value) > 6:
                raise ValueError("Input should not be longer than six numbers.")
            return float(value)
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")


def calculate_split_amount() -> None:
    """
    This function calculates the amount each person has to pay based on the total amount and their respective percentages.
    """
    print("---------------------------------")
    print("Welcome to the Expense Splitter!")
    print("")
    total_amount: float = get_valid_input("Enter the total amount: ")
    num_people: int = int(get_valid_input("Enter the number of people: "))
    tip_percentage: float = get_valid_input("Enter your tip %: ")
    print("---------------------------------")
    print("")

    # Calculate the tip amount based on the total amount
    tip: float = total_amount * (tip_percentage / 100)

    # Add the calculated tip to the total amount
    total_amount += tip

    percentages = []
    for i in range(num_people - 1):
        while True:
            percentage = get_valid_input(f"Enter the percentage for person {i + 1}: ")
            if percentage < 0 or percentage > 100:
                print("Invalid percentage. Please enter a value between 0 and 100.")
            else:
                percentages.append(percentage)
                break

    remaining_percentage = 100 - sum(percentages)
    if remaining_percentage < 0:
        print("The total percentage exceeds 100%. Please check your inputs.")
        return

    percentages.append(remaining_percentage)

    print(f"The remaining {remaining_percentage}% is assigned to person {num_people}.")
    print("")
    print("---------------------------------")

    for i, percentage in enumerate(percentages):
        amount_per_person: float = total_amount * (percentage / 100)
        print("")
        print(
            f"Person {i + 1} has to pay: € {amount_per_person:.2f} which is {percentage}% of the total amount."
        )
    print("")
    print("---------------------------------")
    print("The total amount of the bill including tip: €", total_amount)
    print("---------------------------------")


def main() -> None:
    calculate_split_amount()


if __name__ == "__main__":
    main()
