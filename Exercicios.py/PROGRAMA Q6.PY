# Faça um Programa que leia três números e mostre o maior deles.

nu1 = float(input("Digite um numero: "))
nu2 = float(input("Digite um numero: "))
nu3 = float(input("Digite um numero: "))

if nu1 < nu2 and nu2 < nu3 :
    print(f"{nu3} É o maior numero")
elif nu3 < nu2 and nu2 < nu1 :
    print(f"{nu1} É o maior numero")
elif nu2 > nu3 and nu2 > nu1:
    print(f"{nu2} É o maior numero")
elif nu1 == nu2 == nu3 :
    print("Todos são iguais")