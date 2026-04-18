# The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area,
# or if the areas are the same.

length_1 = int(input("Rectangle 1's length: "))
width_1 = int(input("Rectangle 1's width: "))

length_2 = int(input("Rectangle 2's length: "))
width_2 = int(input("Rectangle 2's width: "))

area_1 = length_1 * width_1
area_2 = length_2 * width_2

if area_1 > area_2:
    print("Area of rectangle 1 is greater than area of rectangle 2!")
elif area_1 < area_2:
    print("Area of rectangle 2 is greater than area of rectangle 1!")
else:
    print("Areas of both rectangles are equal!")