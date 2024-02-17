infinity = float("inf")

# node
graph = {}

# weights
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"] = {}
graph["c"]["fin"] = 3
graph["c"]["d"] = 6
graph["d"] = {}
graph["d"]["fin"] = 1
graph["fin"] = {}  # last node doesn't have have neighborhoods

# costs
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# parents

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

# massive for check
processed = []


def find_lowest_costs_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node


node = find_lowest_costs_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
        processed.append(node)
        node = find_lowest_costs_node(costs)

print(graph["start"].keys())  # get all neighborhoods start
print(graph["start"]["a"])  # get weight start -> a
print(costs["d"])  # get lowest/shortest/cheaper/  costs
print(costs["fin"])
