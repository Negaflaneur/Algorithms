def find_closest_node(costs):
    lowest_cost = float('inf')
    cheapest_node = None
    for node in costs:
        if (costs[node] < lowest_cost) and (node not in processed_nodes):
            lowest_cost = costs[node]
            cheapest_node = node
    return cheapest_node

## defining the nodes of the graph
graph = {}
graph['start']={}
graph['start']['LP'] = 5
graph['start']['poster'] = 0
graph['LP'] = {}
graph['LP']['guitar'] = 15
graph['LP']['drum'] = 20
graph['poster'] = {}
graph['poster']['drum'] = 35
graph['poster']['guitar'] =30
graph['guitar'] = {}
graph['guitar']['finish']= 20
graph['drum'] = {}
graph['drum']['finish'] = 10
graph['finish'] = {}

## defining the costs of each individual node of the graph regardless of the parent
infinity_value = float("inf")
costs = {}
costs['LP'] = 5
costs['poster'] = 0
costs['drum'] = 35
costs['guitar'] = 15
costs['finish'] = infinity_value

##defining the parents of the nodes 
parents= {}
parents['LP'] = "start"
parents['poster'] = "start"
parents['finish'] = None

#defining the array of processed nodes 
processed_nodes = []

node = find_closest_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for sub_node in neighbours.keys():
        path_cost = cost + neighbours[sub_node]
        if costs[sub_node]  > path_cost:
            costs[sub_node] = path_cost
            parents[sub_node] = node
    processed_nodes.append(node)
    node = find_closest_node(costs)

print(costs)
print(costs['finish'])
print(parents)