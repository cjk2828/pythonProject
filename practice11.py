#11번
import sys

filename = input("파일 이름을 입력하세요")
accessMode = "r"
try:
    myfile = open(filename,accessMode)
    dat = myfile.readline()
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
    sys.exit()
count = 1
while dat != "":
    print("{}: {}".format(count,dat), end="")
    count = count+1
    dat = myfile.readline()

myfile.close()