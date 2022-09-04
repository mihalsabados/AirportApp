def pregled_letova(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi):
    print("="*10,"Pregled letova","="*10)
    for let in letovi.values():
        aerodrom=aerodromi[let["polaziste"]]
        print(aerodrom["grad"],"(",aerodrom["drzava"],")","-"*5,end='')
        aerodrom=aerodromi[let["odrediste"]]
        print(aerodrom["grad"],"(",aerodrom["drzava"],"):")
        for konlet in konkretni_letovi.values():
            if let["broj_leta"]==konlet["broj_leta"]:
                print(konlet["datum_polaska"]," - ",let["poletanje"],"----",konlet["datum_dolaska"]," - ",let["sletanje"],"-"*5,let["prevoznik"])
def pregled_nerealizovanih_karata(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,pr_korisnik):
    file = open("karte.txt", "r",encoding="utf8")
    lines = file.readlines()
    t=False
    for line in lines:
        parts = line.split("|")
        if parts[1] == pr_korisnik["kor_ime"]:
            t=True
            sifra_leta=parts[9]
            let = letovi[konkretni_letovi[sifra_leta]["broj_leta"]]
            aerodrom = aerodromi[let["polaziste"]]
            aerodrom1 = aerodromi[let["odrediste"]]
            pgrad = aerodrom["grad"]
            dgrad = aerodrom1["grad"]
            datump = konkretni_letovi[sifra_leta]["datum_polaska"]
            datumd = konkretni_letovi[sifra_leta]["datum_dolaska"]
            vremep = let["poletanje"]
            vremed = let["sletanje"]
            cena = let["cena"]
            print(parts[0],"\t",parts[1],"\t",parts[2],"\t",parts[3],"\t",sifra_leta, "\t", pgrad, "\t", dgrad, "\t", datump, "\t", vremep, "\t", datumd, "\t", vremed, "\t",cena)
    if t==False:
        print("Korisnik nije kupio ni jednu kartu!!!")