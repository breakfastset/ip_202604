scores = [55, 66, 77, 43, 89, 98, 65, 73, 25, 82, 85]

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

print(f"Range: {lowest} - {highest}")
print(f"Average: {average:.1f}")

scores_1 = scores   # both point to the same list
scores_1[0] = 83   # modify scores_1

print(scores)   # but scores is affected

scores_2 = scores[:]   # using slicing to make a copy
scores_2[-1] = 100

print("scores: ", scores)
print("scores_2: ", scores_2)