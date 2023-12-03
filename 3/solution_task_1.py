
def get_adjacent(previous: str, post: str, idx: int):
    if not previous:
        return [post[idx], post[idx - 1], post[idx + 1]]
    elif not post:
        return [previous[idx], previous[idx - 1], previous[idx + 1]]
    return [post[idx], post[idx - 1], post[idx + 1], previous[idx], previous[idx - 1], previous[idx + 1]]


def get_sum(previous: str, post: str, current: str) -> int:
    result = 0
    current_number = ""
    valid = False
    for idx, letter in enumerate(current):
        if letter.isdigit():
            current_number += letter
            adjacent = [current[idx - 1], current[idx + 1]] + get_adjacent(previous, post, idx)
            if not all(char.isdigit() or char == '.' or char == '\n' for char in adjacent):
                valid = True
        else:  # signalizes end of number or periods/symbols
            result += int(current_number) if valid else 0
            current_number, valid = "", False
    return result


def main():
    result = 0
    with open("input.txt") as file:
        current = previous = None
        for line in file:
            if not current:
                current = line
                continue
            post = line
            result += get_sum(previous, post, current)
            previous = current
            current = post
        result += get_sum(previous, post, current)  # last line

    print(f"Total sum is {result}")


if __name__ == "__main__":
    main()
