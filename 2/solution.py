import operator
from functools import reduce

cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def get_game_info(line: str):
    """
    :param line: line from the input file
    :return: game number and parsed subsets
    """
    game_info, subsets = line.split(":")
    game_number = int(game_info.split(" ")[-1])
    # subsets example 2 red, 5 green; 2 blue, 3 red, 3 green; 3 red, 2 blue; 8 green, 2 red
    result = []
    for subset_raw in subsets.split(";"):
        subset = {}
        for part in subset_raw.split(","):
            amount, color = part.strip().split(" ")
            subset[color] = int(amount)
        result.append(subset)
    return game_number, result


def get_power(subsets: list) -> int:
    """
    :param subsets: line from input
    :return: power of the sets present in single line
    """
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for subset in subsets:
        for k, v in subset.items():
            min_cubes[k] = max(min_cubes[k], v)
    return reduce(operator.mul, min_cubes.values(), 1)


def is_playable(subsets: list) -> bool:
    """
    :param subsets: subset from single input
    :return: True if game is playable, False is not
    """
    for subset in subsets:
        for k, v in subset.items():
            if cubes[k] < v:
                return False
    return True


def main():
    result_task_1 = result_task_2 = 0
    with open("input.txt") as file:
        for line in file:
            game_number, subsets = get_game_info(line)
            result_task_1 += game_number if is_playable(subsets) else 0
            result_task_2 += get_power(subsets)

    print(f"Task 1: Total sum is {result_task_1}")
    print(f"Task 2: Total sum is {result_task_2}")


if __name__ == "__main__":
    main()
