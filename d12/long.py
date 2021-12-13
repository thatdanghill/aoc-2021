import sys
all_edges = [line[:-1].split('-') for line in open(sys.argv[1])]

def find_next_nodes(node):
    next_list = []
    for edge in all_edges:
        if edge[0] == node:
            next_list.append(edge[1])
        if edge[1] == node:
            next_list.append(edge[0])
    return next_list


def all_end(path_list):
    return all([path[-1]=='end' for path in path_list])


def is_valid_next_node(path, node, num_allowed):
    if node == 'start':
        return False
    if node == 'end' and node not in path:
        return True
    if not node.islower() or node not in path:
        return True
    return all([path.count(i) < num_allowed for i in path if i.islower()])

def run_search(num_allowed):
    paths = [['start']]
    while not all_end(paths):
        new_paths = []
        for path in paths:
            node_paths = []
            if path[-1] != 'end':
                nexts = find_next_nodes(path[-1])
                for node in nexts:
                    if is_valid_next_node(path, node, num_allowed):
                        node_paths.append(path + [node])
            else:
                node_paths.append(path)
            new_paths += node_paths
        paths = new_paths
    paths = [path for path in paths if path[-1] == 'end']
    return paths

print(f'Silver: {len(run_search(1))}')
print(f'Gold: {len(run_search(2))}')
