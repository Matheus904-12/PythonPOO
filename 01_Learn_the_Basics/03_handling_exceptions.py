# ==========================================
# EXERCÍCIO 03: Tratamento de Erros (try / except)
# ==========================================

# MISSÃO:
# Vamos criar um "Calculador de Divisão" à prova de erros.
#
# 1. Peça ao usuário um "Número A" e um "Número B".
#
# 2. Tente dividir A por B e mostrar o resultado.
#
# 3. O SEU TRABALHO:
#    Use o bloco `try:` e `except:` para capturar dois erros comuns:
#
#    A) Se o usuário digitar um texto em vez de número (ex: "abc"):
#       O Python gera um `ValueError`. Capture-o e diga: "Erro: Digite apenas números!"
#
#    B) Se o usuário tentar dividir por zero (B = 0):
#       O Python gera um `ZeroDivisionError`. Capture-o e diga: "Erro: Não é possível dividir por zero!"
#
# 4. PLUS (Desafio do Tech Lead):
#    Use um loop `while True:` para que o programa continue pedindo os números
#    até que o usuário digite valores válidos e a conta seja feita com sucesso.
#    DICA: Use o comando `break` quando a conta der certo para sair do loop.

# ==========================================
# ESCREVA SEU CÓDIGO ABAIXO DESTA LINHA:
# ==========================================

# try:
#     numA = int(input("Digite o primeiro número: "))
#     numB = int(input("Digite o segundo número: "))

#     resultado = numA / numB

#     print(f"Resultado: {resultado}")

# except ValueError:
#     print("Erro digite apenas números")

# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero!")

while True:
    try: 
        numA = int(input("Digite o primeiro número: "))
        numB = int(input("Digite o segundo número: "))

        resultado = numA / numB
        print(f"Resultado: {resultado}")
        break
    except ValueError:
        print("Erro digite apenas números")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
