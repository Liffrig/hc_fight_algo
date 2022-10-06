from player import Player,State
import pandas as pd

atks = ["N","H"]
states_list = []
st0 = State("0-",0,100,100)
states_list.append(st0)
end_count = 0

results = []


while len(states_list) > 0:
    for st in states_list:
        for at in atks:
            player = Player(st.pl_stam)
            new_gen = st.round + 1
            new_ene_hp = st.ene_hp - player.attack(at)
            nw_state = State(st.path + f"{at}-" ,new_gen,new_ene_hp, player.stamina)
            # nw_state.print_all()

            if nw_state.ene_hp <0:
                # print("---ENDS HERE---")
                end_count+=1
                results.append([nw_state.path, new_gen, new_ene_hp, player.stamina])


            if nw_state.ene_hp > 0:
                states_list.append(nw_state)

        states_list.pop(0)
        break
    print(f'States List -> {len(states_list)}')
    print(f'Results -> {len(results)}')

print(f'end_count: {end_count}')
df = pd.DataFrame(results)
df.to_csv("results.csv")











# while enemy_health > 0:



#     print(" ")
#     print(f"*** ROUND {round_counter} ***")


#     if enemy_health - player1.calculate_attack("H") <= 0:
#         enemy_health -= player1.attack("H")
#     else:
#         enemy_health -= player1.attack("N")

#     print(f"Enemy HP >>> {enemy_health}")
#     round_counter += 1




        