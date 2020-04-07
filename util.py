def Maxx(i):
    j=0;
    m=i[j];
    for j in range(len(i)):
        if j==len(i)-1:
            break
        elif (i[j] < i[j+1]):
            m=i[j+1]
    return m

