from collections import defaultdict

with open("./inputs/23input.txt", "r") as f:
    data = f.read()

connections = data.splitlines()
graph = defaultdict(set)

for connection in connections:
    a, b = connection.split("-")
    graph[a].add(b)
    graph[b].add(a)

# Bron-Kerbosch algorithm for finding the largest clique
def bron_kerbosch(r, p, x, graph):
    if not p and not x:
        yield r
    while p:
        v = p.pop()
        yield from bron_kerbosch(r.union({v}), p.intersection(graph[v]), x.intersection(graph[v]), graph)
        x.add(v)

def find_largest_clique(graph):
    max_clique = set()
    nodes = set(graph.keys())
    for clique in bron_kerbosch(set(), nodes, set(), graph):
        if len(clique) > len(max_clique):
            max_clique = clique
    return max_clique

largest_clique = find_largest_clique(graph)

# Sort the largest clique alphabetically and create the password
password = ",".join(sorted(largest_clique))

# Output the results
print("Largest set of fully connected computers:", largest_clique)
print("Password to get into the LAN party:", password)
