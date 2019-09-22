import random
def Zcasino(maxAmount):
    continued=True
    while continued:
        print("\n your initial amaount",maxAmount," \n =======================")
        i=0
        #boucle pour choisir la somme à miser
        while i==0:
            amaount=input("enter the amount to be bet :") #saisi du nombre
            nbBet=input("enter the number you want to bet on :") #somme miser
            try: #essayer de le convertir en valeur entière
                amaount=int(amaount)
                nbBet=int(nbBet)
                i+=1
            except: #si la convertion marche pas alors resaiisir de nouveau
                print("**** you have entered a non-integer value ****")
                i=0
                continue
            if amaount > maxAmount:#condition pour ne pas miser plus que la somme dont on dispose
                print("**** you have little money to bet this amount ****")
                i=0
                continue
            if nbBet < 0 or nbBet > 49 :
                print("**** Please Enter the number you want bet on between 0 and 49 ****")
                i=0

        print("You Bet:",amaount,"on the number",nbBet)
        nbDraw=random.randrange(50)
        print("\nafter rolling, the third number is :",nbDraw,"\n")
        modDraw=nbDraw%2
        modBet=nbBet%2
        maxAmount -= amaount

        if nbBet==nbDraw:
            maxAmount+= amaount*3
            print("=======you win the triple bet ",amaount*3," =======")
        elif modDraw==modBet:#le nombre de mise et le nombre tiré par
                             #sont de la même couleur
                             #c-à-d sont tous les eux impairs ou pairs
            maxAmount+=amaount/2
            print("=======you lose  ",amaount/2," =======")
        else:
            print("=======You lose=======")

        if maxAmount<=0:#si plus d'argent fin de jeu
            continued=False
        print("\n===================================================")