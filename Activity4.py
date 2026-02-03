friends = ["Alice", "Bob", "Carol"]

friends.append("Dave")
friends.insert(1, "Jayvan")
friends.remove("Bob")

print("Original list: ", end="")
for i in range(len(friends)):
    if i == len(friends) - 1:
        print("and " + friends[i])
    else:
        print(friends[i], end=", ")

friends.sort()

print("Sorted list: ", end="")
for i in range(len(friends)):
    if i == len(friends) - 1:
        print("and " + friends[i])
    else:
        print(friends[i], end=", ")