def InsertionSort(l):
    for sliceEnd in range(len(l)):
        pos=sliceEnd
        while(pos>0 and l[pos]<l[pos-1]):
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos=pos-1

l=[22,11,44,33,55]
InsertionSort(l)
print(l)
