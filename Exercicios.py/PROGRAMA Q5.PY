# Faça um programa para a leitura de duas notas parciais de um aluno. O
# programa deve calcular a média alcançada por aluno e apresentar:
# ○ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# ○ A mensagem "Reprovado", se a média for menor do que sete;
# # ○ A mensagem "Aprovado com Distinção", se a média for igual a dez.:


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

match nota1 , nota2 :

case ((nota1 + nota2 ) / 2) >= 7:
    print("Aprovado")
case ((nota1 + nota2 ) / 2) < 7:
    print("Reprovado")
case ((nota1 + nota2 ) / 2) == 10:
    print("Aprovado com Distinção")

