import random

print("--Gerador de Siglas--")
frase = input("Digite uma frase:")
simbolos = "@#-_!"
palavras = frase.split()
senha = ""

senha += str(random.randint(10, 99))
senha += random.choice(simbolos)

for palavra in palavras:
    senha += palavra[0].upper()
    senha += palavra[-1].lower()

senha += random.choice(simbolos)
senha += str(random.randint(1000, 9999))

print("Senha gerada:", senha)
print("Obrigado por usar o gerador de siglas!")
