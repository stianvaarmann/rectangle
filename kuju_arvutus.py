# ristküliku arvutus

a = float(input('Sisesta esimene külg (1-100): '))
if a > 100 or a < 1:
    print('Mõõt vales vahemikus.')
else:
    b = float(input('Sisesta teine külg (1-100): '))
    if b > 100 or b < 1:
        print('Mõõt vales vahemikus.')
    else: 
        if a == b:
            print('Kujund pole ristkülik.')
        else:
            P = 2 * (a + b)
            S = a * b
            print(f'Ümbermõõt: {P}', (f'Pindala: {S}'))