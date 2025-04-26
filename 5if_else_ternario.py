nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# IF e ELSE de forma ternaria
maioridade = "MAIOR" if idade >= 18 else "MENOR"
print(f"Olá {nome}, você é {maioridade} de idade.")

'''
é uma forma mais curta e concisa de escrever um if e else simples em uma única linha. Chamamos isso de operador ternário (porque envolve três partes).
A linha com o operador ternário verifica se a idade é maior ou igual a 18.
maioridade = "MAIOR" if idade >= 18 else "MENOR"

'''