def get_sum_in_string(string):
    total = 0
    for char in string:
        if char in "0123456789":
            total = total + int(char)
    return total


def main():

    print(get_sum_in_string("2514"))    # 12
    print(get_sum_in_string("4295"))    # 20
    print(get_sum_in_string("1112345"))    # 17
    print(get_sum_in_string("2ab70"))    # 9


if __name__ == '__main__':
    main()
