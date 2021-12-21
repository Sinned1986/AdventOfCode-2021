# Day 15: Chiton

import numpy as np


def read_map(file_name):
    cavern_map_rows = []
    with open(file_name) as fv:
        for row in fv:
            if row != '':
                cavern_map_rows.append(np.array(list(map(int, list(row[:-1]))), dtype=np.uint8))
    return np.stack(cavern_map_rows)


def generate_map_for_part_2(cavern_array, h, v):

    # extend array to te left
    tmp_array = cavern_array-1
    for i in range(1, h):
        tmp_array = np.hstack((tmp_array, (cavern_array+i-1) % 9))

    # extend array to the bottom
    new_array = tmp_array
    for i in range(1, v):
        new_array = np.vstack((new_array, (tmp_array+i) % 9))

    return new_array+1


def calc_dijkstra(cavern_array, start, target):
    visited_array = np.zeros(cavern_array.shape, dtype=bool)
    cost_array = np.full(shape=cavern_array.shape, fill_value=np.iinfo(int).max, dtype=int)
    cost_array[start[0], start[1]] = 3
    start_cost = 0
    unvisited_nodes = {start_cost: [start]}
    max_y = cavern_array.shape[0]-1
    max_x = cavern_array.shape[1]-1
    while True:
        sorted_nodes = sorted(unvisited_nodes)
        min_node_cost = sorted_nodes[0]
        min_node_cost_positions = unvisited_nodes.pop(min_node_cost)
        for node_pos in min_node_cost_positions:
            if visited_array[node_pos[0], node_pos[1]]:
                continue
            visited_array[node_pos[0], node_pos[1]] = True

            # abort because we found the target
            if node_pos == target:
                return min_node_cost

            node_cost = int(cavern_array[node_pos[0], node_pos[1]]) + min_node_cost
            if node_pos[0] > 0:
                neighbour = [node_pos[0] - 1, node_pos[1]]
                if not visited_array[neighbour[0], neighbour[1]] and node_cost < cost_array[neighbour[0], neighbour[1]]:
                    old_value = unvisited_nodes.get(node_cost, [])
                    old_value.append(neighbour)
                    new_dict = {node_cost: old_value}
                    unvisited_nodes.update(new_dict)

            if node_pos[0] < max_y:
                neighbour = [node_pos[0] + 1, node_pos[1]]
                if not visited_array[neighbour[0], neighbour[1]] and node_cost < cost_array[neighbour[0], neighbour[1]]:
                    old_value = unvisited_nodes.get(node_cost, [])
                    old_value.append(neighbour)
                    new_dict = {node_cost: old_value}
                    unvisited_nodes.update(new_dict)

            if node_pos[1] > 0:
                neighbour = [node_pos[0], node_pos[1] - 1]
                if not visited_array[neighbour[0], neighbour[1]] and node_cost < cost_array[neighbour[0], neighbour[1]]:
                    old_value = unvisited_nodes.get(node_cost, [])
                    old_value.append(neighbour)
                    new_dict = {node_cost: old_value}
                    unvisited_nodes.update(new_dict)

            if node_pos[1] < max_x:
                neighbour = [node_pos[0], node_pos[1] + 1]
                if not visited_array[neighbour[0], neighbour[1]] and node_cost < cost_array[neighbour[0], neighbour[1]]:
                    old_value = unvisited_nodes.get(node_cost, [])
                    old_value.append(neighbour)
                    new_dict = {node_cost: old_value}
                    unvisited_nodes.update(new_dict)


def day15a(input_file_name):
    cavern_array = read_map(input_file_name)

    calced_costs = calc_dijkstra(cavern_array=cavern_array, start=[cavern_array.shape[0]-1, cavern_array.shape[1] - 1], target=[0, 0])
    return calced_costs


def day15b(input_file_name):
    cavern_array = generate_map_for_part_2(read_map(input_file_name), h=5, v=5)

    calced_costs = calc_dijkstra(cavern_array=cavern_array, start=[cavern_array.shape[0]-1, cavern_array.shape[1] - 1], target=[0, 0])
    return calced_costs


if __name__ == '__main__':
    print(day15a('day/15/example.txt'))
    print(day15a('day/15/input.txt'))
    print(day15b('day/15/example.txt'))
    print(day15b('day/15/input.txt'))

