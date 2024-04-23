def permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for perm in permutations(lst[1:]):
            for i in range(len(lst)):
                yield perm[:i] + [lst[0]] + perm[i:]

# Пример использования:
my_list = [1, 2, 3]
for perm in permutations(my_list):
    print(perm)
