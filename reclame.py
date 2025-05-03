from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    totaal_na_korting = (1-korting)*prijs
    return f"Vandaag in de aanbieding: emmer ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {totaal_na_korting} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    totaal_btw = 0
    totaal = sum(inkomsten)
    totaal_btw = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waaover {totaal_btw} euro btw dient te worden betaald"

def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]

def gemiddelde(mijn_lijst):
    week_gemiddelde = sum(mijn_lijst) / 7
    return f"De gemiddelde inkomsten van deze week zijn {week_gemiddelde} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie([220,430,125,160,205,90,345]))