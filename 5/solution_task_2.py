def get(depth, seed_x, seed_y, map_ranges):
    for range_x, range_y, dst in map_ranges[depth]:
        if range_x <= seed_x < range_y:
            if seed_y < range_y:
                new_a, new_b = seed_x - range_x + dst, seed_y - range_x + dst
                return new_a if depth == 6 else get(depth + 1, new_a, new_b, map_ranges)
            else:
                return min(get(depth, seed_x, range_y - 1, map_ranges), get(depth, range_y, seed_y, map_ranges))
    return seed_x if depth == 6 else get(depth + 1, seed_x, seed_y, map_ranges)


def main():
    with open("input.txt") as f:
        ls = f.read().split("\n\n")

    seeds, maps = [int(n) for n in ls[0].split(": ")[1].split()], [
        [[int(m) for m in n.split()] for n in l.split(":\n")[1].splitlines()]
        for l in ls[1:]
    ]

    map_ranges = [[] for _ in range(7)]
    for depth, m in enumerate(maps):
        for dst, src, l in m:
            map_ranges[depth].append([src, src + l, dst])

    res = []
    for i in range(0, len(seeds), 2):
        res.append(get(0, seeds[i], seeds[i] + seeds[i + 1], map_ranges))
    print(min(res))


if __name__ == "__main__":
    main()
