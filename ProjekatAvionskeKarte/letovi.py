from pregled import pregled_letova
import time

def kreiranje_letova(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,pr_korisnik):
    print("=" * 10, "KREIRANJE LETOVA", "=" * 10)
    file=open("avionski_letovi.txt","a+",encoding="utf8")
    broj_leta=""
    while True:
        broj_leta=input("Unesite broj leta:")
        if broj_leta in letovi:
            print("Greška takav broj već postoji!!")
        else:
            break
    polskr=""
    while True:
        polaziste=input("Unesite polaziste:")
        t=False

        for aerodrom in aerodromi.values():
            if polaziste in aerodrom["grad"]:
                polskr=aerodrom["skracenica"]
                t=True
        if t==False:
            print("Greska ne postoji takav grad!")
        else:
            break
    odrskr = ""
    while True:
        odrediste=input("Unesite odrediste:")
        t = False

        for aerodrom in aerodromi.values():
            if odrediste in aerodrom["grad"]:
                odrskr = aerodrom["skracenica"]
                t = True
        if t == False:
            print("Greska ne postoji takav grad!")
        else:
            break
    poletanje=""
    while True:
        poletanje=input("Unesite vreme poletanja (HH:MM):")
        t=True
        try:
            time.strptime(poletanje, '%H:%M')
            t=True
        except ValueError:
            print("Greška niste dobro uneli vreme!")
            t=False
        if t==True:
            break
    sletanje=""
    while True:
        sletanje=input("Unesite vreme sletanja (HH:MM):")
        t = True
        try:
            time.strptime(poletanje, '%H:%M')
            t = True
        except ValueError:
            print("Greška niste dobro uneli vreme!")
            t = False
        if t == True:
            break
    prevoznik=input("Unesite prevoznika:")
    dani=""
    while True:
        dani=input("Unesite dane letenja (npr. ponedeljak sreda...):")
        if "ponedeljak" not in dani and "utorak" not in dani and "sreda" not in dani and "četvrtak" not in dani and "petak" not in dani and "subota" not in dani and "nedelja" not in dani:
            print("Greška pogrešno ste upisali dane!!!")
        else:
            break
    model=""
    while True:
        model=input("Unesite model aviona:")
        if model not in modeli_aviona:
            print("Greška uneli ste pogrešan model aviona!!!")
        else:
            break
    cena=""
    while True:
        cena=input("Unesite cenu leta:")
        t=True
        try:
            c=int(cena)
            if c<=0:
                print("Greška cena ne može biti manja ili jednaka 0!!!")
                t=False
        except ValueError:
            print("Greška niste uneli broj!!!")
            t=False
        if t==True:
            break
    ssdana="ne"
    string=broj_leta+"|"+polskr+"|"+odrskr+"|"+poletanje+"|"+sletanje+"|"+ssdana+"|"+prevoznik+"|"+dani+"|"+model+"|"+cena+"\n"
    file.write(string)
    file.close()
def izmena_letova(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,pr_korisnik):
    print("=" * 10, "IZMENA LETOVA", "=" * 10)
    pregled_letova(korisnici, letovi, konkretni_letovi, modeli_aviona, aerodromi)
    s=input("Izaberite let koji želite da izmenite:")
    if s in letovi:
        let=letovi[s]
        print("1-izmena polazista:")
        print("2-izmena odredista:")
        print("3-izmena poletanja i sletanja:")
        print("4-izmena prevoznika:")
        print("5-izmena dana letenja:")
        print("6-izmena modela aviona:")
        print("7-izmena cene:")
        izb=input("Unesite opciju:")
        if izb=="1":
            polskr = ""
            while True:
                polaziste = input("Unesite polaziste:")
                t = False

                for aerodrom in aerodromi.values():
                    if polaziste in aerodrom["grad"]:
                        polskr = aerodrom["skracenica"]
                        t = True
                if t == False:
                    print("Greska ne postoji takav grad!")
                else:
                    break
            letovi[s]["polaziste"]=polskr
            sacuvaj(letovi)
            return
        elif izb=="2":
            odrskr = ""
            while True:
                odrediste = input("Unesite odrediste:")
                t = False

                for aerodrom in aerodromi.values():
                    if odrediste in aerodrom["grad"]:
                        odrskr = aerodrom["skracenica"]
                        t = True
                if t == False:
                    print("Greska ne postoji takav grad!")
                else:
                    break
            letovi[s]["odrediste"]=odrskr
            sacuvaj(letovi)
            return
        elif izb=="3":
            poletanje = ""
            while True:
                poletanje = input("Unesite vreme poletanja (HH:MM):")
                t = True
                try:
                    time.strptime(poletanje, '%H:%M')
                    t = True
                except ValueError:
                    print("Greška niste dobro uneli vreme!")
                    t = False
                if t == True:
                    break
            sletanje = ""
            while True:
                sletanje = input("Unesite vreme sletanja (HH:MM):")
                t = True
                try:
                    time.strptime(sletanje, '%H:%M')
                    t = True
                except ValueError:
                    print("Greška niste dobro uneli vreme!")
                    t = False
                if t == True:
                    break
            letovi[s]["poletanje"]=poletanje
            letovi[s]["sletanje"]=sletanje
            sacuvaj(letovi)
            return
        elif izb=="4":
            prevoznik = input("Unesite prevoznika:")
            letovi[s]["prevoznik"]=prevoznik
            sacuvaj(letovi)
            return
        elif izb=="5":
            dani = ""
            while True:
                dani = input("Unesite dane letenja (npr. ponedeljak sreda...):")
                if dani not in "ponedeljak utorak sreda četvrtak petak subota nedelja":
                    print("Greška pogrešno ste upisali dane!!!")
                else:
                    break
            letovi[s]["dani"]=dani
            sacuvaj(letovi)
            return
        elif izb=="6":
            model = ""
            while True:
                model = input("Unesite model aviona:")
                if model not in modeli_aviona:
                    print("Greška uneli ste pogrešan model aviona!!!")
                else:
                    break
            letovi[s]["model"]=model
            sacuvaj(letovi)
            return
        elif izb=="7":
            cena = ""
            while True:
                cena = input("Unesite cenu leta:")
                t = True
                try:
                    c = int(cena)
                    if c <= 0:
                        print("Greška cena ne može biti manja ili jednaka 0!!!")
                        t = False
                except ValueError:
                    print("Greška niste uneli broj!!!")
                    t = False
                if t == True:
                    break
            letovi[s]["cena"]=cena
            sacuvaj(letovi)
            return
        else:
            print("Greška izabrali ste nepostojeću opciju!!!")
    else:
        print("Izabrali ste nepostojeći let!!!")
        return
def sacuvaj(letovi):
    file=open("avionske_karte.txt","w",encoding='utf8')
    for let in letovi.values():
        string= let["broj_leta"]+"|"+let["polaziste"]+"|"+let["odrediste"]+"|"+let["poletanje"]+"|"+let["sletanje"]+"|"+let["ssdana"]+"|"+let["prevoznik"]+"|"+let["dani"]+"|"+let["model"]+"|"+let["cena"]+"\n"
        file.write(string)
    file.close()
    print("Uspešno sačuvani podaci.")