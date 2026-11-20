class Shakl:
    def yuza(self):
        pass


class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon * self.tomon


class TogriTortburchak(Shakl):
    def __init__(self, uzunlik, eni):
        self.uzunlik = uzunlik
        self.eni = eni

    def yuza(self):
        return self.uzunlik * self.eni


kvadrat = Kvadrat(5)
tortburchak = TogriTortburchak(6, 4)

shakllar = [kvadrat, tortburchak]

for shakl in shakllar:
    print(shakl.yuza())