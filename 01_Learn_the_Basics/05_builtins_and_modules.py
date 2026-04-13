# ==========================================
# EXERCÍCIO 05: Built-in Functions e Módulos
# ==========================================

# MISSÃO:
# Vamos usar as "Baterias Inclusas" do Python.
#
# 1. IMPORTAÇÃO:
#    Importe o módulo `math` e o módulo `datetime`.
#
# 2. BUILT-IN FUNCTIONS:
#    Crie uma lista de números: `notas = [8.5, 7.0, 9.0, 6.5, 10.0]`.
#    Use as funções nativas `sum()` e `len()` para calcular a MÉDIA dessas notas.
#    Imprima a média.
#
# 3. MÓDULO MATH:
#    Use `math.ceil()` para arredondar a média para cima.
#    Use `math.floor()` para arredondar a média para baixo.
#
# 4. MÓDULO DATETIME:
#    Imprima o dia e a hora atual usando `datetime.datetime.now()`.
#
# EXTRA:
# Use a built-in function `help(math)` (ou `dir(math)`) no terminal para 
# ver quantas outras coisas legais existem dentro do módulo math!

# ==========================================
# ESCREVA SEU CÓDIGO ABAIXO DESTA LINHA:
# ==========================================

import math 
import datetime

notas = [8.5, 7.0, 9.0, 6.5, 10.0]

media = sum(notas) / len(notas)

print(media)

media_arredondada_cima = math.ceil(media)
media_arredondada_baixo = math.floor(media)

print(media_arredondada_cima)
print(media_arredondada_baixo)

print(datetime.datetime.now())

