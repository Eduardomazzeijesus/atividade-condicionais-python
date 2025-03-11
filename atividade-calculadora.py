import os 

os.system("cls")

print('''

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝ ''')

print("1 conta de soma")
print("2 conta de subtraçao")
print("3 conta de divisao")
print("4 conta de multiplicaçao")

n1 = int(input("digita o primeiro numero:"))

n2 = int(input("digite o segundo numero:"))

conta = int(input("digite a conta que voce quer:"))

os.system("cls")

print("resultado final")
print("=====================================")


if(conta == 1):
    print("a sua conta é de soma")
    conta1 = n1 + n2
    print("seu resultado é" , + conta1)

elif(conta == 2):
    print("a sua conta é de subtraçao")
    conta2 = n1 - n2 
    print("seu resultado é" , + conta2)

elif(conta == 3):
    print("a sua conta é de divisao")
    conta3 = n1 / n2
    print("seu resultado é" , + conta3)

else:
    print("sua conta é de multiplicaçao")
    conta4 = n1 * n2 
    print("seu resultado é " , + conta4)

print("obrigado por confiar em nosso trabalho")
print("volte sempre :)")




