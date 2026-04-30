numbers = [5, 7, 19, 20, 31, 4, 2, 17]
#          0  1  2   3   4   5  6, 7
#         -8 -7 -6  -5  -4  -3  -2  -1
print(numbers)
print(type(numbers))
print(numbers[0])  # first item, 5
print(numbers[len(numbers) - 1])  # index 7
print(numbers[-1])  # last item

print("--" * 10)
numbers[0] = 99    # modify first item
print(numbers)

print("--" * 10)
names = ["Edgar", "Lim", "Sotong"]
print(names)

print("--" * 10)
person = ["Tom", 7]  # mixed list