names_str = "bobo    chacha   dodo ah gogo"
names = names_str.split()
print(names)

current_date = "19/5/2026"
date_parts = current_date.split("/")
print(date_parts)

if len(date_parts[0]) == 1:
    date_parts[0] = "0" + date_parts[0]
if len(date_parts[1]) == 1:
    date_parts[1] = "0" + date_parts[1]

print(date_parts)
# 07-05-2026

updated_date = "-".join(date_parts)
print(updated_date)