import requests as r # often requests is imported under the alias r

data = r.get("https://pokeapi.co/api/v2/pokemon/20")
print(data.status_code)


    
        # Check Status Code
# if data.status_code == 200:
#     my_data = data.json()
#     for ability in my_data['abilities']:
#         print(ability['result'])
# else:
#     print('Sorry, API call unsuccessful!')

my_data = data.json()

# for x in range(0, 20):
#     print(my_data['results'][x]["name"])


for ability in my_data['abilities']:
    print(ability['ability']['name'])

print("end of ability")
for types in my_data['types']:
    print(types["type"]["name"])
    

print(my_data["species"]["name"])
print(my_data['weight'])



def putPoke(name, weight, abilities, type_of):
    structure = {'name': name, 'weight': weight, 'abilities': abilities, 'type': type_of}
    return structure

p1 = putPoke("bulbasaur",69, "overgrow chlorophyll", "grass poison" )
print(p1)
p2 = putPoke("ivysaur", 130, " overgrow chlorophyll", "grass poison")
print(p2)
p3 = putPoke("venusaur", 100, " overgrow chlorophyll", "grass poison")
print(p3)
p4 = putPoke("charmander", 85, " blaze solar-power", "fire")
print(p4)
p5 = putPoke("charmeleon", 190, " blaze solar-power", "fire")
print(p5)
p6 = putPoke("charizard", 905, " blaze solar-power", "fire flying")
print(p6)
p7 = putPoke("squirtle", 90, " torrent rain-dish", "water")
print(p7)
p8 = putPoke("wartortle", 225, " torrent rain-dish", "water")
print(p8)
p9 = putPoke("blastoise", 855, " torrent rain-dish", "water")
print(p9)
p10 = putPoke("caterpie", 29, "shield-dust run-away", "bug")
print(p10)
p11 = putPoke("metapod", 99, "shed skin", "bug")
print(p11)
p12 = putPoke("butterfree", 320, "compound-eyes tinted-lens", "bug flying")
print(p12)
p13 = putPoke("weedle", 32, "shield-dust run-away", "bug poison")
print(p13)
p14 = putPoke("kakuna", 100, "shed-skin", "bug poison")
print(p14)
p15 = putPoke("beedrill", 295, "swarm sniper", "bug poison")
print(p15)
p16 = putPoke("pidgey", 18, "keen-eye tangled-feet big-pecks", "normal flying")
print(p16)
p17 = putPoke("pidgeotto", 300, "keen-eye tangled-feet big-pecks", "normal flying")
print(p17)
p18 = putPoke("pidget", 395, "keen-eye tangled-feet big-pecks", "normal flying")
print(p18)
p19 = putPoke("rattata", 35, "run-away guts hustle", "normal")
print(p19)
p20 = putPoke("raticate", 185, "run-away guts hustle", "normal")
print(p20)





