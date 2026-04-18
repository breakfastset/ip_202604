# A teacher has 3,123,456 sweets to distribute
# to 127 students.
# How many sweets does each student get?
# How many are left over?
#
num_sweets = 4_123_456
num_students = 127

num_sweets_per_student = num_sweets // num_students
remainder = num_sweets % num_students

print(f"Each student will get {num_sweets_per_student} sweets.")
print(f"There are {remainder} sweets left.")