import re


def main():
    result = 0
    with open("input.txt") as file:
        for line in file:
            digits = re.findall(r'\d', line)
            if digits:
                result += int(digits[0] + digits[-1])

    print(f"Total sum is {result}")


if __name__ == "__main__":
    main()
