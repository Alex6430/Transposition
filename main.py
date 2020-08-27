print("Введите мощность множества:")
m=int(input())
N= [i+1 for i in range(m)]
print("Введите перестановку:")
P = []
for i in range(m):
    P.append(int(input()))
# P = [3,1,4,2,5,8,10,9,6,7,11]
res = []

print(N)
print(P)
i=0
while(True):
    n = N[i]
    p = P[i]
    if(n==p):
        res.append([n])
        N[i]=0
        if N[1:]==N[:-1]:
            break
        else:
            for k in N:
                if k != 0:
                    i = N.index(k)
                    break
            continue
    else:
        j = i
        r = [n]
        while (p != n):
            p = P[j]
            N[N.index(p)]=0
            j = p - 1
            r.append(p)
        res.append(r)
        for k in N:
            if k!=0:
                i=N.index(k)
                break

        if N[1:]==N[:-1]:
            break

# print(res)
def pars(mas):
    for arr in mas:
        if len(arr)>1:
            arr.pop()
            for i in range(len(arr)):
                if i!=len(arr)-1:
                    print("("+str(arr[i])+","+str(arr[i+1])+")o",end="")
        elif len(arr)==1:
            print("("+str(arr)+")o", end="")
    print(" N")

pars(res)