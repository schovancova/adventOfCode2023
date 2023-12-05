def main():
    result_task_2 = []
    result_task_1 = 0
    with open("input.txt") as file:
        for idx, line in enumerate(file):
            win, nums = [num.strip().split() for num in line.split(":")[1].split("|")]
            points = len(list(filter(lambda x: x in win, nums)))
            result_task_2.append([points, 1])
            result_task_1 += pow(2, points - 1) if points else 0
            for k, v in enumerate(result_task_2):
                if k == idx or not v[0]: continue
                v[0] -= 1
                result_task_2[idx][1] += 1 * v[1]
    print(f"Task 1: {result_task_1}")
    print(f"Task 2: {sum(entry[1] for entry in result_task_2)}")


if __name__ == "__main__":
    main()
