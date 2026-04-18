# x^2 + 3x - 4 = 0     (x+4)(x-1) = 0   -> x = -4 or x = 1
# ax^2 + bx + c = 0
a = 1
b = 3
c = -4

determinant = b ** 2 - 4 * a * c

x1 = (b * -1 + (determinant ** 0.5)) / (2 * a)
x2 = (b * -1 - (determinant ** 0.5)) / (2 * a)

print("x1: ", x1)
print("x2: ", x2)