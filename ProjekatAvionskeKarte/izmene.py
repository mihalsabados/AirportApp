import datetime

from kupoprodaja import proveri


def izmena(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    print("="*10,"IZMENA KARATA","="*10)
    karte=ucitaj()
    print("{:^15}".format("šifra karte") + "\t" + "{:^15}".format("korisničko ime") + "\t" + "{:^15}".format("ime") +
          "\t" + "{:^15}".format("prezime") + "\t" + "{:^15}".format("polazište") + "\t" + "{:^15}".format(
        "odredište") +
          "\t" + "{:^15}".format("datum polaska") + "\t" + "{:^15}".format("datum dolaska") + "\t" + "{:^15}".format(
        "rezrevisano sediste"))
    for karta in karte.values():                                                                                        #prikazivanje svih karata koje nisu obrisane
        if karta["obrisana"]=="ne":
            datump=konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
            datumd=konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
            polaziste=aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
            odrediste=aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]

            print("{:^5}".format(karta["sifra_karte"]) + "\t\t\t" + "{:^10}".format(
                karta["kor_ime"]) + "\t" + "{:^15}".format(karta["ime"]) +
                  "\t" + "{:^15}".format(karta["prezime"]) + "\t" + "{:^15}".format(polaziste) + "\t" + "{:^15}".format(
                odrediste) + "\t" + "{:^15}".format(datump) + "\t" + "{:^15}".format(datumd) + "\t" + "{:^15}".format(
                karta["sediste"]))
    sifra=input("Unesite šifru karte koju želite da izmenite:")
    if sifra in karte and karte[sifra]["obrisana"]=="ne":                                                               #provera da li sifra postoji u kartama i da ona nije obrisana
        karta=karte[sifra]
        print("{:^15}".format("šifra karte") + "\t" + "{:^15}".format("korisničko ime") + "\t" + "{:^15}".format("ime") +
              "\t" + "{:^15}".format("prezime") + "\t" + "{:^15}".format("polazište") + "\t" + "{:^15}".format("odredište") +
              "\t" + "{:^15}".format("datum polaska") + "\t" + "{:^15}".format("datum dolaska") + "\t" + "{:^15}".format("rezrevisano sediste"))
        print("{:^5}".format(karta["sifra_karte"]) + "\t\t\t" + "{:^10}".format(karta["kor_ime"]) + "\t" + "{:^15}".format(karta["ime"]) +
              "\t" + "{:^15}".format(karta["prezime"]) + "\t" + "{:^15}".format(polaziste) + "\t" + "{:^15}".format(odrediste) + "\t" + "{:^15}".format(datump) + "\t" + "{:^15}".format(datumd) + "\t" + "{:^15}".format(karta["sediste"]))
    else:
        print("Šifra karte ne postoji!!!")
        return
    print("1-izmeni datume polaska i dolaska")
    print("2-izmena broja leta")
    print("3-izmena sedista")
    while True:
        s=input("Izaberite opciju:")
        if s=="1":
            while True:
                datpstr=input("Unesite datum polaska (dd.mm.yyyy.):")
                datdstr=input("Unesite datum dolaska (dd.mm.yyyy.):")
                t=True
                try:
                    kom=datpstr.split(".")
                    kom1=datdstr.split(".")
                    datump=datetime.datetime(int(kom[2]),int(kom[1]),int(kom[0]))
                    datumd=datetime.datetime(int(kom1[2]),int(kom1[1]),int(kom1[0]))
                    if datump>datumd:
                        t=False
                except:
                    print("Greška pogrešno ste uneli datume!!!")
                    t=False
                if t==True:
                    break
            konkretni_letovi[karte[sifra]["sifra_leta"]]["datum_polaska"]=datpstr
            konkretni_letovi[karte[sifra]["sifra_leta"]]["datum_dolaska"] = datdstr
            sacuvaj_letove(konkretni_letovi)
            return
        if s=="2":
            sifra_leta=input("Unesite sifru leta (morate i nule pisati!):")
            if sifra_leta in konkretni_letovi:
                t = proveri(modeli_aviona, letovi, konkretni_letovi, sifra_leta)                                        #provera da li ima slobodnih mesta na letu
                if t == True:  # ukoliko ima slobodnih mesta
                    karte[sifra]["sifra_leta"]=sifra_leta
                    izmena_sedista(karte,sifra,modeli_aviona,konkretni_letovi,letovi)
                    sacuvaj(karte)
                else:
                    print("Greška sva mesta za izabrani let su popunjena!!!")
            return
        if s=="3":
            if karte[sifra]["sediste"]!="ne":
                izmena_sedista(karte,sifra,modeli_aviona,konkretni_letovi,letovi)
            else:
                print("Greška let nije čekiran!!!")
            return
        else:
            print("Pogrešna opcija!!!")
