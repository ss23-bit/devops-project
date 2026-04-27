try:
    number = int(input("Pick your number: "))
except ValueError as e:
    print(f"Invalid number: {e}")
else:
    if number < 0:
        print("Negative number")
    elif number == 0:
        print("Zero")
    else:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")


