nome = input("Digite seu nome:")   # solicita ao usuário que digite seu nome e armazena na variável nome

print(f"Ola, meu nome é {nome}!")  # solicita ao usuário que digite seu nome e armazena na variável nome

'''
"Lembre-se de que dentro das chaves `{}` em um `f-string`, os espaços ao redor das variáveis ou expressões são geralmente ignorados na saída final. O objetivo principal desses espaços é melhorar a legibilidade do seu código dentro do `f-string`, não para adicionar espaços extras na string resultante.

Para garantir que as palavras no seu `print` não saiam grudadas, adicione espaços explicitamente dentro das aspas da string do `f-string`, onde você deseja que esses espaços apareçam.

Exemplo:

Em vez de:
print(f"Olá{nome}!Você tem{idade}anos.")

Use:
print(f"Olá {nome}! Você tem {idade} anos.")

Observe os espaços adicionados antes e depois das chaves."
Correção da observação sobre a execução no terminal:

"E mais uma vez, lembrando da forma de execução de um script Python utilizando o terminal: o comando básico é python seguido do nome do arquivo Python que você deseja executar(que deve ter a extensão.py).

Exemplo:

Se o seu arquivo se chama meu_script.py, o comando correto para executá-lo no terminal será:

bash
python meu_script.py
É importante garantir que você esteja no diretório correto no terminal onde o arquivo meu_script.py está salvo." == python nome.py 
''' 