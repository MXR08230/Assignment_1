import math
r=30
#area of circle with radius value 30
_area_of_circle_=math.pi*pow(r,2)
print("area of circle is:""{:.2f}".format(_area_of_circle_))
#circumference of circle with radius value 30
_circum_of_circle_=2*math.pi*r
print("circumference of circle is:""{:.2f}".format(_circum_of_circle_))
#Taking radius as user input and calculate the area
radius=int(input("Enter the radius:"))
area_circle=math.pi*pow(radius,2)
print("area of circle is:""{:.2f}".format(area_circle))