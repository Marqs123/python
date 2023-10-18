# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

produto1 = float(input("Digite o primeiro valor: "))
produto2 = float(input("Digite o segundo valor: "))
produto3 = float(input("Digite o terceiro valor: "))


if produto1 < produto2 and produto2 < produto3 :
    print(f"o produto de  {produto1} reais e o mais em conta ")
   
elif produto2 < produto1 and produto1 < produto3:
    print(f"o produto de {produto2} reais e o mais em conta ")

elif produto3 < produto2 and produto2 < produto1:
    print(f"o produto de {produto3} reais e o mais em conta ")

else :
    print("Todos são o mesmo valor ")
   
   

