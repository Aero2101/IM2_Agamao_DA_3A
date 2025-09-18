def display_cart(mydict):
    print("Displaying Values")
    print("Key      Value")
    for k, v in mydict.items():
        print(f"{k:<8} {v}")


def main():
    # start with an empty dictionary
    mydict = {}

    # matrix size = 3 → add 3 shopping items
    mydict[0] = "underwear"
    mydict[1] = "tank top"
    mydict[2] = "jacket"

    print("You have 3 items in the cart")

    while True:
        action = input(
            "\nWhat would you like to do [C]hange items [R]emove [D]isplay  S[earch] ?  "
        ).strip().lower()

        if action == "d":  # Display
            display_cart(mydict)

        elif action == "s":  # Search
            # Search by value first
            item = input("\nEnter item to search: ").strip()
            found = False
            for val in mydict.values():
                if val.lower() == item.lower():
                    print(f"Found {val} item")
                    found = True
                    break
            if not found:
                # if not found by value, ask for key
                try:
                    key = int(input("Enter key to search: ").strip())
                    value = mydict.get(key)
                    if value:
                        print(f"Found {value} item")
                    else:
                        print("Im sorry, not in the cart")
                except ValueError:
                    print("Im sorry, not in the cart")

        elif action == "r":  # Remove
            try:
                key = int(input("\nEnter key to search: ").strip())
                value = mydict.get(key)
                if value:
                    print(f"The key {key} with value {value} has been deleted")
                    del mydict[key]
                else:
                    print("Key not found")
            except ValueError:
                print("Key not found")

        elif action == "c":  # Change
            try:
                key = int(input("\nEnter key to search: ").strip())
                value = mydict.get(key)
                if value:
                    print(f"Found {value} item")
                    new_value = input("Enter value: ").strip()
                    mydict[key] = new_value
                else:
                    print("Im sorry, not in the cart")
            except ValueError:
                print("Im sorry, not in the cart")

        elif action == "*":  # Exit
            print("Bye")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
