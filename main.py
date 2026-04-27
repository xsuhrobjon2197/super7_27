#8-m
class Sportchi:
    def __init__(self, ism):
        self.ism = ism

    def oyin(self):
        print("O'ynayapti")


class Futbolchi(Sportchi):
    def oyin(self):
        super().oyin()
        print("Futbol O'ynayapti")

u1 = Sportchi("Rahmatjon")
u1.oyin()
