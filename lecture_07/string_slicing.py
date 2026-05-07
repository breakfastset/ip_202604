message = "trusted education provider"

print(message[:7])   # start = 0, end = 7, step = 1
# print(message[0:7:1])

print(message[8:17])  # start = 8, end = 17, step = 1

print(message[1:17:2])  # start=1, end=17, step=2
# r s e   d c t o

print("----------------------------")
print()

if "tion" in message:
    print("FOUND tion in message")
else:
    print("tion NOT found in message")

if "private" not in message:
    print("private NOT found in message")
else:
    print("private FOUND in message")