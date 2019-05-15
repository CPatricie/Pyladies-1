class Hrnec():
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.obsah = []
        self.pocet_pouziti = 0
    
    def __repr__(self):
        obsah_textove = "prázdno"
        if len(self.obsah) > 0:
            obsah_textove = ", ".join(self.obsah)
        return '<{} hrnec, je v něm {}>'.format(
            self.jmeno, obsah_textove)
        
    def vloz(self, co_vlozit):
        self.obsah.append(co_vlozit)
        self.pocet_pouziti += 1
    
    def vyprazdni(self):
        self.obsah.clear()
        self.pocet_pouziti += 1
    
    def uvar(self):
        for i in range(len(self.obsah)):
          self.obsah[i] = "uvařená " + self.obsah[i]
        self.pocet_pouziti += 1
    
    def slij(self, druhy):
        for polozka in druhy.obsah:
            self.obsah.append(polozka)
        druhy.obsah.clear()
        self.pocet_pouziti += 1
    
    def kolikrat_pouzit(self):
        return self.pocet_pouziti


cerveny_hrnec = Hrnec("červený")
malovany_hrnec = Hrnec("malovaný")
deravy_hrnec = Hrnec("děravý")

cerveny_hrnec.vloz("voda")
cerveny_hrnec.vloz("mrkev")
cerveny_hrnec.vloz("cibule")
cerveny_hrnec.vloz("žába")

malovany_hrnec.vloz("voda")
malovany_hrnec.vloz("sekyrka")

print(cerveny_hrnec)
print(malovany_hrnec)
print(deravy_hrnec)

print(cerveny_hrnec.uvar())
#print(cerveny_hrnec)
