#3번
def factorial(a):
    sum = 1
    for steps in range(a):
        sum = sum*(steps+1)
    print(sum)

n = int(input("자연수 N을 입력하세요 : "))
factorial(n)