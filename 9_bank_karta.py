class Karta:
    def __init__(self, egasi, raqam_oxiri, balans):
        self.egasi = egasi
        self.raqam_oxiri = raqam_oxiri
        self.balans = balans

    def __str__(self):
        return f"Egasi: {self.egasi}, Balans: {self.balans}"

    def __gt__(self, other):
        return self.balans > other.balans

    def __lt__(self, other):
        return self.balans < other.balans


karta1 = Karta("Ali", "1234", 500000)
karta2 = Karta("Vali", "5678", 800000)

print(karta1)
print(karta2)

if karta1 > karta2:
    print("Ali kartasida mablag kop")
else:
    print("Vali kartasida mablag kop")