def najjeftiniji(korisnici,letovi,konkretni_letovi,modeli_aviona,aerodromi):
    print("="*10,"PRIKAZ 10 NAJJEFTINIJIH","="*10)
    polaziste=input("Unesite polaziste:")
    odrediste=input("Unesite odredište:")
    lists=[]
    for let in letovi.values():
        for konlet in konkretni_letovi.values():
            aerodrom=aerodromi[let["polaziste"]]
            aerodrom1=aerodromi[let["odrediste"]]
            if polaziste in aerodrom["grad"] and odrediste in aerodrom1["grad"] and let["broj_leta"]==konlet["broj_leta"]:
                lists.append((aerodrom["grad"],aerodrom["drzava"],aerodrom1["grad"],aerodrom1["drzava"],konlet["datum_polaska"],let["poletanje"],konlet["datum_dolaska"],let["sletanje"],let["prevoznik"],let["cena"]))
    for i in range(len(lists)-1):
        for j in range(i+1,len(lists)):
            if int(lists[i][9])>int(lists[j][9]):
                lists[i],lists[j]=lists[j],lists[i]
    if len(lists)>10:
        lenght=10
    else:
        lenght=len(lists)
    if len(lists)==0:
        print("Ne postoje uneti podaci")
    for i in range(lenght):
        print(lists[i][0],"-(",lists[i][1],")-->",lists[i][2],"-(",lists[i][3],") : ",lists[i][4],"-",lists[i][5],"-->",lists[i][6],"-",lists[i][7],"---",lists[i][8],"  ",lists[i][9])
