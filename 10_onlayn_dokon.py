class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savat:
    def __init__(self, nom):
        self.nom = nom
        self.mahsulotlar = []

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        jami = 0

        for mahsulot in self.mahsulotlar:
            jami += mahsulot.narx

        return jami

    def __str__(self):
        return f"{self.nom}: {len(self.mahsulotlar)} ta mahsulot"


mahsulot1 = Mahsulot("Telefon", 3000000)
mahsulot2 = Mahsulot("Sichqoncha", 100000)
mahsulot3 = Mahsulot("Klaviatura", 200000)

savat = Savat("Mening savatim")

savat.mahsulotlar.append(mahsulot1)
savat.mahsulotlar.append(mahsulot2)
savat.mahsulotlar.append(mahsulot3)

print(savat)

if savat:
    print("Savat bosh emas")
    print("Umumiy narx:", savat.umumiy_narx())
else:
    print("Savat bosh")