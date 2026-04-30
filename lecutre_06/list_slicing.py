fruits = ["apple", "pineapple", "durian", "banana",
          "cherry", "pear", "honeydew", "rock melon",
          "watermelon", "starfruit", "mangosteen"]

# slice = list[start:end:step], where end is excluded
fruits_1 = fruits[:4]  # 0, 1, 2, 3
print(fruits_1)   # apple ... banana

fruits_2 = fruits[2:7]  # 2... 6
print(fruits_2)  # durian... honeydew

fruits_3 = fruits[7:]  # 7 ... 10
print(fruits_3)  # rock melon... mangosteen

fruits_4 = fruits[1:8:2] # 1, 3, 5, 7
print(fruits_4)   # pineapple, banana, pear, rock melon

fruits_5 = fruits[::-1]  # reverse
print(fruits_5)