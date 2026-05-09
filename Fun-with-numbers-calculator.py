# Name: Elias Mandeville    
# Date: Thursday, 9.18.25
# Description: This program will get the user's name, a couple of numbers,
# Do some basic math with the numbers, and display the output.


def main():

    # Declare constant to store computer's number
    COMPUTER_NUMBER = 8.75

    # Display line of 40 #'s
    print("#" * 40)

    # Display intro
    print("Welcome To Fun With Numbers!")

    # Display line of 40 #'s
    print("#" * 40)

    # Blank lines
    print()
    print()

    # Prompt for user name
    userName = input("Please enter your name: ")

    # Prompt for whole number
    numOne = int(input(f"\nHello {userName}, please enter a whole number: "))

    # Zero‑check loop (must come AFTER numOne is created)
    while numOne == 0:
        numOne = int(input("Whole number cannot be zero. Please enter a different whole number: "))

    # Prompt for real number
    numTwo = float(input("\nNow, please enter a real (decimal) number: "))

    # Calculations
    funWithNumbers = numTwo / numOne
    productOfNumbers = COMPUTER_NUMBER * numOne

    # Blank lines
    print()
    print()

    # Display table
    print("Fun With Numbers:")
    print("NumOne:\t\t", numOne)
    print("NumTwo:\t\t", numTwo)
    print("COMPUTER_NUMBER:\t", COMPUTER_NUMBER)

    print()

    # Display fun math message
    print("Let's see some fun math with your numbers and the computer's number")
    print()

    # Display division result
    print("Your second number", numTwo, "divided by your first number", numOne, "is", funWithNumbers)

    # Display multiplication result
    print(f"Your first number {numOne} times the computer's number {COMPUTER_NUMBER} is {productOfNumbers}")

    print()
    print("Thank you for your time!")


# Call main
main()
