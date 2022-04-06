#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: April 2022
# This program lets the user see if it is a leap year


def main():
    # this function lets the user see if it is a leap year

    # input
    try:
        year = int(input("Enter the year: "))

        # process & output

        if year % 4 == 0:
            if year % 400 == 0:
                print("It is not a leap year.")
            else:
                print("It is a leap year.")
        else:
            print("It is not a leap year.")
    except Exception:
        print("This was not an integer")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
