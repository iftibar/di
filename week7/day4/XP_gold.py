import random

total = 0


def throw_dice():
    num = random.randint(1, 6)
    return num


def throw_until_double():
    dice1 = throw_dice()
    dice2 = throw_dice()
    print(dice2, dice1)
    if dice1 == dice2:
        return 1
    return 1 + throw_until_double()


print(throw_until_double())


def main():
    dict = {}
    for i in range(1, 100):
        dict[i] = throw_until_double()
    total_throws = sum(dict.values())
    print(f" 1. total throws was {total_throws}\n 2. average throws to reach double was {total_throws / 100}")


main()
