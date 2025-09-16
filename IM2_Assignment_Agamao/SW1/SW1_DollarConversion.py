# Dollar Conversion Program

def convert_currency(dollar):
    """Convert dollar to Rupee, Pound, and Yuan"""
    # Example conversion rates (you can update with latest values if needed)
    rupee_rate = 88.08     # 1 USD = 88.08 Indian Rupees
    pound_rate = 0.74      # 1 USD = 0.74 British Pounds
    yuan_rate = 7.12       # 1 USD = 7.12 Chinese Yuan

    rupee = dollar * rupee_rate
    pound = dollar * pound_rate
    yuan = dollar * yuan_rate
    return rupee, pound, yuan


print("Dollar ($)   Indian Rupee (R)   British Pound (P)   Chinese Yuan (Y)")
print("-" * 60)

while True:
    user_input = input("Enter dollar ($) (* to exit): ")

    if user_input == "*":
        print("Bye")
        break

    # Split input by '@'
    amounts = user_input.split("@")

    for amt in amounts:
        if amt.strip().isdigit():
            dollar = int(amt.strip())
            r, p, y = convert_currency(dollar)
            print(f"{dollar:<12}{r:<18.2f}{p:<20.2f}{y:.2f}")
        else:
            print(f"Invalid input: {amt}")
