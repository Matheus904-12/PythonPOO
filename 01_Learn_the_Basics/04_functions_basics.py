# ==========================================
# EXERCÍCIO 04: Funções (def) e Argumentos
# ==========================================

# MISSÃO:
# Vamos criar um "Processador de Mensagens" para um sistema de Login.
#
# 1. Defina uma função chamada `gerar_saudacao` que:
#    - Receba um parâmetro chamado `usuario`.
#    - Retorne (use `return`) a string: "Bem-vindo ao sistema, [usuario]!".
#
# 2. Defina uma função chamada `calcular_bonus` que:
#    - Receba um parâmetro chamado `salario`.
#    - Calcule um bônus de 10% em cima desse salário.
#    - Retorne o valor do bônus.
#
# 3. NO FINAL DO ARQUIVO:
#    - Chame a função `gerar_saudacao` passando o seu nome e dê um `print` no retorno.
#    - Peça um salário via `input()`, chame a função `calcular_bonus` e imprima:
#      "Seu bônus anual é de R$ [valor]".

# ==========================================
# ESCREVA SEU CÓDIGO ABAIXO DESTA LINHA:
# ==========================================

def gerar_saudacao(usuario):
    return(f"Bem-vindo ao sistema, {usuario}!")

def calcular_bonus(salario):
    return(f"Seu bônus anual é de R$ {salario * 0.10}")

saldo_usuario = float(input("Digite seu salário: "))
bonus = calcular_bonus(saldo_usuario)

print(bonus)
print(gerar_saudacao("Matheus"))