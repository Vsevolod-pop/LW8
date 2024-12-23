N = input('Введите натуральное число N - ')
while True:
    try:
        if int(N) >= 0 and int(N) == float(N) and ('00' != N[:2]):
            N = N
        else:
            raise Exception
    except Exception:
        N = input('Введенное значение не корректно. Введите число N - ')
    else:
        break
def Recursion(N):
    if len(N) == 1:
        return N
    else:
        return Recursion(N[1:])+N[:1]
print(list([Recursion(N).split('')]))
