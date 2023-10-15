#17
def square(side):
    perimeter=4*side
    area=round(side**2,2)
    return perimeter, area
    
def rectangle(l, b):
    perimeter = round(2 * 1 * b, 2)
    area = round(l * b, 2)
    return perimeter, area
    
def circle(r):
    perimeter=round(2*3.14*r,2)
    area=round(3.14*(r**2),2)
    return perimeter, area
    
def triangle(sl, s2, b, h):
    perimeter = s1 + s2 + b
    area = round((h * b) / 2, 2)
    return perimeter, area
    
def cylinder(d, h):
    perimeter = (2 * d) + (2 * h)
    area = round((2 * 3.14 * r * h) + (2 * 3.14 * (r ** 2)), 2)
    return perimeter, area

def calc (): 
    print( 'Welcome!' )
    print('Press 1 for Square') 
    print('Press 2 for Rectangle')
    print('Press 3 for Circle') 
    print('Press 4 for Triangle') 
    print('Press 5 for Cylinder')
    print('Press 6 to Exit') 
    choice = int(input('Enter your choice: ')) 
    if(choice == 1): 
        side = float(input('Enter side: ')) 
        perimeter, area = square(side)
        print (f'The perimeter of the square is: {perimeter} unit')
        print(f'The area of the square is: {area} sq. unit')
    elif(choice == 2): 
        length = float(input('Enter length: ')) 
        breadth = float(input('Enter breadth: ')) 
        perimeter, area = rectangle(length, breadth)
        print(f'The perimeter of the rectangle is: {perimeter} unit')
        print(f'The area of the rectangle is: {area} sq. unit') 
    elif(choice == 3): 
        radius = float(input('Enter radius: ')) 
        perimeter, area = circle(radius) 
        print(f'The perimeter of the circle is: {perimeter} unit') 
        print(f'The area of the circle is: {area} sq. unit')
    elif(choice == 4): 
        sidel = float(input('Enter side 1: '))
        side2 = float(input('Enter side 2: ')) 
        base = float(input('Enter base: ')) 
        height = float(input('Enter height: ')) 
        perimeter, area = triangle(sidel, side2, base, height) 
        print (f'The perimeter of the triangle is: {perimeter} unit') 
        print(f'The area of the triangle is: {area} sq. unit') 
    elif(choice == 5): 
        d = float(input('Enter diameter: '))
        h = float(input('Enter height: ')) 
        perimeter, area = cylinder(d, h)
        print(f'The perimeter of the cylinder is: {perimeter} unit')
        print(f'The area of the cylinder is: {area} sq. unit')
    elif(choice == 6):
        exit()
    else:
        print ('Wrong Choice..."')
    calc()

calc()