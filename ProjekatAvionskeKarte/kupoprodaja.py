import datetime
def kupovina(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    print("=" * 10, "KUPOVINA KARATA", "=" * 10)

    t=True
    while t:
        polaziste = input("Unesite polazište:")
        odrediste = input("Unesite odredište:")
        for let in letovi.values():
            for konlet in konkretni_letovi.values():
                aerodrom=aerodromi[let["polaziste"]]
                aerodrom1=aerodromi[let["odrediste"]]
                if polaziste in aerodrom["grad"] and odrediste in aerodrom1["grad"] and let["broj_leta"]==konlet["broj_leta"]:
                    print(konlet["sifra"],"\t",end='')
                    print(aerodrom["grad"],"(",aerodrom["drzava"],")","-"*5,end='')
                    print(aerodrom1["grad"],"(",aerodrom1["drzava"],"):",end='')
                    print(konlet["datum_polaska"]," - ",let["poletanje"],"----",konlet["datum_dolaska"]," - ",let["sletanje"],"-"*5,let["prevoznik"],"-",let["cena"])
                    t=False
        if t==True:
            print("Ne postoji takav let!!!")
    sifra_leta=input("Unesite šifru leta koju želite da kupite (morate i nule pisati!):")
    if sifra_leta in konkretni_letovi:

        t=proveri(modeli_aviona,letovi,konkretni_letovi,sifra_leta)
        if t==True :                                                                      #ukoliko ima slobodnih mesta
            prijava_za_let(sifra_leta,korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik)
        else:
            print("Greška sva mesta za izabrani let su popunjena!!!")
    else:
        print("Ne postoji šifra koju ste uneli!!!")
def proveri(modeli_aviona,letovi,konkretni_letovi,sifra_leta):
    avion=modeli_aviona[letovi[konkretni_letovi[sifra_leta]["broj_leta"]]["model"]]
    br_redova=int(avion["broj_redova"])
    br_sedista=len(avion["pozicija_sedista"].split(" "))
    broj=br_redova*br_sedista
    file=open("karte.txt","r")
    lines = file.readlines()
    ind=0
    for line in lines:
        parts=line.split("|")
        if parts[8]==sifra_leta:
            ind+=1
    if broj<=ind:
        return False
    else:
        return True

def sacuvaj(korisnik,let,modeli_aviona,sifra_leta):
    file=open("karte.txt","r",encoding="utf8")
    lines=file.readlines()
    sifra_karte=1
    if len(lines)>0:
        line=lines[-1].split("|")
        sifra_karte=eval(line[0])+1
    file.close()
    file = open("karte.txt", "a+",encoding="utf8")
    avion=modeli_aviona[let["model"]]
    danas=datetime.datetime.now()
    datump=danas.strftime("%d.%m.%Y.")
    string=str(sifra_karte)+"|"+korisnik["kor_ime"]+"|"+korisnik["ime"]+"|"+korisnik["prezime"]+"|"+korisnik["broj_pasoša"]+"|"+korisnik["državljanstvo"]+"|"+korisnik["telefon"]+"|"+korisnik["email"]+"|"+korisnik["pol"]+"|"+sifra_leta+"|"+let["cena"]+"|"+"ne"+"|"+"ne"+"|"+datump+"\n"
    try:
        file.write(string)
    except:
        print("Greška prilikom čuvanja")
    file.close()
    print("Uspešno sačuvana kupovina.")
def prijava_za_let(sifra_leta,korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    let = letovi[konkretni_letovi[sifra_leta]["broj_leta"]]
    aerodrom = aerodromi[let["polaziste"]]
    aerodrom1 = aerodromi[let["odrediste"]]
    pgrad = aerodrom["grad"]
    dgrad = aerodrom1["grad"]
    datump = konkretni_letovi[sifra_leta]["datum_polaska"]
    datumd = konkretni_letovi[sifra_leta]["datum_dolaska"]
    vremep = let["poletanje"]
    vremed = let["sletanje"]
    cena=let["cena"]
    print(sifra_leta, "\t", pgrad, "\t", dgrad, "\t", datump, "\t", vremep, "\t", datumd, "\t", vremed, "\t", cena)
    while True:
        if korisnik["uloga"]=="kupac":                                                                                  #ako je korisnik kupac on bira da li kupuje za sebe ili za nekog drugog
            print("1-kupovina za ", korisnik["kor_ime"])
            print("2-kupovina za drugog korisnika")
        elif korisnik["uloga"]=="prodavac":                                                                             #ukoliko je prodavac on ili prodaje za postojećeg ili za neregistrovanog kupca
            print("1-Kupovina za postojećeg korisnika")
            print("2-Kupovina za neregistrovanog korisnika")
        s=input("Izaberite opciju:")
        if s == "1":
            isti_korisnik = korisnici[korisnik["kor_ime"]]
            if korisnik["uloga"]=="prodavac":
                kor=input("Unesite korisničko ime:")
                if kor in korisnici:
                    isti_korisnik=korisnici[kor]
                else:
                    print("Ne postoji takav korisnik!!!")
                    return
            while True:
                izbor=input("Potvrdite kupovinu (da/ne):")
                if izbor=="da":
                    sacuvaj(isti_korisnik, let, modeli_aviona, sifra_leta)
                    break;
                elif izbor=="ne":
                    return
                else:
                    print("Uneli ste pogrešan izbor!!!")
            print("1-nastavi sa kupovinom")
            print("2-nastavi sa kupovinom karte za saputnika")
            print("x-izađi")
            while True:
                str=input("Unesite opciju:")
                if str=="1":
                    datum_dolaska=datetime.datetime(int(datumd[6:10]), int(datumd[3:5]), int(datumd[:2]),int(vremed[:2]),int(vremed[3:]))               #postavljanje datuma dolaska
                    fleks_vreme=datum_dolaska+datetime.timedelta(hours=2)                                                                               #postavljanje fleksibilnog vremena, 2 sata fleksibilna
                    polazak=aerodrom1["skracenica"]
                    t=False                                                                                                                             #postavljanje indikatora da li postoje uopste povezani letovi
                    sifre=[]
                    for let in letovi.values():
                        for konlet in konkretni_letovi.values():                                                                                        #prolazak kroz biblioteku radi pronalaženja povezanih letova
                            aerodrom = aerodromi[let["polaziste"]]
                            aerodrom1 = aerodromi[let["odrediste"]]
                            datump = konlet["datum_polaska"]
                            vremep = letovi[konlet["broj_leta"]]["poletanje"]
                            datd=datetime.datetime(int(datump[6:10]), int(datump[3:5]), int(datump[:2]),int(vremep[:2]),int(vremep[3:]))
                            if polazak in let["polaziste"] and let["broj_leta"]==konlet["broj_leta"] and datum_dolaska<datd<=fleks_vreme:
                                print(konlet["sifra"], "\t",aerodrom["grad"], "(", aerodrom["drzava"], ")", "-" * 5,aerodrom1["grad"], "(", aerodrom1["drzava"], "):",konlet["datum_polaska"], " - ", let["poletanje"], "----", konlet["datum_dolaska"],
                                      " - ", let["sletanje"], "-" * 5, let["prevoznik"], "-", let["cena"])
                                sifre.append(konlet["sifra"])
                                t=True
                    if t==True:                                                                                                                          #ukoliko postoje povezani letovi onda se korisnik moze prijaviti za taj let
                        sifra_leta = input("Unesite šifru leta koju želite da kupite (morate i nule pisati!):")
                        if sifra_leta in sifre:

                            t = proveri(modeli_aviona, letovi, konkretni_letovi, sifra_leta)
                            if t == True:
                                prijava_za_let(sifra_leta, korisnici, letovi, konkretni_letovi, modeli_aviona,
                                                       aerodromi, korisnik)
                            else:
                                print("Greška sva mesta za izabrani let su popunjena!!!")
                        else:
                            print("Ne postoji šifra koju ste uneli!!!")
                    else:                                                                                                                                   #ukoliko ne postoji povezani let
                        print("Ne postoje povezani letovi!!!")
                        return
                elif str=="2":
                    t = proveri(modeli_aviona, letovi, konkretni_letovi, sifra_leta)
                    if t == True:
                        karta_za_drugog(sifra_leta, korisnici, letovi, konkretni_letovi, modeli_aviona, aerodromi,korisnik)
                        return
                    else:
                        print("Greška sva mesta za izabrani let su popunjena!!!")

                elif str=="x":
                    return
                else:
                    print("Uneli ste pogrešnu opciju!!!")
        elif s == "2":
            karta_za_drugog(sifra_leta,korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik)
            return
        else:
            print("Uneli ste nepostojeću opciju!!!")

def karta_za_drugog(sifra_leta,korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    let = letovi[konkretni_letovi[sifra_leta]["broj_leta"]]
    print("Unesite podatke za drugog korisnika")
    ime = input("Unesite ime:")
    prezime = input("Unesite prezime:")
    drugi_korisnik = {"kor_ime": korisnik["kor_ime"], "ime": ime, "prezime": prezime, "broj_pasoša": "",
                      "državljanstvo": "", "telefon": "", "email": "", "pol": ""}
    while True:
        izbor = input("Potvrdite kupovinu (da/ne):")
        if izbor == "da":
            sacuvaj(drugi_korisnik, let, modeli_aviona, sifra_leta)
            return
        elif izbor == "ne":
            return
        else:
            print("Uneli ste pogrešan izbor!!!")
def checkin(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,korisnik):
    print("="*10,"Čekiranje karte","="*10)
    file=open("karte.txt","r",encoding="utf8")
    lines=file.readlines()
    karte={}
    sifre=[]
    t=True
    for line in lines:
        parts=line.split("|")
        parts[-1]=parts[-1].replace("\n","")
        karta={"sifra_karte":parts[0],"kor_ime":parts[1],"ime":parts[2],"prezime":parts[3],"broj_pasosa":parts[4],"drzavljanstvo":parts[5],"telefon":parts[6],"email":parts[7],"pol":parts[8],"sifra_leta":parts[9],"cena":parts[10],"sediste":parts[11],"obrisana":parts[12],"dan_kupovine":parts[13]}
        karte[parts[0]]=karta
        konlet=konkretni_letovi[parts[9]]
        datump=konlet["datum_polaska"]
        brleta=konlet["broj_leta"]
        vremep=letovi[brleta]["poletanje"]
        datpol=datetime.datetime(int(datump[6:10]), int(datump[3:5]), int(datump[:2]),int(vremep[:2]),int(vremep[3:]))
        fleksdan=datetime.timedelta(days=2)
        trenutni=datetime.datetime.now()
        polaziste=aerodromi[letovi[konlet["broj_leta"]]["polaziste"]]["grad"]
        odrediste=aerodromi[letovi[konlet["broj_leta"]]["odrediste"]]["grad"]
        if datpol-fleksdan<=trenutni<datpol and karte[parts[0]]["sediste"]=="ne" and karte[parts[0]]["obrisana"]=="ne":  #ukoliko postoji karta na korisnicko ime trenutno prijavljenog korisnika i karta nije čekirana ni izbrisana
            if korisnik["uloga"] == "kupac" and parts[1] == korisnik["kor_ime"]:
                sifre.append(parts[0])
                string=parts[0]+"\t"+parts[1]+"\t"+parts[2]+"\t"+polaziste+"\t"+odrediste+"\t"+datump                                #karte se prikazuju
                print(string)
                t=False
            elif korisnik["uloga"] == "prodavac":
                sifre.append(parts[0])
                string = parts[0] + "\t" + parts[1] + "\t" + parts[2] + "\t" + polaziste + "\t" + odrediste + "\t" + datump  # karte se prikazuju
                print(string)
                t=False
    if t==True:
        print("Nema letova koje možete da čekirate!")
        return
    file.close()
    sifra=input("Odaberite let koji želite da čekirate (šifra karte):")
    if sifra in sifre:                                                         #ukoliko sifra karte postoji
        if karte[sifra]["broj_pasosa"]=="":                                    #ukoliko putnik nije napisao sve informacije
            print("Unesite ostale informacije za putnika")
            pasos = input("broj pasoša:")
            while pasos=="":
                pasos=input("broj pasoša:")
                print("Greška! Unesite ponovo")
            drzavljanstvo=input("državljanstvo:")
            while drzavljanstvo=="":
                drzavljanstvo=input("državljanstvo:")
                print("Greška! Unesite ponovo")
            telefon=input("broj telefona:")
            while telefon=="":
                telefon=input("broj telefona:")
                print("Greška! Unesite ponovo")
            email=input("email:")
            while email=="":
                email=input("email:")
                print("Greška! Unesite ponovo")
            pol=input("pol:")
            while pol=="":
                pol=input("pol:")
                print("Greška! Unesite ponovo")
            karte[sifra]["broj_pasosa"]=pasos
            karte[sifra]["drzavljanstvo"] = drzavljanstvo
            karte[sifra]["telefon"] = telefon
            karte[sifra]["email"] = email
            karte[sifra]["pol"] = pol
        print("Prikaz sedišta:")
        sifra_leta=karte[sifra]["sifra_leta"]
        broj_redova=modeli_aviona[letovi[konkretni_letovi[sifra_leta]["broj_leta"]]["model"]]["broj_redova"]                 #uzimanje broja redova konkretnog leta
        broj_redova=eval(broj_redova)
        pozicija_sedista=modeli_aviona[letovi[konkretni_letovi[sifra_leta]["broj_leta"]]["model"]]["pozicija_sedista"]       #i pozicije sedista
        for i in range(1,broj_redova+1):                                                                                #ispis redova i broja sedista
            print("Red ",i,": ",end='')
            string=pozicija_sedista
            for karta in karte.values():
                if karta["sifra_leta"]==sifra_leta and karta["sediste"]!="ne":                                      #provera koja mesta su vec zauzeta
                    kom=karta["sediste"].split('-')
                    if i==eval(kom[0]):
                        string=string.replace(kom[1],"X")
            print(string)
        while True:
            rez=input("Unesite broj reda i poziciju sedista(Velikim Slovom!) odvojeno znakom - (npr. 10-B):")               #Čekiranje broja reda i sedista
            t=True
            if "-" in rez:
                spl=rez.split("-")
                for karta in karte.values():                                                                                #provera da li je to mesto vec rezervisano
                    if rez in karta["sediste"]:
                        print("Greška to mesto je već zauzeto")
                        t = False
                if eval(spl[0])<0 or eval(spl[0])>broj_redova or spl[1] not in pozicija_sedista:
                    print("Greška niste dobro uneli!!!")

                elif t==True:
                    break
            else:
                print("Greška niste dobro uneli!!!")
        karte[sifra]["sediste"]=rez
        file=open("karte.txt","w",encoding="utf8")                                                                                      #upisivanje čekirane karte u datoteku
        for karta in karte.values():
            string=karta["sifra_karte"]+"|"+karta["kor_ime"]+"|"+karta["ime"]+"|"+karta["prezime"]+"|"+karta["broj_pasosa"]+"|"+karta["drzavljanstvo"]+"|"+karta["telefon"]+"|"+karta["email"]+"|"+karta["pol"]+"|"+karta["sifra_leta"]+"|"+karta["cena"]+"|"+karta["sediste"]+"|"+karta["obrisana"]+"|"+karta["dan_kupovine"]+"\n"
            try:
                file.write(string)
            except:
                print("Greška prilikom čuvanja podataka!")
        file.close()
        print("Podaci Sačuvani.")
    else:
        print("Uneli ste pogrešnu šifru karte ili je ta karta već čekirana!!!")                                         #ukoliko je čekirana karta
