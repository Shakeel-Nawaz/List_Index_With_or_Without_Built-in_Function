x = ["India","USA","China","India","UK","USA","China","India"]
idx = 0
temp = []
for i in x:
    if i not in temp:
        print(i,end=' : ')
        for j in x:
            if j == i:
                print(idx,end=" ")
                idx += 1
            else:
                idx += 1
        print(' ,',end='\n')
    temp.append(i)
