#Write a Python program that will accept the base and height of a triangle and compute the area.
"""A triangle is a polygon with three edges and three vertices. It is one of the basic shapes in geometry. A triangle with vertices A, B, and C is denoted triangle ABC.

    Vertex of a triangle: The point at which two sides of a triangle meet.
    Altitude of a triangle: The perpendicular segment from a vertex of a triangle to the line containing the opposite side.
    Base of a triangle: The side of a triangle to which an altitude is drawn.
    Height of a triangle: The length of an altitude.
"""
a = int(input("Input the base: "))
b = int(input("Input the height: "))

area = a*b/2

print ("area = ", area)
