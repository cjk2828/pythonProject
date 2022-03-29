#8번
def listProd(a,b):
    sum = 0
    for steps in range(len(a)):
        sum = sum + a[steps]*b[steps]
    print(sum)
    return
a = [1,0,1]
b = [1,1,2]
listProd(a,b)