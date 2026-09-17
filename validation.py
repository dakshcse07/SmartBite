def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")

        except ValueError:
            print("Please enter a valid integer.")