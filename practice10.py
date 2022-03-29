#10번
import random
a = "true"
count = 0
correct = 0
while a == "true":
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    answer = int(input("{} * {} = :".format(n1,n2)))
    count = count+1
    if answer == n1*n2:
        correct = correct + 1
        print("맞았습니다")
    else:
        print("틀렸습니다")
    keep = input("계속 하시겠습니까? (y/n)")
    if keep.lower() == 'y' :
        continue
    elif keep.lower() == 'n':
        print("정답률은 {}% 입니다.".format(correct/count*100))
        break