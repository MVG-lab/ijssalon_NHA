def decoreer(tekst = ""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    try:
        berdrag_pp = bedrag/personen
    except:
        berdrag_pp = "??"
    return f"Het bedrag per persoon is {berdrag_pp} euro"