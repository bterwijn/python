
v = 1
v2 = v
v += 100
print("v:",v,"v2:",v2) # v: 101 v2: 1

v = [1,2,3]
v2 = v
v.append(100)
print("v:",v,"v2:",v2) # v: [1, 2, 3, 100] v2: [1, 2, 3, 100]

import copy

w = [1,2,3]
w2 = copy.deepcopy(w)
w.append(100)
print("w:",w,"w2:",w2) # w: [1, 2, 3, 100] w2: [1, 2, 3]

print(id(v), id(v2)) # 139992454782848 139992454782848 
print(v is v2)       # True
 
print(id(w), id(w2)) # 139992453441280 139992453556992
print(w is w2)       # False
