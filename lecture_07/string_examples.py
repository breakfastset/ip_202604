phrase = "Roses are red"

print(phrase[0])    # R
print(phrase[-1])   # d
print("-------------")

for char in phrase:
    print(char)
print("-------------")

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)

# phrase[0] = 'r'  # str is immutable
phrase = "Violets are blue"
print(phrase)