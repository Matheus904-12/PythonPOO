# ==========================================
# EXERCÍCIO 01: Variáveis, Tipos e Type Casting
# ==========================================

# MISSÃO:
# 1. Solicite ao usuário (usando a função built-in `input()`) que digite o seu NOME.
#    Armazene isso em uma variável chamada `nome`.
#
# 2. Solicite ao usuário que digite a sua IDADE.
#    Armazene em uma variável chamada `idade`. ATENÇÃO: a função input() sempre
#    retorna uma string (str). Você precisa converter (Type Casting) esse
#    valor para um número inteiro (int).
#
# 3. Solicite ao usuário que digite a sua ALTURA (ex: 1.75).
#    Armazene em uma variável `altura` e faça o cast para float (decimal).
#
# 4. Imprima no terminal uma frase formatada (f-string) usando as 3 variáveis.
#    Exemplo esperado: "Olá, João! Você tem 25 anos e mede 1.75m de altura."
#
# 5. Por fim, use a função built-in `type()` para imprimir o tipo de cada
#    uma das 3 variáveis na tela, provando que `idade` virou int e `altura` float.

# ==========================================
# ESCREVA SEU CÓDIGO ABAIXO DESTA LINHA:
# ==========================================

nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m de altura.")

print(type(nome))
print(type(idade))
print(type(altura))