friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(f"difference1: {local_friends}")

local_friends = abroad.difference(friends)
print(f"difference2: {local_friends}")

union = friends.union(abroad)
print(f"union: {union}")

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(f"intersection: {both}")