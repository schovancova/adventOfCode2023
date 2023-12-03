def get_gear_indexes(lines, gear_indexes):
    for line in lines:
        current_number = ""
        valid_for = set()  # on current
        for idx, letter in enumerate(line):
            if letter.isdigit():
                current_number += letter
                valid_for.update(set(id for id in [idx, idx + 1, idx - 1] if id in gear_indexes))
            else:
                if current_number and valid_for:
                    [gear_indexes[valid].append(int(current_number)) for valid in valid_for]
                current_number = ""
                valid_for = set()
    return gear_indexes


def get_gear_sum(previous, post, current):
    if "*" not in current:
        return 0
    gear_indexes = {i: [] for i, char in enumerate(current) if char == '*'}
    adjacent = get_gear_indexes([previous, post, current], gear_indexes)
    return sum(v[0] * v[1] if len(v) == 2 else 0 for v in adjacent.values())


def main():
    result = 0
    with open("input.txt") as file:
        current = previous = None
        for line in file:
            if not current:
                current = line
                continue
            result += get_gear_sum(previous, line, current)
            previous, current = current, line
        result += get_gear_sum(previous, [], current)  # last line

    print(f"Total sum is {result}")


if __name__ == "__main__":
    main()
