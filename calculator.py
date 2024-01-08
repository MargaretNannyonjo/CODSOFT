import math
print("SIMPLE CALCULATOR")
print()
print("1. Add\n2. Subtract\n3. Divide\n4. Multiply\n5. Quit")

while True:
    menu = int(input("Choose a number from the menu above: "))
    
    if menu == 5:
        print("Thank you for using the calculator.")
        break

    elif 1 <= menu <= 4:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter Second number: "))
        
        if menu == 1:
            result = first_number + second_number
            print(f"Answer = {result}")
        elif menu == 2:
            result = first_number - second_number
            print(f"Answer = {result}")
        elif menu == 3:
            if second_number != 0:  # To avoid division by zero
                result = first_number / second_number
                print(f"Answer = {result}")
            else:
                print("Error: Division by zero!")
        elif menu == 4:
            result = first_number * second_number
            print(f"Answer = {result}")
    else:
        print("Enter a number from 1 to 5")
