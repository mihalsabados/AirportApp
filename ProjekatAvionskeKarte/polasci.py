import datetime
def fleksibilni_polasci(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi):
    print("=" * 10, "FLEKSIBILNI POLASCI", "=" * 10)
    polaziste = input("Unesite polaziste:")
    odrediste = input("Unesite odredište:")
    datump=datetime.datetime.now()
    datumd=datetime.datetime.now()
    dan_polaska=datetime.timedelta(0)
    dan_dolaska=datetime.timedelta(0)
    while True:
        datum_polaska=input("Unesite datum polaska(dd.mm.yyyy.):")
        try:
            if datum_polaska[:2].isdigit() and datum_polaska[2]=="." and datum_polaska[3:5].isdigit() and datum_polaska[5]=="." and datum_polaska[6:10].isdigit() and datum_polaska[10]==".":
                datump = datetime.datetime(int(datum_polaska[6:10]), int(datum_polaska[3:5]), int(datum_polaska[:2]))
                break
            else:
                print("Uneli ste pogresno vreme!!")
        except:
            print("Uneli ste pogresno vreme!!")
    while True:
        fleksp=input("Unesite broj fleksibilnih dana polaska:")
        try:
            if int(fleksp)>=0:
                dan_polaska=datetime.timedelta(int(fleksp))
                break
            else:
                print("Uneli ste pogresno dane!!")
        except:
            print("Uneli ste pogresno dane!!")
    while True:
        datum_dolaska=input("Unesite datum dolaska(dd.mm.yyyy.):")
        try:
            if datum_dolaska[:2].isdigit() and datum_dolaska[2] == "." and datum_dolaska[3:5].isdigit() and datum_dolaska[5] == "." and datum_dolaska[6:10].isdigit() and datum_dolaska[10]==".":
                datumd=datetime.datetime(int(datum_dolaska[6:10]),int(datum_dolaska[3:5]),int(datum_dolaska[:2]))
                if datumd<datump:
                    print("Greška prvi datum je veci od drugog!!!")
                else:
                    break
            else:
                print("Uneli ste pogresno !!")
        except:
            print("Uneli ste pogresan datum!!")
    while True:
        fleksd = input("Unesite broj fleksibilnih dana dolaska:")
        try:
            if int(fleksd)>=0:
                dan_dolaska = datetime.timedelta(int(fleksd))
                break
            else:
                print("Uneli ste pogresno dane!!")
        except:
            print("Uneli ste pogresan datum!!")
    for let in letovi.values():
        for konlet in konkretni_letovi.values():
            aerodrom=aerodromi[let["polaziste"]]
            aerodrom1=aerodromi[let["odrediste"]]
            if polaziste in aerodrom["grad"] and odrediste in aerodrom1["grad"] and let["broj_leta"]==konlet["broj_leta"]:
                datum_polaska=datetime.datetime(int(konlet["datum_polaska"][6:10]),int(konlet["datum_polaska"][3:5]),int(konlet["datum_polaska"][:2]))
                datum_dolaska=datetime.datetime(int(konlet["datum_dolaska"][6:10]),int(konlet["datum_dolaska"][3:5]),int(konlet["datum_dolaska"][:2]))
                if datump-dan_polaska<=datum_polaska<=datump+dan_polaska and datumd-dan_dolaska <=datum_dolaska<=datumd+dan_dolaska:
                    print(aerodrom["grad"], "(", aerodrom["drzava"], ")", "-" * 5, end='')
                    print(aerodrom1["grad"], "(", aerodrom1["drzava"], "):")
                    print(konlet["datum_polaska"], " - ", let["poletanje"], "----", konlet["datum_dolaska"], " - ",
                          let["sletanje"], "-" * 5, let["prevoznik"])