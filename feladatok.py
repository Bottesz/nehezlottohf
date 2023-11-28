import main

#########
# Kérj be a felhasználótól 5 számot, és döntsd el, hogy van-e találata?
#########
def talalat_ellenorzes(szamok):
    keresett_szamok = [3, 7, 12, 15, 20]  

    talalat = any(szam in keresett_szamok for szam in szamok)

    if talalat:
        print("Gratulálok! Van találat a keresett számok között.")
    else:
        print("Sajnos nincs találat a keresett számok között.")



bekert_szamok = []
for i in range(5):
    szam = int(input(f"Kérlek adj meg egy számot ({i+1}. szám): "))
    bekert_szamok.append(szam)


talalat_ellenorzes(bekert_szamok)



##############
# Kérj be a felhasználótól 5 számot, és a program mondja meg, hány találata van az illetőnek? 
#############

def talalatok_szama(bekert_szamok, keresett_szamok):
    talalatok = sum(szam in keresett_szamok for szam in bekert_szamok)
    return talalatok

bekert_szamok = []
for i in range(5):
    szam = int(input(f"Kérlek adj meg egy számot ({i+1}. szám): "))
    bekert_szamok.append(szam)


keresett_szamok = [3, 7, 12, 15, 20]


talalatok = talalatok_szama(bekert_szamok, keresett_szamok)
print(f"Az illetőnek {talalatok} találata van a keresett számok között.")


############
# A húzott véletlen számok ne lehessenek azonosak!
############
import random

def talalatok_szama2(bekert_szamok, keresett_szamok):
    talalatok = sum(szam in keresett_szamok for szam in bekert_szamok)
    return talalatok


bekert_szamok = []
keresett_szamok = []

while len(bekert_szamok) < 5:
    szam = int(input(f"Kérlek adj meg egy számot ({len(bekert_szamok) + 1}. szám): "))
    if szam not in keresett_szamok:
        bekert_szamok.append(szam)
        keresett_szamok.append(szam)
    else:
        print("Ez a szám már korábban meg lett adva. Kérlek adj meg egy másik számot.")


talalatok = talalatok_szama(bekert_szamok, keresett_szamok)
print(f"Az illetőnek {talalatok} találata van a keresett számok között.")



##############
# A felhasználótól addig kérd be a számokat, amíg 5 különbözőt ad meg!
##############
def bekerni_ot_szamot():
    bekert_szamok = set()
    
    while len(bekert_szamok) < 5:
        szam = int(input("Kérlek adj meg egy számot: "))
        
        if szam in bekert_szamok:
            print("Ezt a számot már megadtad korábban. Adj meg egy másik számot.")
        elif szam not in range(1, 101):
            print("A számnak 1 és 100 között kell lennie. Adj meg egy másik számot.")
        else:
            bekert_szamok.add(szam)
    
    return bekert_szamok

bekert_szamok = bekerni_ot_szamot()
print("Az általad megadott különböző számok:", bekert_szamok)
