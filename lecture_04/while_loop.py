# 1. init pre-test condition
# while 2. condition is True
#     3. statement(s)
#        ...
#        ...
#     4. update variable in condition (to eventually False)
# Usage: Unknown number of iterations, Indefinite loops

count = 0  # 1. init
while count < 5:    # 2. condition
    print(count)    # 3. statements
    count = count + 1    # 4. update var
# 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 (until 2 is false)
print("==== End of program ===")