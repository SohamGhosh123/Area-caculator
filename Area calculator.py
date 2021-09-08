def areacalculator():
    _input_=input("Enter the shape you want to calculate the area of:")
    area=0
    pie=3.14
    if _input_=="Square":
        side=int(input("Enter the value of 1 side:"))
        area=area +(side*side)
    elif _input_=="circle":
        radius=int(input("Enter the radius of the circle"))
        area=area +(2*pie*radius)
    elif _input_=="rectangle":
        length=int(input("Enter the lenght of the rectangle:"))
        breadth=int(input("Enter the breadth of the rectangle:"))
        area=area +(length*breadth)
    elif _input_=="triangle":
        base=int(input("Enter the base of the triangle"))
        height=int(input("Enter the height of the triangle"))
        area=area +(0.5*base*height)
    else:
        print("Please enter a valid shape")
    print("%.2f"%area)
areacalculator()
