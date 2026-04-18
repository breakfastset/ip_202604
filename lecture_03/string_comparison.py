string_1 = "bat"      # 'b' is 98
string_2 = "bagger"
string_3 = "Bat"      # 'B' is 66

print(string_1 == string_2)   # False
print(string_1 != string_2)   # True
print(string_1 > string_2)    # True
print(string_1 < string_2)    # False

print()
print(string_1 > string_3) # True

name = input("Your name? ")
print(name)
print(name.lower())    # change to lower case
print(name.upper())   # change to upper case