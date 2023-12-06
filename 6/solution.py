import math


def quadratic_eq(b, c):
    discriminant = b ** 2 - 4 * c
    solr = sorted([(-b + math.sqrt(discriminant)) / 2, (-b - math.sqrt(discriminant)) / 2])
    return math.floor(solr[1]) - math.ceil(solr[0]) + 1


def task_1():
    win = 1
    with open("input.txt") as file:
        t, d = [list(map(int, t.split(":")[1].strip().split())) for t in file.readlines()]
    for t1, d1 in list(zip(t, d)):
        this_win = quadratic_eq(-t1, d1)
        win *= this_win if this_win else 1
    print(f"Task1: {win}")


def task_2():
    with open("input.txt") as file:
        t, d = [int("".join(t.split(":")[1].strip().split())) for t in file.readlines()]
        print(f"Task2: {quadratic_eq(-t, d)}")


if __name__ == "__main__":
    task_1()
    task_2()
