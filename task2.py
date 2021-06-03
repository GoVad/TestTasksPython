import string
import numpy.random as r


def find_rep_id(arr):
    for i in range(len(arr) - 1):
        for k in range(i + 1, len(arr)):
            if arr[i] == arr[k]:
                return arr[k]
    return -1


a = []
for i in range(20):
    a.append(string.ascii_lowercase[r.randint(len(string.ascii_lowercase))])
print(a)
print(find_rep_id(a))
a = ['a', 'b', 'c', 'd', 'e', 'f']
print(a)
print(find_rep_id(a))
