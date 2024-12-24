N = input('Введите натуральное число N - ')
while True:
    try:
        if N.isdigit() == True and N[0]!='0':
            N = N
        else:
            raise Exception
    except Exception:
        N = input('Введенное значение не корректно. Введите число N - ')
    else:
        break
def Recursion(N):
    if len(N) == 1:
        print(N)
    else:
        print(N[-1],end = ' ')
        return Recursion(N[:-1])
Recursion(N)