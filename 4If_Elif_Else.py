nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

if nota >= 0 and nota <= 10: #definine o parametro a ser seguido , desse ponto a esse ponto e pronto, caso ao contrario ela da como invalido.
    if nota >= 7:
        print(f"Olá {nome}, você foi APROVADO com a nota {nota}.")
    elif nota >= 5:
        print(f"Olá {nome}, você está em RECUPERAÇÃO com a nota {nota}.")
    else:
        print(f"Olá {nome}, você foi REPROVADO com a nota {nota}.")
else:
    print(f"Olá {nome}, a nota {nota} é inválida. A nota deve ser entre 0 e 10.")


    '''
    O primeiro if checa se a nota é válida.
O segundo if (e as outras condições dentro dele) checam o seu resultado final, mas só se a nota for válida. É uma verificação dentro de outra.
observe os sinais de maior > ,e menor < ,na hora de definir o resultado de cada nota.

    
    '''