class piratas_team_fruta:
    nombre = "frut"
    def __init__(self,nombree):
        self.nombre = nombree
    def correr(self):
        print(self.nombre,"El pirata con fruta corre")
    def saltar(self):
        print(self.nombre,"El pirata con fruta salta")
    def golpear(self):
        print(self.nombre,"El pirata con fruta golpea")
    def volar(self):
        print(self.nombre,"El pirata con fruta vuela")
    def estirarse(self):
        print(self.nombre,"El pirata con fruta se estira ")
    def entrenar(self):
        print(self.nombre,"El pirata con fruta entrena con su fruta")
    def nadar(self):
        print(self.nombre,"El pirata con fruta no puede nadar (posee fruta)")

class piratas_team_espada:
    nombre = "esp"
    def __init__(self,nombree):
        self.nombre = nombree
    def correr(self):
        print(self.nombre,"El pirata espadachin corre")
    def saltar(self):
        print(self.nombre,"El pirata espadachin salta")
    def golpear(self):
        print(self.nombre,"El pirata espadachin golpea")
    def cortar(self):
        print(self.nombre,"El pirata espadachin corta")
    def nadar(self):
        print(self.nombre,"El pirata nada (no posee fruta)")
    def entrenar(self):
        print(self.nombre,"El pirata espadachin entrena con sus espadas")

zoro = piratas_team_espada("zoro")
zoro.cortar()
luffy = piratas_team_fruta("luffy")
luffy.correr()
brook = piratas_team_espada("brook")
brook.golpear()
robin = piratas_team_fruta("robin")
robin.correr()