def brisanje(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    print("="*10,"BRISANJE KARATA","="*10)
    karte = ucitaj()
    print("{:^15}".format("šifra karte") + "\t" + "{:^15}".format("korisničko ime") + "\t" + "{:^15}".format("ime") +
                  "\t" + "{:^15}".format("prezime") + "\t" + "{:^15}".format("polazište") + "\t" + "{:^15}".format("odredište") +
                  "\t" + "{:^15}".format("datum polaska") + "\t" + "{:^15}".format("datum dolaska") + "\t" + "{:^15}".format("rezrevisano sediste"))
    for karta in karte.values():  # prikazivanje svih karata koje nisu obrisane
        if karta["obrisana"] == "ne":
            datump = konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
            datumd = konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
            polaziste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
            odrediste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]

            print("{:^5}".format(karta["sifra_karte"]) + "\t\t\t" + "{:^10}".format(
                karta["kor_ime"]) + "\t" + "{:^15}".format(karta["ime"]) +
                  "\t" + "{:^15}".format(karta["prezime"]) + "\t" + "{:^15}".format(polaziste) + "\t" + "{:^15}".format(
                odrediste) + "\t" + "{:^15}".format(datump) + "\t" + "{:^15}".format(datumd) + "\t" + "{:^15}".format(
                karta["sediste"]))
    sifra = input("Unesite šifru karte koju želite da obrišete:")
    if sifra in karte and karte[sifra]["obrisana"]=="ne":
        karte[sifra]["obrisana"]="da"
        sacuvaj(karte)
    else:
        print("Ne postoji takva šifra!!!")
def pretraga_prodatih(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    print("="*10,"PRETRAGA KARATA","="*10)
    karte=ucitaj()
    print("1-Pretraga po polazištu")
    print("2-Pretraga po odredištu")
    print("3-Pretraga po datumu polaska")
    print("4-Pretraga po datumu dolaska")
    print("5-Pretraga po putniku")
    s=input("Unesite opciju:")
    polaziste=""
    odrediste=""
    datump=""
    datumd=""
    ime=""
    prezime=""
    if s=="1":
        polaziste=input("Unesite polazište:")
    elif s=="2":
        odrediste=input("Unesite odredište:")
    elif s=="3":
        datump=input("Unesite datum polaska (dd.mm.yyyy.):")
    elif s=="4":
        datumd=input("Unesite datum dolaska (dd.mm.yyyy.):")
    elif s=="5":
        ime=input("Unesite ime:")
        prezime=input("Unesite prezime:")
    else:
        print("Greška uneli ste nepostojeću opciju!!!")
        return
    t=False
    for karta in karte.values():
        pol=aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
        odr=aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]
        datp=konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
        datd=konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
        if polaziste in pol and odrediste in odr and datump in datp and datumd in datd and ime in karta["ime"] and prezime in karta["prezime"] and ime in karta["ime"] and prezime in karta["prezime"] and karta["obrisana"]=="ne":
            t=True
            print(karta["sifra_karte"] + "\t" + karta["kor_ime"] + "\t" + karta["ime"] + "\t" + karta[
                  "prezime"] + "\t" + pol + "\t" + odr + "\t" + datp + "\t" + datd + "\t" + karta["sediste"])
    if t==False:
        print("Nema rezultata pretrage!!")
def sacuvaj(karte):
    file = open("karte.txt", "w", encoding="utf8")  # upisivanje čekirane karte u datoteku
    for karta in karte.values():
        string = karta["sifra_karte"] + "|" + karta["kor_ime"] + "|" + karta["ime"] + "|" + karta["prezime"] + "|" + \
                 karta["broj_pasosa"] + "|" + karta["drzavljanstvo"] + "|" + karta["telefon"] + "|" + karta[
                     "email"] + "|" + karta["pol"] + "|" + karta["sifra_leta"] + "|" + karta["cena"] + "|" + karta[
                     "sediste"] + "|" + karta["obrisana"] + "|" + karta["dan_kupovine"] + "\n"
        try:
            file.write(string)
        except:
            print("Greška prilikom čuvanja podataka!")
    file.close()
    print("Podaci uspešno sačuvani.")
