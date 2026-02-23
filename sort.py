tuple_list = [(2,3 ), (1, 2), (5,9), (6, 16), (5, 25)]
sorted_list = sorted(tuple_list, key=lambda x: x[1])
print("Sorted list of tuples by last element:")
print(sorted_list)
