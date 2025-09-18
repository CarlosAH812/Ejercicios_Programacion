import json

file_name = "pokemon.json"

with open(file_name, "r", encoding="utf-8") as f:
    pokemons = json.load(f)

print("\n=== Add a New Pokémon ===")
name = input("Name (in English): ")
types = input("Type(s): ").split(",")

types = [t.strip() for t in types]

print("\n=== Base Stats ===")
hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp. Attack: "))
sp_defense = int(input("Sp. Defense: "))
speed = int(input("Speed: "))

new_pokemon = {
    "name": {"english": name},
    "type": types,
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}

pokemons.append(new_pokemon)

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(pokemons, f, indent=2, ensure_ascii=False)

print(f"\n {name} has been successfully added to '{file_name}'")

print("\n Current Pokémon list in the file:\n")
for p in pokemons:
    print(f" {p['name']['english']} ({', '.join(p['type'])})")
    for stat, value in p["base"].items():
        print(f"   {stat}: {value}")
    print()  