# função para calcular fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# função para ordenar lista
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# função para calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# jogo de adivinhação de números
import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Adivinhe o número entre 1 e 100!")
    
    while True:
        tentativa = int(input("Sua tentativa: "))
        tentativas += 1
        
        if tentativa < numero_secreto:
            print("Mais alto!")
        elif tentativa > numero_secreto:
            print("Mais baixo!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            break

# Teste as funções
if __name__ == "__main__":
    print("Fibonacci de 10:", fibonacci(10))
    print("Lista ordenada:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print("IMC:", calcular_imc(70, 1.75))
    jogo_adivinhacao()