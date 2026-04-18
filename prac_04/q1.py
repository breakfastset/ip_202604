# Write a program that asks the user to enter the number of times that
# he/she have run around a racetrack, and then use a loop to prompt him/her
# to enter the lap time for each of his/her lap.
# When the loop finishes, the program should display
# a) the time of the fastest lap,
# b) the time of the slowest lap,
# c) and the average lap time.
# d) total time taken

num_rounds = int(input("How many rounds around the racetrack? "))
total = 0
highest_timing = -1   # slowest
lowest_timing = 1_000_000   # fastest

for i in range(num_rounds):
    time_taken = float(input(f"Timing in round {i+1} in seconds? "))
    if time_taken > highest_timing:
        highest_timing = time_taken
    if time_taken < lowest_timing:
        lowest_timing = time_taken
    total += time_taken

print()
if num_rounds > 0:
    print("============= Your stats ==============")
    print(f"  Total time taken: {total:.2f} seconds.")
    print(f"Average time taken: {total / num_rounds:.2f} seconds.")
    print(f"Slowest time taken: {highest_timing:.2f} seconds.")
    print(f"Fastest time taken: {lowest_timing:.2f} seconds.")

# 150
# 140
# 190