# Day 14: Extended Polymerization

def read_file(input_files):
    polymer_template = ''
    pair_insertion_rules = {}

    with open(input_files) as fv:
        row = fv.readline()
        polymer_template = row[:-1]

        row = fv.readline()
        if row != '\n':
            raise Exception('empty line expected')

        row = fv.readline()
        while row != '':
            tmp = row.split(' -> ')
            pair_insertion_rules[tmp[0]] = tmp[1][:-1]
            row = fv.readline()

    return polymer_template, pair_insertion_rules


def process(template, rules, iterations):
    if iterations <= 0:
        if iterations == 0:
            return template
        else:
            raise Exception('invalid amount of process iterations')
    new_polymer = [template[0]]

    for i in range(0, len(template)-1):
        key = ''.join(template[i:i+2])
        if key in rules:
            new_polymer.append(rules[key])
        new_polymer.append(template[i+1])
    
    return process(new_polymer, rules, iterations-1)


def count_elements(polymer):
    element_bin = {}
    for element in polymer:
        if element in element_bin:
            element_bin[element] += 1
        else:
            element_bin[element] = 1
    return element_bin


def day14a(input_file):
    template, rules = read_file(input_file)
    iterations = 10
    processed_polymer = process(list(template), rules, iterations)
    element_bin = count_elements(processed_polymer)
    max_element = max(zip(element_bin.values(), element_bin.keys()))
    min_element = min(zip(element_bin.values(), element_bin.keys()))

    return max_element[0] - min_element[0]


if __name__ == '__main__':
    print(day14a('day/14/example.txt'))
    print(day14a('day/14/input.txt'))
