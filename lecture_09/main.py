from coin import Coin

def reset_all_coins(coins):
    """Reset all coins to their initial state."""
    for i in range(len(coins)):
        coins[i].side_up = "Heads"


def main():
    """Start of program."""
    coins = []
    for i in range(5):
        coins.append(Coin())

    for i in range(len(coins)):
        coins[i].toss()
        print(coins[i])  # call __str__()

    print("---- Reset all coins ----")
    reset_all_coins(coins)
    for i in range(len(coins)):
        print(coins[i])  # call __str__()


if __name__ == "__main__":
    main()