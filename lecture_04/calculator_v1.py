# Summation series:
# 2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, .... <1000
# sum up in steps of 5 from 2 to not exceeding 1000
# find the average
total = 0
count = 0
for i in range(2, 1001, 5):  # start=2, end=53, step=5
    total += i
    count += 1

print(f"Total: {total}")
print(f"Average: {total/count}")

