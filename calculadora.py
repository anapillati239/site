def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# Teste das funções
if _name_ == "_main_":
    print(f"Soma: {soma(5, 3)}")
    print(f"Subtração: {subtracao(5, 3)}")
    print(f"Multiplicação: {multiplicacao(5, 3)}")
    print(f"Divisão: {divisao(6, 3)}")
