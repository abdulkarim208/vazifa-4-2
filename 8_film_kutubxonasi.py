class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom

        if filmlar is None:
            self.filmlar = []
        else:
            self.filmlar = filmlar

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, index):
        return self.filmlar[index]

    def __contains__(self, film):
        return film in self.filmlar


kutubxona = FilmKutubxonasi("Mening kinolarim")

kutubxona.filmlar.append("Avatar")
kutubxona.filmlar.append("Titanic")
kutubxona.filmlar.append("Joker")

print("Filmlar soni:", len(kutubxona))
print("Birinchi film:", kutubxona[0])
print("Avatar bormi:", "Avatar" in kutubxona)
print("Batman bormi:", "Batman" in kutubxona)