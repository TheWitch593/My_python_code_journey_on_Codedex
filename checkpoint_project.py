import math

tries = 0

while True and tries < 3:
    print("\n==================")
    print("Area Calculator 📐")
    print("==================")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    shape = int(input("What shape did you choose? "))

# Triangle
    if shape == 1:
        print("\nYour shape is a triangle!")
        height = float(input("\nEnter the height: "))
        base = float(input("Enter the base: "))
        area = (height * base) / 2
        print(f"Area: {area}")

#Rectangle 
    elif shape == 2:
        print("\nYour shape  is a  rectangle!")
        length = float(input("\nEnter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"Area: {area}")

#Square
    elif shape == 3:
        print("\nYour shape is a square!")
        side = float(input("\nEnter the side size: "))
        area = side*side
        print(f"Area: {area}")

#Circle
    elif shape == 4:
        print("\nYour shape is a circle!")
        radius = float(input("\nEnter the radius size: "))
        area = math.pi * (radius * radius)
        print(f"Area: {area}")

#Quit
    elif shape == 5:
        print("You quit the Area Calculator. Have a nice day!❤️")
        break
        
    else:
        print("You choose an invalid option! Try again!")
        tries = tries + 1
        
        if tries == 3:
            print("You reach your daily limit! Try again tomorrow!")