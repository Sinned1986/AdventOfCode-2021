# Day 14: Extended Polymerization

from collections import Counter
import os
from multiprocessing import Pool as ThreadPool
from functools import partial


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
    if iterations <= 0:
        if iterations == 0:
            return Counter(template[:-1])
        else:
            raise Exception('invalid amount of process iterations')
    new_polymer = [template[0]]

    for i in range(0, len(template)-1):
        key = ''.join(template[i:i+2])
        if key in rules:
            new_polymer.append(rules[key])
        new_polymer.append(template[i+1])

    if new_polymer == template:
        return Counter(template[:-1])

    element_bin = Counter()
    for i in range(0, len(new_polymer)-1):
        sub_bin = process(template=new_polymer[i:i+2], rules=rules, iterations=iterations-1)
        element_bin.update(sub_bin)
    return element_bin


def count_elements(polymer):
    element_bin = {}
    for element in polymer:
        if element in element_bin:
            element_bin[element] += 1
        else:
            element_bin[element] = 1
    return element_bin


def do_the_work(input_file, iterations):
    template, rules = read_file(input_file)

    mt_pool = ThreadPool(os.cpu_count())
    mt_templates = []
    for i in range(0, len(template)-1):
        mt_templates.append(template[i:i+2])

    mt_func = partial(process, rules, iterations)
    mt_results = mt_pool.map(mt_func, mt_templates)
    element_bin = Counter()

    for sub_bin in mt_results:
        element_bin.update(sub_bin)
    if template[-1] in element_bin:
        element_bin[template[-1]] += 1
    else:
        element_bin[template[-1]] = 1

    mt_pool.close()
    mt_pool.join()

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
