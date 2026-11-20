class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print("Hayvon ovoz chiqaryapti")


class It(Hayvon):
    def qoriqlash(self):
        print(f"{self.nomi} uyni qoriqlayapti")


class Mushuk(Hayvon):
    def sichqon_tutish(self):
        print(f"{self.nomi} sichqon tutyapti")


it = It("Rex", 3)
mushuk = Mushuk("Mosh", 2)

it.ovoz()
it.qoriqlash()

mushuk.ovoz()
mushuk.sichqon_tutish()