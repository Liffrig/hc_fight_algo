class Player:
    attack_types_values = {"N": 10, "H":20}

    def __init__(self, attack_stat, stamina):
        self.attack_stat = attack_stat
        self.base_stamina = stamina
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
            print(f"Attack >>> {value} / Stamina >>> {self.stamina}")
            return value
        else:
            self.rest()
            print(f"Resting >>> {self.stamina}")
            return 0

        
    



player1 = Player(11,100)
enemy_health = 110

round_counter = 1

while enemy_health > 0:
    print(f"*** ROUND {round_counter} ***")

    if enemy_health - player1.calculate_attack("N") <= 0:
        enemy_health -= player1.attack("N")
    else:
        enemy_health -= player1.attack("H")

    print(f"Enemy HP >>> {enemy_health}")
    round_counter += 1




        