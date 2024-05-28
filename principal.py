print ("CLASSIFICADOR DE HERÓI")

nome = input("insira o nome do herói:")
xp=0
Rank=""


while True:
    op= int(input())
    if(op==1):
        print("Ranking: ", xp, Rank)
    if(op==2):
        print("ganhou 500xp")
        xp+=500
    
    if (xp<=1000):
        Rank="Ferro"
    elif(xp>=1001 and xp<=2000):
        Rank="Bronze"
    elif(xp>=2001 and xp<= 5000):
        Rank="Prata"
    elif(xp>=5001 and xp<=7000):
        Rank="Ouro"
    elif(xp>=7001 and xp<=8000):
        Rank="Platina"
    elif(xp>=8001 and xp<=9000):
        Rank="Ascendente"
    elif(xp>=9001 and xp<=10000):
        Rank="Imortal"
    elif(xp>10001):
        Rank="Radiante"