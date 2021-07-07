from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon_info):

        for pokemon_data in self.pokemons:
            if pokemon_info.pokemon_details() == pokemon_data[1]:
                return "This pokemon is already caught"
        self.pokemons.append([pokemon_info.name, pokemon_info.pokemon_details()])
        return f"Caught {pokemon_info.pokemon_details()}"

    def release_pokemon(self, pokemon_info):
        for i in range(len(self.pokemons)):
            if pokemon_info == self.pokemons[i][0]:
                self.pokemons.pop(i)
                return f"You have released {pokemon_info}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemon_string = '\n'.join([f"- {pokemon_data[1]}" for pokemon_data in self.pokemons])
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{pokemon_string}"
