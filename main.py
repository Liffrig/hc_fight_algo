from ast import While
from operator import indexOf


class Player:
    attack_types_values = {"N": 10, "H":20}

    def __init__(self, stamina):
        self.attack_stat = 11
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
            print(f"Attack >>> {value} / Stamina >>> {self.stamina}")
            return value
        else:
            self.rest()
            print(f"Resting >>> {self.stamina}")
            return 0

        
class State:
    def __init__(self,path,round, ene_hp, pl_stam) -> None:
        self.path = path
        self.round = round
        self.ene_hp = ene_hp
        self.pl_stam = pl_stam
    def print_all(self):
        print(self.path ,self.round, self.ene_hp, self.pl_stam)








atks = ["N","H"]
states_list = []
st0 = State("0-",0,110,100)
states_list.append(st0)

def remove_done(gen):
    for i in reversed(states_list):
        if i.ene_hp < 0 or i.round < gen:
            inx = indexOf(states_list,i)
            states_list.pop(inx)

current_generation = -1

while len(states_list) > 0:
    for st in states_list:
        for at in atks:
            player = Player(st.pl_stam)
            new_gen = st.round + 1
            new_ene_hp = st.ene_hp - player.attack(at)
            nw_state = State(st.path + f"{at}-" ,new_gen,new_ene_hp, player.stamina)
            nw_state.print_all()

            if nw_state.ene_hp <0:
                print("---ENDS HERE---")


            if nw_state.ene_hp > 0:
                states_list.append(nw_state)
    
        current_generation +=1
        remove_done(current_generation)















# while enemy_health > 0:



#     print(" ")
#     print(f"*** ROUND {round_counter} ***")


#     if enemy_health - player1.calculate_attack("H") <= 0:
#         enemy_health -= player1.attack("H")
#     else:
#         enemy_health -= player1.attack("N")

#     print(f"Enemy HP >>> {enemy_health}")
#     round_counter += 1




        