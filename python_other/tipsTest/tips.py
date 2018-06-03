def sortby_inplace(somelist, n):
    somelist[:] = [(x[n], x) for x in somelist]
    somelist.sort()
    print(somelist)
    somelist[:] = [val for (key, val) in somelist]
    return


somelist = [(1, 2, 'def'), (2, -4, 'ghi'), (3, 6, 'abc')]
# sortby_inplace(somelist, 1)
# print(somelist)

import operator
somelist.sort(key=operator.itemgetter(1))

print(somelist)

slist = ["1","2","3","4"]
s = "_".join(slist)
print(s)

from collections import defaultdict

s = 'mississippi'
d = defaultdict(int)
for k in s:
  d[k] += 1
print(d)

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
  d[k].add(v)
 
print(d)

def doit1():
    import string ###### import statement inside function
    string.lower('Python')

for num in range(100000):
    doit1()

import string
string.