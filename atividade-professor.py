import os 

os.system("cls")

print('''
███████╗░██████╗░█████╗░░█████╗░██╗░░░░░░█████╗░
██╔════╝██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗
█████╗░░╚█████╗░██║░░╚═╝██║░░██║██║░░░░░███████║
██╔══╝░░░╚═══██╗██║░░██╗██║░░██║██║░░░░░██╔══██║
███████╗██████╔╝╚█████╔╝╚█████╔╝███████╗██║░░██║
╚══════╝╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝ ''')

prof1 = input("digite o seu nome:")

niv = int(input("digite o seu nivel:"))

dia = int(input("digite quantas aulas por semana:"))

os.system("cls")

print("seu nome é:" , prof1)
print("seu nivel é:" , niv)
print("aulas semanais:" , dia)

if(niv == 1):
    niv1 =(dia * 12)
    print ("seu salario mensao" , + niv1)

elif(niv == 2):
    niv2 = (dia * 17)
    print("seu salario mensao" , + niv2)

else:
    niv3 = (dia * 25)
    print("seu salario mensao" , + niv3)