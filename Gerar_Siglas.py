import random

frase = input("Digite uma frase:")
simbolos = "@#$%&!"
palavras = frase.split()
senha = ""

senha += str(random.randint(10, 99))
senha += random.choice(simbolos)

for palavra in palavras:
    senha += palavra[0].upper()
    senha += palavra[-1].upper()

senha += random.choice(simbolos)
senha += str(random.randint(10, 99))

print("Senha gerada:", senha)