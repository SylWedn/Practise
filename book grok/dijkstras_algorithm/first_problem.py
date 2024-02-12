graph = {}
graph["start"] = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["d"] = {}
graph["fin"] = {}

graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"]["fin"] = 3
graph["c"]["d"] = 6
graph["d"]["fin"] = 1


print(graph["start"].keys())
print
graph(["start"]["a"])


