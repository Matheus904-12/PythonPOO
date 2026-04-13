# ==========================================
# EXERCÍCIO 02: Condicionais (if, elif, else) e Lógica
# ==========================================

# MISSÃO:
# Vamos criar um "Classificador de Descontos" para um cinema.
#
# 1. Solicite a IDADE do usuário.
#
# 2. Use a estrutura if/elif/else para classificar o preço do ingresso:
#    - Se a idade for MENOR que 12 anos: Imprima "Ingresso Infantil: R$ 15,00"
#    - Se a idade for entre 12 e 17 anos: Imprima "Ingresso Adolescente: R$ 20,00"
#    - Se a idade for entre 18 e 59 anos: Imprima "Ingresso Inteira: R$ 35,00"
#    - Se a idade for 60 anos ou mais: Imprima "Ingresso Idoso (60% de desconto): R$ 14,00"
#
# 3. EXTRA (Desafio):
#    Pergunte se o usuário tem "carteirinha de estudante" (sim/nao).
#    Se ele for "Inteira" mas tiver carteirinha, ele deve pagar "Meia Entrada: R$ 17,50".
#    DICA: Use operadores lógicos como `and` ou `or`, ou aninhamento de `if`.

# ==========================================
# ESCREVA SEU CÓDIGO ABAIXO DESTA LINHA:
# ==========================================

idade = int(input("Digite aqui sua idade: "))

if idade < 12:
    print("Ingresso Infantil: R$ 15,00")
elif 12 <= idade <= 17:
    print("Ingresso Adolescente: R$ 20,00")
elif 18 <= idade <= 59:
    print("Ingresso Inteira: R$ 35,00")
else:
    print("Ingresso Idoso (60% de desconto): R$ 14,00")

carteirinha = bool(input("Você tem carteirinha de estudante? (sim/não): "))

if 18 <= idade <= 59:
    if carteirinha:
        print("Meia Entrada: R$ 17,50")
    else:
        print("Inteira R$ 35,00")