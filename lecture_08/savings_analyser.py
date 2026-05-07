def read_data(filename):
    savings_list = []   # a list of floats read from the file.
    file_in = open(filename, "r")
    for line in file_in:
        amount = float(line)
        savings_list.append(amount)
    file_in.close()
    return savings_list


def main():

    savings = []
    # 1. read the savings.txt into a list of savings
    savings = read_data("savings.txt")
    print(savings)   # debugging

    # 2. calculate the total and hence the average
    total_savings = sum(savings)
    average_savings = total_savings / len(savings)
    print("---- Savings Analyser Report ----")
    print(f"  Total savings: ${total_savings:.2f}")
    print(f"Average savings: ${average_savings:.2f}")


if __name__ == '__main__':
    main()