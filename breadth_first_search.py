from collections import deque

def is_mango_seller(person):
    mango_seller = False
    if person[0] == 'm':
        mango_seller = True
    return mango_seller

graph = {}
graph["you"] = ["alice", "bob", "jack"]
graph["bob"] = ["lex", "peggy"]
graph["alice"] = ["peggy"]
graph["jack"] = ["tom", "malex"]
graph["lex"] = []
graph["peggy"] = []
graph["tom"] = []
graph["malex"] = []

checked_nodes = {}

search_queue = deque()
search_queue += graph["you"]
while search_queue:
    person_checking = search_queue.popleft()
    if is_mango_seller(person_checking) and (not(checked_nodes.get(person_checking))):
        print(person_checking, "is a mango seller")
        mango_seller_status = True
        break
    else:
        search_queue += graph[person_checking]
        checked_nodes[person_checking] = True
        mango_seller_status = False

if mango_seller_status != True:
    print("No mango sellers around")

