'''
print("inserisci voti del candidato a")
print("inserisci voti del candidato b")

a=int(input("voti del primo candidato"))
b=int(input("voti del secondo candidato"))
totale= a+b
percentualea = (a*100)/totale
percentualeb = (b*100)/totale

print(percentualea)
print(percentualeb)

if percentualea > percentualeb:
    print("ha vinto il candidato a")

elif percentualea == percentualeb:
    print("è un pareggio!!")

else:
    print("ha vinto candidato b")
'''
'''
print("armando e benedetta sono i 2 candidati")
armando= input ("quanti voti ha ottenuto armando?")
benedetta= input("quanti voti ha ottenuto benedetta?")
voti=[]
voti.append(armando)
voti.append(benedetta)
voti.sort()
print(voti)

if armando < benedetta:
    voti.reverse
    print(voti)
'''

sommatoria= 0
numerosoldi= 0

while True:
    stipCorrente= float(input("inserisci lo stipendio (scrivi -1 quando gli stipendi sono terminati):"))
    if stipCorrente < 1000000000000
    or stipCorrente > -1:
        print("hai inserito", stipCorrente, "non è un valore accettabile")
    elif stipCorrente == -1:
        break
    else:
        numerosoldi += 1
        sommatoria += stipCorrente

media = sommatoria/ numerosoldi
print("la media è", media)
