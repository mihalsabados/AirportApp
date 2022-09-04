def registracija_kupca(korisnici):
    print("=" * 10, "REGISTRACIJA KUPCA", "=" * 10)
    file = open("korisnici.txt", "a+", encoding='utf8')
    kor_ime = input("Unesite korisničko ime:")
    if kor_ime in korisnici:
        print("Greška takvo korisničko ime već postoji!")
        return
    lozinka = input("Unesite lozinku:")
    ime = input("Unesite ime")
    prezime = input("Unesite prezime:")
    broj_pasosa=input("Unesite broj pasosa:")
    drzavljanstvo=input("Unesite drzavljanstvo:")
    telefon=input("Unesite broj telefona:")
    mail=input("Unesite email:")
    pol=input("Unesite pol:")
    uloga = "kupac"
    string = kor_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + uloga  + "|" + broj_pasosa + "|" + drzavljanstvo + "|" + telefon + "|" + mail + "|" + pol+"\n"
    file.write(string)
    file.close()
def registracija_prodavca(korisnici):
    print("=" * 10, "REGISTRACIJA PRODAVCA", "=" * 10)
    file = open("korisnici.txt", "a+", encoding='utf8')
    kor_ime = input("Unesite korisničko ime:")
    if kor_ime in korisnici:
        print("Greška takvo korisničko ime već postoji!")
        return
    lozinka = input("Unesite lozinku:")
    ime = input("Unesite ime")
    prezime = input("Unesite prezime:")
    uloga = "prodavac"
    string = kor_ime + "|" + lozinka + "|" + ime + "|" + prezime + "|" + uloga + "\n"
    file.write(string)
    file.close()