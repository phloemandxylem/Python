#Packages
#Import the math package
import math

#Use math.pi to calculate the circumference of the circle and store it in C.
r = 0.43
C = 2 * r * math.pi

#Use math.pi to calculate the area of the circle and store it in A.
A = math.pi * r ** 2

#Print circumference and area
print("Circumference: " + str(C))
print("Area: " + str(A))

