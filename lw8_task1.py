spisok = []
for i in range(10):
    K = input('Введите число - ')
    while True:
        try:
            if int(K) > 0 and int(K) == float(K) and ('0' != K[0]):
                spisok.append(int(K))
            else:
                raise Exception
        except Exception:
            K = input('Введенное значение не корректно. Введите число - ')
        else:
            break
def IsSquare(i):
    if i**(1/2) == int(i**(1/2)):
        return True
    else:
        return False
count = 0
for i in spisok:
    if IsSquare(i) == True:
        count += 1
print('Количество квадратов в данном списке чисел равно = ', count)