#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: May 2021
# This program checks if a number is positive, negative, or neither

import math


def main():
    # This function checks if the number is positive, negative, or 0

    # Input

    chosen_number = int(input("Enter the number you have chosen: "))
    print("")

    # process
    if chosen_number > 0:
        # Output
        print("The number is positive")

    elif chosen_number < 0:
        # Output
        print("The number is negative")

    else:
        print("This number is a 0")


if __name__ == "__main__":
    main()
    