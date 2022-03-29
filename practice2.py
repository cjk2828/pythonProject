#2번
n = int(input("자연수 N을 입력하세요 : "))
sum = 0;
for steps in range(n+1):
    if steps%2 == 0 :
        sum = sum + steps
print(sum)