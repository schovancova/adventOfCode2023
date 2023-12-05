def calc(seeds, m):
    return [min(((d + (seed - s)) for d, s, l in m if seed in range(s, s + l + 1)), default=seed) for seed in seeds]


def main():
    seeds = []
    m = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if not seeds: seeds = list(map(int, line.split(":")[1].strip().split(" ")))
            if line and ":" in line:
                seeds, m = calc(seeds, m), []
            elif line:
                m.append(list(map(int, line.split())))
    seeds = calc(seeds, m)
    print(seeds)

    print(f"Total sum is {min(seeds)}")


if __name__ == "__main__":
    main()
