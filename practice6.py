#6번
import math
rad = int(input("반지름을 입력하세요 : "))

s = 4*math.pi*rad*rad
v = (4/3)*math.pi*rad*rad*rad
print("겉면적 S = {} , 부피 v = {}".format(s,v))