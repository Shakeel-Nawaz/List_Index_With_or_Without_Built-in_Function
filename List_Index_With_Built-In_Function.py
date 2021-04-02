x = ["India","USA","China","India","UK","USA","China","India"]
xy = []
for i in x:
    if i in xy:
        pass
    else:
        xy.append(i)
# y = list(set(x))
# print(y)
lst = []
for i in xy:
    ab = x.count(i)
    j = 0
    lst.append(i)
    lst.append(':')
    for _ in range(ab):
        xyz = x.index(i,j) 
        lst.append(xyz)
        j = xyz +1
    lst.append(',')
print(*lst)
