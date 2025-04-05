for n in range(3, 1000):
    stroka = '1' + n * '6'
    while '111' in stroka or '66' in stroka:
        if '6666' in stroka:
            stroka = stroka.replace('6666', '1', 1)
        else:
            stroka = stroka.replace('111', '3', 1)
        if '66' in stroka:
            stroka = stroka.replace('66', '6', 1)

    schet = stroka.count('3')
    if schet >= 5:
        print(n)
        break