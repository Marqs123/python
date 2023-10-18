# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

nu1 = float(input("Digite um numero: "))
nu2 = float(input("Digite um numero: "))
nu3 = float(input("Digite um numero: "))


if nu1 < nu2 and nu2 < nu3 : # nu1 menor é nu3 maior
    print(f"{nu3} É o maior numero")
    print(f"{nu1} É o menor numero")
elif nu3 < nu2 and nu2 < nu1 : # nu3 menor é nu1 maior 
    print(f"{nu1} É o maior numero")
    print(f"{nu3} É o menor numero")
elif nu2 < nu3 and nu3 < nu1 : # nu2 menor é nu1 maior 
    print(f"{nu1} É o maior numero")
    print(f"{nu2} É o menor numero")
elif nu3 < nu1 and nu1 < nu2: # nu3 menor é nu2 maior 
    print(f"{nu2} É o maior numero")
    print(f"{nu3} É o menor numero")
elif nu1 < nu3 and nu3 < nu2 : # nu1 menor é nu2 maior 
    print(f"{nu2} É o maior numero")
    print(f"{nu1} É o menor numero")
elif nu2 < nu1 and nu1 < nu3 : # nu2 menor é nu3 maior
    print(f"{nu3} É o maior numero")
    print(f"{nu2} É o menor numero")
    
elif nu1 and nu2 > nu3 :
    print(f"{nu1} e {nu2} são o maior que {nu3}")

elif nu3 and nu2 > nu1 :
    print(f"{nu3} e {nu2} são o maior que {nu1}")

elif nu3 and nu1 > nu2 :
    print(f"{nu3} e {nu1} são o maior que {nu2}")

elif nu1 and nu2 < nu3 :
    print(f"{nu1} e {nu2} são o menor que {nu3}")

elif nu3 and nu2 < nu1 :
    print(f"{nu3} e {nu2} são o menor que {nu1}")

elif nu3 and nu1 < nu2 :
    print(f"{nu3} e {nu1} são o menor que {nu2}")

else:
    print("Numeros iguais")