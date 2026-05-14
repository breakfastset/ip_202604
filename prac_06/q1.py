
def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    valid_numbers = []

    # filter the numbers in the valid list
    for number in numbers:
        if 0 <= number <= 100:
            valid_numbers.append(number)

    total = sum(valid_numbers)
    print(f"The total of all numbers is {total}")

    if len(valid_numbers) > 0:  # if at least 1 element
        average = total / len(valid_numbers)
        print(f"The average number is {average}")

if __name__ == '__main__':
    main()
