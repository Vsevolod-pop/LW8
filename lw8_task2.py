H = input('Введите число H - ')
while True:
    try:
        if int(H) > 0 and int(H) == float(H) and ('0' != H[0]):
            H = int(H)
        else:
            raise Exception
    except Exception:
        H = input('Введенное значение не корректно. Введите число H - ')
    else:
        break
M = input('Введите число M - ')
while True:
    try:
        if int(M) > 0 and int(M) == float(M) and ('0' != M[0]):
            M = int(M)
        else:
            raise Exception
    except Exception:
        M = input('Введенное значение не корректно. Введите число M - ')
    else:
        break
S = input('Введите число S - ')
while True:
    try:
        if int(S) > 0 and int(S) == float(S) and ('0' != S[0]):
            S = int(S)
        else:
            raise Exception
    except Exception:
        S = input('Введенное значение не корректно. Введите число S - ')
    else:
        break
T = input('Введите число T - ')
while True:
    try:
        if int(T) > 0 and int(T) == float(T) and ('0' != T[0]):
            T = int(T)
        else:
            raise Exception
    except Exception:
        T = input('Введенное значение не корректно. Введите число T - ')
    else:
        break
def IncTime(H,M,S,T):
    H = H*3600
    M = M*60
    time = H+M+S+T
    H = time//3600
    M = (time-(H*3600))//60
    S = time-(H*3600)-(M*60)
    return H,M,S
H,M,S = IncTime(H,M,S,T)
print('Число H = ', H, 'ч', sep='')
print('Число M = ', M, 'м', sep='')
print('Число S = ', S, 'с', sep='')