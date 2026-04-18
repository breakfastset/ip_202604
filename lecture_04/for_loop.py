# for item in ... :     # for each loop
#    statement(s)
# Usage: Fixed number of iterations
for char in "Mountain":
    print(char)

print("-" * 40)
for item in ["Pen", "Pencil", "Eraser"]:
    print(item)

print("-" * 10)
# for i in range(start, end, step):
#    statement(s)       # indexed for loop
for i in range(5):  # start=0, end=5, step=1
    print(i)        # exclude end

print("-" * 40)
for i in range(3, 8): # start=3, end=8, step=1
    print(i)   # 3, 4, 5, 6, 7

print("-" * 40)
for i in range(5, 20, 3): #start=5, end=20, step=3
    print(i)   # 5, 8, 11, 14, 17