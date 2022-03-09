def findpos(l,v):
    for i in range(len(l)):
        if l[i]==v:
            pos=i
            break
        else:
            pos=-1
        return(pos)

l=[1,2,31,22]
findpos(l,2)
print(l)