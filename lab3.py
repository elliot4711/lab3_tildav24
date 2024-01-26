from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()             # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

engelska = Bintree()
with open("engelska.txt", "r", encoding="utf-8") as engelskfil:
    for rad in engelskfil:
        ordlista = rad.split()
        for ordet in ordlista:
            ordet = ordet.replace('!', '')
            ordet = ordet.replace('"', '')
            ordet = ordet.replace(',', '')
            ordet = ordet.replace('.', '')
            ordet = ordet.replace("'", '')
            if ordet in engelska:
                pass
            else:
                engelska.put(ordet)
                if ordet in svenska:
                    print(ordet, end = " ") 
                else:
                    pass