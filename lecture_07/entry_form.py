
full_name = input("Full name (at least 3 chars)? ")
password = input("Password (at least 8 chars)? ")

full_name = full_name.strip()
password = password.strip()

if len(full_name) >= 3 and len(password) >= 8:
    print("Full name:", full_name)
    print("Password:", password)
    print("Thank you for registering with us!")
else:
    print("Full name must >= 3 chars")
    print("Password must >= 8 chars")