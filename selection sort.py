import sys
def SelectionSort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i] < l[minpos]:
                minpos=i
        (l[start],l[minpos])=(l[minpos],l[start])

l=[12,2,33,54,22,11]
SelectionSort(l)
print(l)