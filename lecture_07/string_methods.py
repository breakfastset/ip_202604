
brand = "Shaw Theatres"
print(brand.lower())
print(brand.upper())

brand = brand.lower()   # point to the new string
print(brand)

print("len of str: ", len(brand))

print("starts with sh? ", brand.startswith("sh"))
print("starts with SH? ", brand.startswith("SH"))
print("end with es? ", brand.endswith("es"))
print("end with EX? ", brand.endswith("EX"))