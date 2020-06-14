import json


js = json.loads(input())
parents = {}
res = {}
child = {}

for d in js:
    parents[d['name']] = d['parents']


for k, v in parents.items():
    child[k] = set()
    print(child[k])
    for par, val in parents.items():
        if k in val:
            child[k].add(par)


def num_parents(graph, elem, visited=None):
    if visited is None:
        visited = set()
    visited.add(elem)
    for node in graph.get(elem):
        num_parents(graph, node, visited)
    return visited


for k in child.keys():
    s = num_parents(child, k)
    res[k] = len(s)


for k, v in sorted(res.items()):
    print(f'{k} : {v}')

