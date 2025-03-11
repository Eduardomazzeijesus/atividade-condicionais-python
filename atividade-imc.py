import os 

os.system("cls")

print('''
██╗███╗░░░███╗░█████╗░
██║████╗░████║██╔══██╗
██║██╔████╔██║██║░░╚═╝
██║██║╚██╔╝██║██║░░██╗
██║██║░╚═╝░██║╚█████╔╝
╚═╝╚═╝░░░░░╚═╝░╚════╝░''')

peso = float(input("digite o seu peso:"))

altura = float(input("digite a sua altura:"))

multi = peso / (altura * altura) 
print("imc é: " , round(multi,2) )

if(multi <= 16.9):
    print("voce esta muito abaixo do peso")

elif(multi >= 17 and multi <= 18.4):
    print("voce esta abaixo do peso")

elif(multi >= 18.5 and multi <= 24.9):
    print("voce esta no peso ideal")

elif(multi >= 25 and multi <= 29.9):
    print("voce esta acima do peso ")

elif(multi >= 30 and multi <= 34.9):
    print("voce esta com obesidade 1")

elif(multi >= 35 and multi <= 40):
    print("voce esta com obesidade 2")

else:
    print("voce esta com obesidade grau3")
