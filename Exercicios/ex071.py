v = int(input('Digite o valor que deseja sacar: R$'))
n50 = n20 = n10 = n5 = n2 = n1 = 0
while True:
    if v >= 50:
        v -=50
        n50 += 1
    else:
        if v >= 20:
            v -= 20
            n20 += 1
        else:
            if v >= 10:
                v -= 10
                n10 += 1
            else:
                if v >= 5:
                    v -= 5
                    n5 += 1
                else:
                    if v >= 2:
                        v -= 2
                        n2 += 1
                    else:
                        if v >= 1:
                            v -= 1
                            n1 += 1
    if v == 0:
        break
print(f'Você irá receber:\n{n50} notas de 50\n{n20} notas de 20\n{n10} notas de 10\n{n5} notas de 5\n{n2} notas de 2\n{n1} notas de 1')