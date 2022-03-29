#5번
temp = float(input("Enter a temperature : "))
con = input("Convert to (F)ahrenheit or (C)elsius? : ")

if con.lower() == 'f':
    t = (9/5)*temp+32
    print("{} C = {} F".format(temp,t))
elif con.lower() == 'c':
    t = (5/9)*(temp-32)
    print("{} F = {} C".format(temp,t))