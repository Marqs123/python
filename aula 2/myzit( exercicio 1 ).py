numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"{numero1} é maior que o {numero2}")
elif numero2 > numero1:
    print(f"{numero2} é maior que o {numero1}") 
else:
    print("Os dois numeros são iguais")
