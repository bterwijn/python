
A = {1, 2, 10, 20}
B =       {10, 20, 100, 200}

print(A.union(B))         # {1, 2, 100, 200, 10, 20},  print(A | B)
print(A.intersection(B))  # {10, 20},                  print(A & B)
print(A.difference(B))    # {1, 2},                    print(A - B)
print(A.symmetric_difference(B))  # {1, 2, 100, 200},  print(A ^ B)

print({1, 2}.isdisjoint({10, 20}))  # True
print({1, 2} < {1, 2, 3})           # True (proper subset)
print({1, 2, 3} <= {1, 2, 3})       # True (subset)
print({1, 2, 3} > {1, 2})           # True (proper superset)
print({1, 2, 3} >= {1, 2, 3})       # True (superset)
