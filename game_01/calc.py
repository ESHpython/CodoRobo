def calc(a,b,c,qi):
    if b == "+":
        qi = a + c    
    elif b == "-":
        qi = a - c
    elif b == "/":
        qi = a / c
    else:
        qi = a * c

    print("Результатом выражения стало " + str(qi))


variable = input("Введите выраженние ")
qi = 0
a = int(variable[0])
b = variable[1]
c = int(variable[2])


calc(a,b,c,qi)