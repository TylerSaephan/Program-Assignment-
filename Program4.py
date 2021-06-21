
def fibonacciFinder (max):
    i = 0 
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j
        j = k
        return("Fibonacci yay")

def primeFinder (max):
    for i in range(2,max):
        for j in range(2,max):
            if i % j == 0:
                break
            else:
                print(1)
            return(max) 

#print(fibonacciFinder(100), primeFinder(15))

def trianglearea(base, height):
    area = base*height/2
    return area 

m = 5
n = 5
arelist = [0]*n*m
i = 0
for b in range(0, n):
    for h in range(0, m):
        areaList[1] = trianglearea(b, h)
        i += 5 