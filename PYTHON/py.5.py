import math
radius = float(input("enter the radius of the circle: "))
area = math.pi *pow(radius , 2)
circumference = 2*math.pi*radius
print(f"The area of the circle is {round(area, 2)}mm^2 and the circumference is {round(circumference, 2)}mm^2")