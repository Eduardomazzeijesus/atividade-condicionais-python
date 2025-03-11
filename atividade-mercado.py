import os 

os.system("cls")

print('''
███╗░░░███╗███████╗██████╗░░█████╗░░█████╗░██████╗░░█████╗░
████╗░████║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║█████╗░░██████╔╝██║░░╚═╝███████║██║░░██║██║░░██║
██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██╗██╔══██║██║░░██║██║░░██║
██║░╚═╝░██║███████╗██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░ ''')

n1 = input("digite o nome do produto:")

n2 = int(input("digite a quantidade:"))

valor = float(input("digite o valor:"))

os.system("cls")

print("nota fiscal")
print("============================================")

soma = n2 * valor 
print("valor da compra sem o desconto!", + soma)


if(n2 <= 5):
    desconto1 = soma - (0.02 * soma)
    print("valor final com 2 % de desconto " , + desconto1)

elif(n2 > 5 and n2 <= 10):
    desconto2 = soma - (0.03 * soma)
    print("valor final com 3% de desconto" , + desconto2)

else:
    desconto3 = soma - (0.05 * soma)
    print("valor final com 5% de desconto" , + desconto3)

print("obrigado por visitar o nosso mercado")
print("volte sempre!:)")




