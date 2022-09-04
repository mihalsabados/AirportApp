def iscitaj(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi):
    file=open("Korisnici.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts=line.split("|")
        parts[-1] = parts[-1].replace("\n", "")
        if parts[4]=="kupac":
            korisnik={"kor_ime":parts[0],"lozinka":parts[1],"ime":parts[2],"prezime":parts[3],"uloga":parts[4],"broj_pasoša":parts[5],"državljanstvo":parts[6],"telefon":parts[7],"email":parts[8],"pol":parts[9]}
        else:
            korisnik = {"kor_ime": parts[0], "lozinka": parts[1], "ime": parts[2], "prezime": parts[3],"uloga": parts[4]}
        korisnici[parts[0]]=korisnik
    file.close()

    file=open("avionski_letovi.txt","r",encoding="utf8")
    lines =file.readlines()
    for line in lines:
        parts=line.split("|")
        parts[-1] = parts[-1].replace("\n", "")
        let={"broj_leta":parts[0],"polaziste":parts[1],"odrediste":parts[2],"poletanje":parts[3],"sletanje":parts[4],"ssdana":parts[5],"prevoznik":parts[6],"dani":parts[7],"model":parts[8],"cena":parts[9]}
        letovi[parts[0]]=let
    file.close()

    file=open("konkretni_letovi.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts=line.split("|")
        parts[-1] = parts[-1].replace("\n", "")
        konlet={"sifra":parts[0],"broj_leta":parts[1],"datum_polaska":parts[2],"datum_dolaska":parts[3]}
        konkretni_letovi[parts[0]]=konlet
    file.close()

    file = open("modeli_aviona.txt", "r",encoding="utf8")
    lines = file.readlines()
    for line in lines:
        parts = line.split("|")
        parts[-1] = parts[-1].replace("\n", "")
        model = {"naziv": parts[0], "broj_redova": parts[1], "pozicija_sedista": parts[2]}
        modeli_aviona[parts[0]]=model
    file.close()

    file = open("aerodromi.txt", "r",encoding="utf8")
    lines = file.readlines()
    for line in lines:
        parts = line.split("|")
        parts[-1]=parts[-1].replace("\n","")
        aerodrom = {"skracenica": parts[0], "naziv": parts[1], "grad": parts[2],"drzava":parts[3]}
        aerodromi[parts[0]] = aerodrom
    file.close()