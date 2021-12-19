# Day 14: Extended Polymerization

from collections import Counter


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


def process(rules, iterations, template):

    # count all start elements
    elements = {}
    for element in list(template):
        elements.update({element: elements.get(element, 0)+1})

    # count all tuples
    input_symbols = {}
    for p in range(len(template)-1):
        input_symbols.update({''.join(template[p:p+2]): input_symbols.get(''.join(template[p:p+2]), 0)+1})

    for i in range(iterations):
        output_symbols = {}
        for key, val in input_symbols.items():
            left, right = list(key)
            mid = rules[key]
            output_symbols.update({''.join([left, mid]): output_symbols.get(''.join([left, mid]), 0) + val})
            output_symbols.update({''.join([mid, right]): output_symbols.get(''.join([mid, right]), 0) + val})
            elements.update({mid: elements.get(mid, 0) + val})
        input_symbols = dict(output_symbols)

    return Counter(elements)


def do_the_work(input_file, iterations):
    template, rules = read_file(input_file)

    element_bin = process(rules=rules, iterations=iterations, template=template)
    max_element = max(zip(element_bin.values(), element_bin.keys()))
    min_element = min(zip(element_bin.values(), element_bin.keys()))

    return max_element[0] - min_element[0]


def day14a(input_file):
    return do_the_work(input_file, 10)


def day14b(input_file):
    return do_the_work(input_file, 40)


if __name__ == '__main__':
    print(day14a('day/14/example.txt'))
    print(day14a('day/14/input.txt'))
    print(day14b('day/14/input.txt'))
