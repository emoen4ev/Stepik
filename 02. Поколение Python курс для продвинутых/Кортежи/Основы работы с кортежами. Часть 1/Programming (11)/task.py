tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]

# non_empty_tuples = [tuples[i] for i in range(len(tuples)) if tuples[i]]

non_empty_tuples = [el for el in tuples if el]

print(non_empty_tuples)