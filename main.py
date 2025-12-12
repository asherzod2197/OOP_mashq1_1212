# 1
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def malumot(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"

talaba1 = Talaba("Ali", 20)
print(talaba1.malumot())



# 2
class Avtomobil:
    def __init__(self, brend, model, yil):
        self.brend = brend
        self.model = model
        self.yil = yil
        self.km = 0

    def yurish(self, masofa):
        self.km += masofa
        return f"{self.brend} {masofa} km yurdi."

    def holat(self):
        return f"{self.brend} {self.model}, {self.yil}-yil, {self.km} km yurgan"

avto1 = Avtomobil("Toyota", "Camry", 2020)
print(avto1.holat())

print(avto1.yurish(100))
print(avto1.holat())
