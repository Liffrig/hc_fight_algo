class Player:
    attack_types_values = {"N": 10, "H":20}

    def __init__(self, stamina):
        self.attack_stat = 17
        self.base_stamina = 100
        self.stamina = stamina
    
    def calculate_attack(self,type):
        if type == "N" and self.stamina >= self.attack_types_values["N"]:
            attack =  round((self.attack_stat*(self.stamina*0.02)*1.0),0)

        elif type == "H" and self.stamina >= self.attack_types_values["H"]:
            attack =  round((self.attack_stat*(self.stamina*0.02)*1.5),0)

        else:
            attack = 0

        return attack
    
    def rest(self):
        if self.stamina <= self.base_stamina * 0.9:
            self.stamina += round((self.base_stamina*0.1))
        else:
            self.stamina = self.base_stamina


    def attack(self, type):
        stamina_used = self.attack_types_values[type]
        if self.calculate_attack(type) > 0:
            value = self.calculate_attack(type)
            self.stamina -= stamina_used
            #print(f"Attack >>> {value} / Stamina >>> {self.stamina}")
            return value
        else:
            self.rest()
            #print(f"Resting >>> {self.stamina}")
            return 0

        
class State:
    def __init__(self,path,round, ene_hp, pl_stam) -> None:
        self.path = path
        self.round = round
        self.ene_hp = ene_hp
        self.pl_stam = pl_stam
    def print_all(self):
        print(self.path ,self.round, self.ene_hp, self.pl_stam)