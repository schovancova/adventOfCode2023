The advent 2023 begins and that means I get to do the annual coding challenges!


- **Language** python 3.10
- **Website** https://adventofcode.com/2023/


    transformations = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        # no zero in assignment
    }

    """
    Find numbers on the start or end of string.
    Default option is to search from the start. If searching from the end, reverse is applied. 
    """
    def find_numbers(line: str, start: bool = True) -> str:
        temp = ""
        if not start:
            # searching from the end, reverse line
            line = line[::-1]
        for letter in line:
            if letter.isdigit():
                return letter
            temp += letter
            for key in transformations.keys():
                if key in (temp if start else temp[::-1]):
                    return str(transformations[key])

    def main():
        result = 0
        with open("input.txt") as file:
            for line in file:
                first_num = find_numbers(line, True)
                last_num = find_numbers(line, False)
                result += int(first_num + last_num)
        print(f"Total sum is {result}")

    if __name__ == "__main__":
        main()
