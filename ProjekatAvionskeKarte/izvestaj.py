import datetime
from izmene import ucitaj
def izvestavanje(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,pr_korisnik):
    print("=" * 10, "IZVEŠTAJ", "=" * 10)
    karte=ucitaj()
    print("1-lista prodatih karata za izabrani dan prodaje")
    print("2-lista prodatih karata za izabrani dan polaska")
    print("3-lista prodatih karata za izabrani dan prodaje i izabranog prodavca")
    print("4-ukupan broj i cena prodatih karata za izabrani dan prodaje")
    print("5-ukupan broj i cena prodatih karata za izabrani dan polaska")
    print("6-ukupan broj i cena prodatih karata za izabrani dan prodaje i izabranog prodavca")
    print("7-ukupan broj i cena prodatih karata u poslednjih 30 dana, po prodavcima.")
    while True:
        s=input("Izaberite opciju:")
        if s=="1":
            while True:
                danprodaje=input("Unesite datum prodaje (dd.MM.yyyy.):")
                t=True
                if "." in danprodaje:
                    try:
                        delovi=danprodaje.split(".")
                        datetime.datetime(int(delovi[2]),int(delovi[1]),int(delovi[0]))
                    except ValueError:
                        print("Pogrešno ste uneli datum")
                        t=False
                else:
                    print("Pogrešno ste uneli datum!!!")
                if t==True:
                    break
            for karta in karte.values():
                datump = konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
                datumd = konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
                polaziste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
                odrediste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]
                if karta["dan_kupovine"]==danprodaje:
                   print("{:^5}".format(karta["sifra_karte"]) + "\t\t\t" + "{:^10}".format(karta["kor_ime"])
                          + "\t" + "{:^15}".format(karta["ime"]) +"\t" + "{:^15}".format(karta["prezime"]) + "\t" + "{:^15}".format(polaziste) + "\t" + "{:^15}".format(
                        odrediste) + "\t" + "{:^15}".format(datump) + "\t" + "{:^15}".format(
                        datumd) + "\t" + "{:^15}".format(
                        karta["sediste"]))
            return
        elif s=="2":
            while True:
                danpolaska=input("Unesite datum polaska (dd.MM.yyyy.):")
                t=True
                if "." in danpolaska:
                    try:
                        delovi=danpolaska.split(".")
                        datetime.datetime(int(delovi[2]),int(delovi[1]),int(delovi[0]))
                    except ValueError:
                        print("Pogrešno ste uneli datum")
                        t=False
                else:
                    print("Pogrešno ste uneli datum!!!")
                if t==True:
                    break
            for karta in karte.values():
                datump = konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
                datumd = konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
                polaziste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
                odrediste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]
                if datump==danpolaska:
                    print("{:^5}".format(karta["sifra_karte"]) + "\t\t\t" + "{:^10}".format(karta["kor_ime"])
                          + "\t" + "{:^15}".format(karta["ime"]) +"\t" + "{:^15}".format(karta["prezime"]) + "\t" + "{:^15}".format(polaziste) + "\t" + "{:^15}".format(
                        odrediste) + "\t" + "{:^15}".format(datump) + "\t" + "{:^15}".format(datumd) + "\t" + "{:^15}".format(karta["sediste"]))
            return
        elif s=="3":
            while True:
                danprodaje=input("Unesite datum prodaje (dd.MM.yyyy.):")
                prodavac=input("Unesite korisničko ime prodavca:")
                t=True
                if "." in danprodaje:
                    try:
                        delovi=danprodaje.split(".")
                        datetime.datetime(int(delovi[2]),int(delovi[1]),int(delovi[0]))
                    except ValueError:
                        print("Pogrešno ste uneli datum")
                        t=False
                else:
                    print("Pogrešno ste uneli datum!!!")
                if prodavac not in korisnici and korisnici[prodavac]["uloga"]!="prodavac":
                    print("Ne postoji takav prodavac!!!")
                else:
                    break
                if t==True:
                    break
            for karta in karte.values():
                datump = konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
                datumd = konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
                polaziste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
                odrediste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]
                if karta["dan_kupovine"]==danprodaje and karta["kor_ime"]==prodavac:
                   print("{:^5}".format(karta["sifra_karte"]) + "\t\t\t" + "{:^10}".format(karta["kor_ime"])
                          + "\t" + "{:^15}".format(karta["ime"]) +"\t" + "{:^15}".format(karta["prezime"]) + "\t" + "{:^15}".format(polaziste) + "\t" + "{:^15}".format(
                        odrediste) + "\t" + "{:^15}".format(datump) + "\t" + "{:^15}".format(
                        datumd) + "\t" + "{:^15}".format(
                        karta["sediste"]))
            return
        elif s=="4":
            while True:
                danprodaje=input("Unesite datum prodaje (dd.MM.yyyy.):")
                t=True
                if "." in danprodaje:
                    try:
                        delovi=danprodaje.split(".")
                        datetime.datetime(int(delovi[2]),int(delovi[1]),int(delovi[0]))
                    except ValueError:
                        print("Pogrešno ste uneli datum")
                        t=False
                else:
                    print("Pogrešno ste uneli datum!!!")
                if t==True:
                    break
            broj=0
            cena=0
            for karta in karte.values():
                datump = konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
                datumd = konkretni_letovi[karta["sifra_leta"]]["datum_dolaska"]
                polaziste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["polaziste"]]["grad"]
                odrediste = aerodromi[letovi[konkretni_letovi[karta["sifra_leta"]]["broj_leta"]]["odrediste"]]["grad"]
                if karta["dan_kupovine"]==danprodaje:
                    broj+=1
                    cena+=int(karta["cena"])
            print("Ukupan broj prodatih karata je: ", broj, " a cena: ", cena)
            return
        elif s=="5":
            while True:
                danpolaska=input("Unesite datum polaska (dd.MM.yyyy.):")
                t=True
                if "." in danpolaska:
                    try:
                        delovi=danpolaska.split(".")
                        datetime.datetime(int(delovi[2]),int(delovi[1]),int(delovi[0]))
                    except ValueError:
                        print("Pogrešno ste uneli datum")
                        t=False
                else:
                    print("Pogrešno ste uneli datum!!!")
                if t==True:
                    break
            broj=0
            cena=0
            for karta in karte.values():
                datump = konkretni_letovi[karta["sifra_leta"]]["datum_polaska"]
                if datump==danpolaska:
                    broj+=1
                    cena+=int(karta["cena"])
            print("Ukupan broj prodatih karata je: ",broj," a cena: ",cena)
            return
        elif s=="6":
            while True:
                danprodaje=input("Unesite datum prodaje (dd.MM.yyyy.):")
                prodavac=input("Unesite korisničko ime prodavca:")
                t=True
                if "." in danprodaje:
                    try:
                        delovi=danprodaje.split(".")
                        datetime.datetime(int(delovi[2]),int(delovi[1]),int(delovi[0]))
                    except ValueError:
                        print("Pogrešno ste uneli datum")
                        t=False
                else:
                    print("Pogrešno ste uneli datum!!!")
                if prodavac not in korisnici and korisnici[prodavac]["uloga"]!="prodavac":
                    print("Ne postoji takav prodavac!!!")
                else:
                    break
                if t==True:
                    break
            broj=0
            cena=0
            for karta in karte.values():
                if karta["dan_kupovine"]==danprodaje and karta["kor_ime"]==prodavac:
                    broj += 1
                    cena += int(karta["cena"])
            print("Ukupan broj prodatih karata je: ",broj," a cena: ",cena)
            return
        elif s=="7":
            danas=datetime.datetime.now()
            period=datetime.timedelta(days=30)
            for korisnik in korisnici.values():
                broj = 0
                cena = 0
                if korisnik["uloga"]=="prodavac":
                    for karta in karte.values():
                        parts=karta["dan_kupovine"].split(".")
                        dankup=datetime.datetime(int(parts[2]),int(parts[1]),int(parts[0]))
                        if danas-period <= dankup <= danas and karta["kor_ime"]==korisnik["kor_ime"]:
                            broj += 1
                            cena += int(karta["cena"])
                    print("Ukupan broj prodatih karata za ",korisnik["kor_ime"]," je: ",broj," a cena: ",cena)
            return
        else:
            print("Uneli ste nepostojeću opciju!!!")