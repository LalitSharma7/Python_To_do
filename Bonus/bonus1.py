try:
    width = int(input("Enter width of rectangle: "))
    length = int(input("Enter length of rectangle: "))
    if width == length:
        exit("This looks like a square")
    area = width*length
    print(area)

except ValueError:
    print("Please enter a number")