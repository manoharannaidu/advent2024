from collections import defaultdict

with open("./inputs/23input.txt", "r") as f:
    data = f.read()

connections = data.splitlines()


graph = defaultdict(set)

for connection in connections:
    a, b = connection.split("-")
    graph[a].add(b)
    graph[b].add(a)

# Find all sets of three interconnected computers
sets_of_three = set()

for node in graph:
    for neighbor1 in graph[node]:
        for neighbor2 in graph[node]:
            if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                # Create a sorted tuple to ensure uniqueness
                triple = tuple(sorted([node, neighbor1, neighbor2]))
                sets_of_three.add(triple)

# Filter sets where at least one computer's name starts with 't'
sets_with_t = [s for s in sets_of_three if any(computer.startswith('t') for computer in s)]

# Output the results
print("Sets of three containing at least one 't'-starting computer:", len(sets_with_t))
