class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh


class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def show_info(self):
        print(f"Ism: {self.ism}")
        print(f"Maosh: {self.maosh}")
        print(f"Fan: {self.fan}")


class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def show_info(self):
        print(f"Ism: {self.ism}")
        print(f"Maosh: {self.maosh}")
        print(f"Qavat: {self.qavat}")


oqituvchi = Oqituvchi("Ali", 5000000, "Matematika")
farrosh = Farrosh("Vali", 2500000, 2)

oqituvchi.show_info()
print("==================")
farrosh.show_info()