def izmena_sedista(karte,sifra,modeli_aviona,konkretni_letovi,letovi):
    karte[sifra]["sediste"]="ne"
    print("Prikaz sedišta:")
    sifra_leta = karte[sifra]["sifra_leta"]
    broj_redova = modeli_aviona[letovi[konkretni_letovi[sifra_leta]["broj_leta"]]["model"]][
        "broj_redova"]  # uzimanje broja redova konkretnog leta
    broj_redova = eval(broj_redova)
    pozicija_sedista = modeli_aviona[letovi[konkretni_letovi[sifra_leta]["broj_leta"]]["model"]][
        "pozicija_sedista"]  # i pozicije sedista
    for i in range(1, broj_redova + 1):  # ispis redova i broja sedista
        print("Red ", i, ": ", end='')
        string = pozicija_sedista
        for karta in karte.values():
            if karta["sifra_leta"] == sifra_leta and karta["sediste"] != "ne":  # provera koja mesta su vec zauzeta
                kom = karta["sediste"].split('-')
                if i == eval(kom[0]):
                    string = string.replace(kom[1], "X")
        print(string)
    while True:
        rez = input(
            "Unesite broj reda i poziciju sedista(Velikim Slovom!) odvojeno znakom - (npr. 10-B):")  # Čekiranje broja reda i sedista
        t = True
        if "-" in rez:
            spl = rez.split("-")
            for karta in karte.values():  # provera da li je to mesto vec rezervisano
                if rez in karta["sediste"]:
                    print("Greška to mesto je već zauzeto")
                    t = False
            if eval(spl[0]) < 0 or eval(spl[0]) > broj_redova or spl[1] not in pozicija_sedista:
                print("Greška niste dobro uneli!!!")

            elif t == True:
                break
        else:
            print("Greška niste dobro uneli!!!")
    karte[sifra]["sediste"] = rez
    sacuvaj(karte)
def ucitaj():                                                                                   #ucitavanje karti iz fajla
    karte = {}
    file = open("karte.txt", "r", encoding="utf8")
    lines = file.readlines()
    for line in lines:
        parts = line.split("|")
        parts[-1] = parts[-1].replace("\n", "")
        karta = {"sifra_karte": parts[0], "kor_ime": parts[1], "ime": parts[2], "prezime": parts[3],
                 "broj_pasosa": parts[4], "drzavljanstvo": parts[5], "telefon": parts[6], "email": parts[7],
                 "pol": parts[8], "sifra_leta": parts[9], "cena": parts[10], "sediste": parts[11],
                 "obrisana": parts[12], "dan_kupovine": parts[13]}
        karte[parts[0]] = karta
    file.close()
    return karte
def sacuvaj_letove(konkretni_letovi):
    file=open("konkretni_letovi.txt","w")
    for kon in konkretni_letovi.values():
        string=kon["sifra"]+"|"+kon["broj_leta"]+"|"+kon["datum_polaska"]+"|"+kon["datum_dolaska"]+"\n"
        file.write(string)
    file.close()
    print("Podaci uspešno sačuvani.")
def brisanje_menadzer(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    print("="*10,"BRISANJE KARATA","="*10)
    karte=ucitaj()
    print("{:^15}".format("šifra karte") + "\t" + "{:^15}".format("korisničko ime") + "\t" + "{:^15}".format("ime") +
          "\t" + "{:^15}".format("prezime") + "\t" + "{:^15}".format("polazište") + "\t" + "{:^15}".format(
        "odredište") +
          "\t" + "{:^15}".format("datum polaska") + "\t" + "{:^15}".format("datum dolaska") + "\t" + "{:^15}".format(
        "rezrevisano sediste"))
    for karta in karte.values():  # prikazivanje svih karata koje jesu obrisane
        if karta["obrisana"] == "da":
            datump = konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
            datumd = konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
            polaziste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
            odrediste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]

            print("{:^5}".format(karta["sifra_karte"]) + "\t\t\t" + "{:^10}".format(
                karta["kor_ime"]) + "\t" + "{:^15}".format(karta["ime"]) +
                  "\t" + "{:^15}".format(karta["prezime"]) + "\t" + "{:^15}".format(polaziste) + "\t" + "{:^15}".format(
                odrediste) + "\t" + "{:^15}".format(datump) + "\t" + "{:^15}".format(datumd) + "\t" + "{:^15}".format(
                karta["sediste"]))
    sifra = input("Unesite šifru karte koju želite da obrišete/aktivirate:")
    if sifra in karte and karte[sifra]["obrisana"] == "da":
        print("1-aktiviraj")
        print("2-trajno obrisi")
        while True:
            s=input("Izaberite opciju:")
            if s=="1":
                karte[sifra]["obrisana"]="ne"
                sacuvaj(karte)
                return
            if s=="2":
                file = open("karte.txt", "w", encoding="utf8")  #   trajno brisanje karte
                for karta in karte.values():
                    if karta["sifra_karte"]!=karte[sifra]["sifra_karte"]:
                        string = karta["sifra_karte"] + "|" + karta["kor_ime"] + "|" + karta["ime"] + "|" + karta[
                            "prezime"] + "|" + \
                                 karta["broj_pasosa"] + "|" + karta["drzavljanstvo"] + "|" + karta["telefon"] + "|" + karta[
                                     "email"] + "|" + karta["pol"] + "|" + karta["sifra_leta"] + "|" + karta["cena"] + "|" + \
                                 karta[
                                     "sediste"] + "|" + karta["obrisana"] + "|" + karta["dan_kupovine"] + "\n"
                        try:
                            file.write(string)
                        except:
                            print("Greška prilikom čuvanja podataka!")
                file.close()
                print("Podaci uspešno sačuvani.")
                return
            else:
                print("Izabrali ste nepostojeću funkciju!!!")
    else:
        print("Ne postoji takva šifra!!!")


