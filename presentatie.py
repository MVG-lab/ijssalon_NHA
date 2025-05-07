def presenteer(aankopen, totaal):
    print()
    for aankoop in aankopen:
        print(f"{aankoop} : {aankopen[aankoop]} euro")
    print("==========================")
    print(f"Totaal : {totaal} euro")