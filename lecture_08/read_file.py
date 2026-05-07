file_in = open("quotes.txt", "r")  # for reading
print("Current position: ", file_in.tell())
first_3_chars = file_in.read(3)
print("First 3 chars: ", first_3_chars)
print("Current position after reading: ", file_in.tell())

rest_of_line = file_in.readline()
print("Rest of line: ", rest_of_line)

second_line = file_in.readline()
print("Second line: ", second_line)

rest_of_passage = file_in.read()
print("Rest of passage: ", rest_of_passage)
print("Current position after read(): ", file_in.tell())

more_text = file_in.read(100)
print(f"More text: [{more_text}]")

print("--------------------------")
file_in.seek(0)   # go back to start
all_lines = file_in.readlines()  # a list of all the lines
for i in range(len(all_lines)):
    print(f"{i:2}) {all_lines[i]}")

file_in.close()  # remember to close file