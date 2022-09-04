def pretraga(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi):
    while True:
            print("="*10,"PRETRAGA","="*10)
            print("1-po polazištu")
            print("2-po odredištu")
            print("3-po datumu polaska")
            print("4-po datumu dolaska")
            print("5-po vremenu poletanja")
            print("6-po vremenu sletanja")
            print("7-po prevozniku")
            s=input("Unesite kriterijum za pretragu:")
            polaziste=""
            odrediste=""
            datum_polaska=""
            datum_dolaska=""
            vreme_poletanja=""
            vreme_sletanja=""
            prevoznik=""
            if s == "1":
                polaziste=input("Unesite polazište:")
                break
            elif s == "2":
                odrediste = input("Unesite odredište:")
                break
            elif s == "3":
                while True:
                    datum_polaska = input("Unesite datum polaska (dd.mm.yyyy.):")
                    try:
                        if datum_polaska[:2].isdigit() and datum_polaska[2]=="." and datum_polaska[3:5].isdigit() and datum_polaska[5]=="." and datum_polaska[6:10].isdigit() and datum_polaska[10]==".":
                            break
                        else:
                            print("Uneli ste pogresno datum!!")
                    except:
                        print("Uneli ste pogresno datum!!")
                break
            elif s == "4":
                while True:
                    datum_dolaska = input("Unesite datum polaska (dd.mm.yyyy.):")
                    try:
                        if datum_dolaska[:2].isdigit() and datum_dolaska[2] == "." and datum_dolaska[3:5].isdigit() and datum_dolaska[5] == "." and datum_dolaska[6:10].isdigit() and datum_dolaska[10]==".":
                            break
                        else:
                            print("Uneli ste pogresno datum!!")
                    except:
                        print("Uneli ste pogresno datum!!")
                break
            elif s == "5":
                while True:
                    vreme_poletanja = input("Unesite vreme poletanja:")
                    try:
                        if vreme_poletanja[:2].isdigit() and vreme_poletanja[2]==":" and vreme_poletanja[3:].isdigit() and  0<int(vreme_poletanja[:2])<=24 and 0<=int(vreme_poletanja[3:])<=60:
                            break
                        else:
                            print("Uneli ste pogresno vreme!!")
                    except:
                        print("Uneli ste pogresno vreme!!")
                break
            elif s == "6":
                while True:
                    vreme_sletanja = input("Unesite vreme poletanja:")
                    try:
                        if vreme_sletanja[:2].isdigit() and vreme_sletanja[2] == ":" and vreme_sletanja[3:].isdigit() and 0 < int(vreme_sletanja[:2]) <= 24 and 0 <= int(vreme_sletanja[3:]) < 60:
                            break
                        else:
                            print("Uneli ste pogresno vreme!!")
                    except:
                        print("Uneli ste pogresno vreme!!")
                break
            elif s == "7":
                prevoznik = input("Unesite prevoznika:")
                break
            else:
                print("Uneli ste nepostojeću operaciju!!!")

    for let in letovi.values():
        for konlet in konkretni_letovi.values():
            aerodrom=aerodromi[let["polaziste"]]
            aerodrom1=aerodromi[let["odrediste"]]
            if polaziste in aerodrom["grad"] and odrediste in aerodrom1["grad"] and prevoznik in let["prevoznik"] and vreme_poletanja in let["poletanje"] and vreme_sletanja in let["sletanje"] and let["broj_leta"]==konlet["broj_leta"] and datum_dolaska in konlet["datum_dolaska"] and datum_polaska in konlet["datum_polaska"]:
                print(aerodrom["grad"],"(",aerodrom["drzava"],")","-"*5,end='')
                print(aerodrom1["grad"],"(",aerodrom1["drzava"],"):")
                print(konlet["datum_polaska"]," - ",let["poletanje"],"----",konlet["datum_dolaska"]," - ",let["sletanje"],"-"*5,let["prevoznik"])