def read_movements():
    movements = []
    with open('day/2/input.txt') as fv:
        for row in fv:
            items = row.split()
            movements.append([items[0], int(items[1])])
    return movements


def day02a():
    movements = read_movements()
    h_pos = 0
    depth = 0
    down = 0;
    up = 0;
    for movement in movements:
        if 'forward' == movement[0]:
            h_pos = h_pos + movement[1]
        elif 'up' == movement[0]:
            depth = depth - movement[1]
        elif 'down' == movement[0]:
            depth = depth + movement[1]

    return h_pos * depth


def day02b():
    movements = read_movements()
    h_pos = 0
    depth = 0
    aim = 0

    for movement in movements:
        if 'forward' == movement[0]:
            h_pos = h_pos + movement[1]
            depth = depth + aim * movement[1]
        elif 'up' == movement[0]:
            aim = aim - movement[1]
        elif 'down' == movement[0]:
            aim = aim + movement[1]

    return h_pos * depth


if __name__ == '__main__':
    print('%d is the multiplication of the final horizontal position by the final depth' % (day02a()))
    print('%d is the multiplication of the final horizontal position by the final depth' % (day02b()))
