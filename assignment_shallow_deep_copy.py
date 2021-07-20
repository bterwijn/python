import copy

list_of_lists = [[1,2],[3]]
print(list_of_lists)

assignment = list_of_lists
shallow    = copy.copy(list_of_lists)
deep       = copy.deepcopy(list_of_lists)
print("assignment:", assignment, "shallow:", shallow, "deep:",deep)

list_of_lists[0] = [1111]
print("assignment:", assignment, "shallow:", shallow, "deep:",deep)

list_of_lists[1].append(2222)
print("assignment:", assignment, "shallow:", shallow, "deep:",deep)
