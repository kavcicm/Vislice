import model
lojtrice = "#############################\n"

def izpis_zmage(igra):
    tekst = lojtrice + "Uganili ste geslo {0}.\n".format(igra.geslo)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + "Obešeni ste! Pravilno geslo je blio {0}.\n".format(igra.geslo)
    return tekst
def izpis_igre(igra):
    tekst = (lojtrice + 
            igra.pravilni_del_gesla() + "\n" +
            ("Preostalo število poizkusov: {0}\n Napačni ugibi: {1} "
            ).format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
            igra.nepravilni_ugibi()) + lojtrice)
    return tekst

def zahtevaj_vnos():
    return input("Ugibaj črko:  ")

def  pozeni_vmesnik():

    igra = model.nova_igra()

    while True:
        #Izpišemo stanje
        print(izpis_igre(igra))
        #zahtevaj vnos uporabnika
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        # preveri ali smo končali
        if igra.poraz():
            print(izpis_poraza(igra))
            break
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        else:
            pass
    return None

pozeni_vmesnik()