# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


letra = str(input("Digite uma letra: ")).lower()
if len(letra)== 1:
     
  if letra in "aeiou":
    print("Vogal")
  elif letra in "bcdfgjklmnpqrstvwxz":
     print("Consoante")
  else:
     print("Meu fi so uma LETRA")
