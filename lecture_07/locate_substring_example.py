phrase = "The fish quote: Give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime"

sub_text = "fish"

num_instances = phrase.count(sub_text)
print(f"There are {num_instances} instances of {sub_text}")

index = phrase.find(sub_text, 5)   # start from position 5
print(f"First instance found at position {index}")

# find all here
print(f"------ Finding all indexes of {sub_text} ---------")
count = 0
current_index = 0
while count < num_instances:
    index = phrase.find(sub_text, current_index)
    if index != -1:   # if found
        print(f"{sub_text} found at index {index}")  # print position
    current_index = index + 1   # update new position to start locating fish
    count += 1   # update the number of fish found