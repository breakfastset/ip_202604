score = float(input("Score: "))

#if 80 <= score <= 100:
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 60 <= score < 70:
    grade = "C"
elif 50 <= score < 60:
    grade = "D"
elif 0 <= score < 50:
    grade = "F"
else:
    grade = "NA"

if grade != "NA":
    print(f"Your grade is {grade} for score {score:.0f}.")
else:
    print("Please key in a valid score (0 to 100)")