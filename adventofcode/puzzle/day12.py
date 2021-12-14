def read_connections():
    connections = {}
    with open('day/12/input.txt') as fv:
        for row in fv:
            points = row[:-1].split('-')

            if len(points) != 2:
                raise Exception('corrupted input')

            if points[0] in connections:
                connections[points[0]].append(points[1])
            else:
                connections[points[0]] = [points[1]]

            if points[1] in connections:
                connections[points[1]].append(points[0])
            else:
                connections[points[1]] = [points[0]]

    return connections


def restriction_a(next_cave, visited_caves):
    if next_cave.isupper():
        return True
    elif next_cave.islower():
        if next_cave not in visited_caves:
            return True
    return False


def restriction_b(next_cave, visited_caves):
    if next_cave.isupper():
        return True
    elif next_cave.islower():
        if next_cave not in visited_caves:
            return True
        else:
            visited_lowercase_caves = [cave for cave in visited_caves if cave.islower()]
            if len(set(visited_lowercase_caves)) == len(visited_lowercase_caves):
                return True
    return False


def scan_cave(connections, visited_caves, restriction):
    next_caves = connections[visited_caves[-1]]
    paths = []
    for next_cave in next_caves:
        if next_cave == 'start':
            pass
        elif next_cave == 'end':
            contains_small_cave = False
            for cave in visited_caves:
                if cave.islower():
                    contains_small_cave = True
            if contains_small_cave:
                paths.append(visited_caves + [next_cave])
        elif restriction(next_cave, visited_caves):
            longer_paths = scan_cave(connections, visited_caves + [next_cave], restriction)
            paths.extend(longer_paths)
    return paths


def day12a():
    connections = read_connections()
    paths = scan_cave(connections, ['start'], restriction_a)
    return len(paths)


def day12b():
    connections = read_connections()
    paths = scan_cave(connections, ['start'], restriction_b)
    return len(paths)


if __name__ == '__main__':
    print(day12a())
    print(day12b())

