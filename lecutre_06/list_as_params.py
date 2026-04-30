def find_median(number_list):
    """Assume that number_list is not empty."""
    sorted_numbers = sorted(number_list)  # first sort
    # [1, 3, 6, 7, 8, 9, 10]
    if len(number_list) % 2 == 1:   # odd number, get middle value
        middle_index = len(number_list) // 2  # int(3.5) = 3
        median = sorted_numbers[middle_index]
    else:    # [1, 3, 5, 6, 7, 8, 9, 10]
        middle_right = len(number_list) // 2    # 7
        middle_left = middle_right - 1          # 6
        median = sorted_numbers[middle_left] + sorted_numbers[middle_right]
        median = median / 2
    return median

def add_zero(n_l):   # pass by reference
    n_l.append(0)    # n_l points to the list passed in

def change_this(number):     # pass by value
    number = 9999            # number is a local copy

def main():
    number_list = [1, 3, 5, 6, 7, 8, 9, 10]
    median = find_median(number_list)
    print(median)
    add_zero(number_list)
    add_zero(number_list)
    add_zero(number_list)
    print(number_list)

    my_number = 10
    change_this(my_number)
    print(my_number)

main()