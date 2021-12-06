def calc_polulation(cycles):
    lanternfishes = []
    for i in range(0, 9):
        lanternfishes.append(0)

    with open('day/6/input.txt') as fv:
        for row in fv:
            for str_val in row.split(','):
                int_val = int(str_val)
                assert(int_val >= 0)
                assert(int_val < 6)
                lanternfishes[int_val] += 1

    print(lanternfishes)
    for day in range(0, cycles):
        fishes_ready_to_breed = lanternfishes.pop(0)
        lanternfishes.append(fishes_ready_to_breed)
        lanternfishes[6] += fishes_ready_to_breed
        print(lanternfishes)
    return sum(lanternfishes)


def day06a():
    return calc_polulation(80)


def day06b():
    return calc_polulation(256)


if __name__ == '__main__':
    print(day06a())
    print(day06b())
