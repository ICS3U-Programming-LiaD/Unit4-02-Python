
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov. 3rd, 2022
# This program gives you the
# Factorial of the inputted number


def main():

    # Initialise the counter and factorial answer
    loop_counter = 0
    factorial_answer = 1

    # asking user for a positive integer
    user_number_as_string = input("Enter a whole positive integer ")

    try:

        # making the string into an Int
        user_number = int(user_number_as_string)

        if user_number >= 0:

            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} time(s)".format(loop_counter))
                if loop_counter >= user_number:
                    break
            print("{}! = {}".format(user_number, factorial_answer))
        else:
            print(
                user_number,
                " is not a whole positive integer",
            )

    except Exception:
        print(user_number, "is not a positive whole integer")

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
