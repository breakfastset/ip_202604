animals_1 = ["elephant", "crocodile", "hippopotamus"]
animals_2 = ["hyena", "cheetah", "honey badger"]

animals_3 = animals_1 + animals_2
print(animals_3)

print(f"Number of animals: {len(animals_3)}")

animals_3.insert(0, "tiger")
print(animals_3)
animals_3.append("emu")
print(animals_3)

animals_3.pop(4)   # remove hyena
print(animals_3)
animals_3.pop()    # remove emu, the last item
print(animals_3)

animals_3.remove("elephant")
print(animals_3)

animals_3.sort()   # sort the original list.
print(animals_3)
animals_3.append("warthog")
animals_3.append("baboon")
print(animals_3)
animals_3.reverse()
print(animals_3)

ascending_animals = sorted(animals_3)  # ascending order
descending_animals = sorted(animals_3, reverse=True)
# sorted makes a copy and sort the copy

print("----------------\nAscending and Descending: ")
print(ascending_animals)
print(descending_animals)
print("Original list: ", animals_3)


