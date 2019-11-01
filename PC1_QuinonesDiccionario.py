op = 0
diccionario = dict(
    {1:0,2:0,3:0}
)
#creacion de la matriz de 7x6
matriz = []
for i in range(7):
    matriz.append([])
    for j in range(6):
        matriz[i].append("X")


while op != 4:
    print("MENU DE VOTACIONES")
    print("+**********************+")
    print("+      VOTACION        +")
    print("+**********************+")
    print("+ 1. Ver Candidados    +")
    print("+ 2. Registrar Voto    +")
    print("+ 3. Flash Informativo +")
    print("+ 4. Salir             +")
    print("+**********************+")

    op = int(input("Ingrese Opion: "))

    if(op==1):
        print("+***********************+")
        print("+      CANDIDATOS       +")
        print("+***********************+")
        print("+#\t\tCandidato\t\t+")
        print("+1.\tLuis Esperanza\t\t"+"+")
        print("+2.\tJose Barata\t\t\t"+"+")
        print("+3.\tMarco Ocras\t\t\t"+"+")
        print("+**********************+")
    elif(op==2):
        voto=0
        print("+1.\tLuis Esperanza\t+")
        print("+2.\tJose Barata\t+")
        print("+3.\tMarco Ocras\t+")
        while voto < 1 or voto > 3:
            voto=int(input("Eliga candidato: "))
            total = diccionario.get(voto)
            total = total + 1
            diccionario[voto] = total
            if (voto < 1 or voto > 3):
                print("Error, Candidato No Existe")

    elif(op==3):
        if(diccionario.get(1)>0 or diccionario.get(2)>0 or diccionario.get(3)>0):
            print("+***********************+")
            print("+  FLASH INFORMATIVO    +")
            print("+***********************+")
            print("+#\tCandidato\tVotos\t+")
            print("+1.\tLuis Esperanza\t"+str(diccionario.get(1))+"\t+")
            print("+2.\tJose Barata\t\t"+str(diccionario.get(2))+"\t+")
            print("+3.\tMarco Ocras\t\t"+str(diccionario.get(3))+"\t+")
            print("+***********************+")
            print("+\tTOTAL VOTOS\t\t"+str(diccionario.get(1)+diccionario.get(2)+diccionario.get(3))+"\t+")
            print("+***********************+")
        else:
            print("No Hay Votos Emitidos")

    elif(op==4):
        total = []
        total.append(diccionario.get(1))
        total.append(diccionario.get(2))
        total.append(diccionario.get(3))

        if(diccionario.get(1)>0 or diccionario.get(2)>0 or diccionario.get(3)>0):
            print("+***********************+")
            print("+       GANADOR         +")
            print("+***********************+")
            if(max(total)==total[0]):
                for i in range(7):
                    for j in range(6):
                        if(i==2):
                            print("+\t"+matriz[i][j])

                        if(i>=2 and j==5):
                            print("\t"+matriz[i][j],end=" ")
                print("\n+***********************+")
                print("+\nLuis Esperanza: "+ str(max(total)) + " Votos" )
                print("+***********************+")
            elif(max(total)==total[1]):
                for i in range(7):
                    for j in range(6):
                        if(i>1 and i<5 and j==0):
                            print("\t"+matriz[i][j],end=" ")
                print("")
                for i in range(7):
                    for j in range(6):
                        if(i==3 and j<=3):
                            print("\t\t"+matriz[i][j])

                for i in range(7):
                    for j in range(6):
                        if(i>=2 and i<=3 and j==3):
                            print("\t"+matriz[i][j],end=" ")
                print("")
                for i in range(7):
                    for j in range(6):
                        if(i>=2 and i<=3 and j==5):
                            print("\t"+matriz[i][j],end=" ")





                print("\n+***********************+")
                print("+\n\tJose Barata: "+ str(max(total)) + " Votos" )
                print("+***********************+")
            elif(max(total)==total[2]):
                for i in range(7):
                    for j in range(6):
                        if(i==2 and j==0):
                            print("\t"+matriz[i][j],end="\t  ")
                        if(i==4  and j==0):
                            print("\t"+matriz[i][j],end="\t  ")
                print("")
                for i in range(7):
                    for j in range(6):
                        if(i==3 and j==0):
                            print("\t\t"+matriz[i][j],end="\t  ")

                print("")
                for i in range(7):
                    for j in range(6):
                        if(i==2 and j==0):
                            print("\t"+matriz[i][j],end="\t  ")
                        if(i==4  and j==0):
                            print("\t"+matriz[i][j],end="\t  ")


                print("")
                for i in range(7):
                    for j in range(6):
                        if(i==2 and j==0):
                            print("\t"+matriz[i][j],end="\t  ")
                        if(i==4  and j==0):
                            print("\t"+matriz[i][j],end="\t  ")
                print("")
                for i in range(7):
                    for j in range(6):
                        if(i==2 and j==0):
                            print("\t"+matriz[i][j],end="\t  ")
                        if(i==4  and j==0):
                            print("\t"+matriz[i][j],end="\t  ")



                print("\n+***********************+")
                print("+\n\tMarco Ocram: "+ str(max(total)) + " Votos" )
                print("+***********************+")













