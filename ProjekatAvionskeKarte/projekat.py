from izmene import pretraga_prodatih, brisanje, izmena, brisanje_menadzer
from izvestaj import izvestavanje
from kupoprodaja import kupovina, checkin
from letovi import kreiranje_letova, izmena_letova
from polasci import fleksibilni_polasci
import pregled
from pretrage import pretraga
from prikaz import najjeftiniji
from registracije import registracija_prodavca, registracija_kupca
from ucitavanje import iscitaj
import sys

korisnici={}                                            #svi korisnici
letovi={}
konkretni_letovi={}
modeli_aviona={}
aerodromi={}
pr_korisnik={}                                          #trenutno prijavljeni korisnik
def prijava():
    print("="*50)
    while True:
        korisnicko=input("Korisničko ime:")
        sifra=input("Šifra:")
        for user in korisnici.values():
            if user["kor_ime"]==korisnicko and user["lozinka"]==sifra:
                print("Uspešno prijavljivanje.")
                pr_korisnik["kor_ime"]=korisnicko
                pr_korisnik["sifra"]=sifra
                pr_korisnik["uloga"]=user["uloga"]
                meni(user["uloga"])
                break
        else:
            print("Uneto korisničko ime ili šifra ne postoji!!\nPokušajte ponovo")
def meni_kupac():
    print("="*10,"Dodatni meni za kupca","="*10)
    print("1-Kupovina karata")
    print("2-Pregled nerealizovanih karata")
    print("3-Prijava na let(Čekiranje)")
    print("x-nazad")
    menik={
        "1" : kupovina,
        "2" : pregled.pregled_nerealizovanih_karata,
        "3" : checkin,
        "x" : meni
    }
    s=input("Unesite opciju:")
    while True:
        if s in menik:
            if s=="x":
                menik[s]("kupac")
            else:
                menik[s](korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,pr_korisnik)
                meni_kupac()
        else:
            print("Odabrali ste nepostojeću opciju!")
def meni_prodavac():
    print("="*10,"Dodatni meni za prodavca","="*10)
    print("1-prodaja karata")
    print("2-Prijava na let(Čekiranje)")
    print("3-Izmena karata")
    print("4-brisanje karata")
    print("5-pretraga prodatih")
    print("x-nazad")
    menik = {
        "1": kupovina,
        "2": checkin,
        "3": izmena,
        "4": brisanje,
        "5": pretraga_prodatih,
        "x": meni
    }
    s = input("Unesite opciju:")
    while True:
        if s in menik:
            if s == "x":
                menik[s]("prodavac")
            else:
                menik[s](korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,pr_korisnik)
                meni_prodavac()
        else:
            print("Odabrali ste nepostojeću opciju!")
def meni_menadzer():
    print("="*10,"Dodatni meni za menadžera","="*10)
    print("1-pretraga prodatih")
    print("2-registracija prodavca")
    print("3-kreiraj let")
    print("4-izmeni let")
    print("5-brisanje karata")
    print("6-izveštaj")
    print("x-nazad")
    menik = {
        "1": pretraga_prodatih,
        "2": registracija_prodavca,
        "3": kreiranje_letova,
        "4":izmena_letova,
        "5": brisanje_menadzer,
        "6": izvestavanje,
        "x": meni
    }
    s = input("Unesite opciju:")
    while True:
        if s in menik:
            if s == "x":
                menik[s]("menadzer")
            elif s=="2":
                menik[s](korisnici)
                iscitaj(korisnici, letovi, konkretni_letovi, modeli_aviona, aerodromi)
                meni_menadzer()
            else:
                menik[s](korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi,pr_korisnik)
                meni_menadzer()
        else:
            print("Odabrali ste nepostojeću opciju!")
def meni(uloga):
    print("="*10,"MENI","="*10)
    print("1-prijava")
    print("2-pregled letova")
    print("3-pretraga")
    print("4-prikaz 10 najjeftinijih letova")
    print("5-fleksibilni polasci")
    print("x-izlazak")
    meni_dict={
        "1":prijava,
        "2":pregled.pregled_letova,
        "3":pretraga,
        "4":najjeftiniji,
        "5":fleksibilni_polasci
        }
    if uloga=="nista":
        print("6-registracija")
        meni_dict["6"]=registracija_kupca
    if uloga=="kupac":
        print("6-Dodatni meni")
        meni_dict["6"]=meni_kupac
    if uloga=="prodavac":
        print("6-Dodatni meni")
        meni_dict["6"]=meni_prodavac
    if uloga=="menadzer":
        print("6-Dodatni meni")
        meni_dict["6"]=meni_menadzer
    while True:
        s=input("Unesite opciju:")
        if s in meni_dict:
            if s=="1":
                meni_dict[s]()
            elif s=="6" and uloga!="nista":
                meni_dict[s]()
                iscitaj(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi)
                meni(uloga)
            elif s=="6" and uloga=="nista":
                meni_dict[s](korisnici)
                iscitaj(korisnici, letovi, konkretni_letovi, modeli_aviona, aerodromi)
                meni(uloga)
            else:
                meni_dict[s](korisnici, letovi, konkretni_letovi, modeli_aviona, aerodromi)
                meni(uloga)
        elif s=="x":
            sys.exit(1)
            break
        else:
            print("Odabrali ste nepostojeću opciju!!")
def main():
    iscitaj(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi)
    meni("nista")
if __name__=="__main__":
    main()

