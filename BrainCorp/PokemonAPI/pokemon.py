import requests
import json
import collections
import heapq

class pokemonCLI:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/pokemon/'
        self.move_counts = collections.defaultdict(int)

    def lookup_by_name(self, name: str):
        api = f"{self.base_url}{name.lower()}"
        response = requests.get(api)
        if response.status_code != 200:
            print("Error: Pokémon not found.")
            return []
        data = response.json()
        moves = [move['move']['name'] for move in data['moves']]
        return sorted(moves)
    
    def lookup_by_number(self, number: int):
        api = f"{self.base_url}{number}"
        response = requests.get(api)
        if response.status_code != 200:
            print("Error: Pokémon not found.")
            return []
        data = response.json()
        moves = [move['move']['name'] for move in data['moves']]
        return sorted(moves)

    def get_top_moves(self) -> list:
        """Return the top 10 moves from the first 5 pages of the Pokémon API."""
        for i in range(1, 101):
            moves = self.lookup_by_number(i)
            for move in moves:
                self.move_counts[move] += 1
        min_heap = heapq.nsmallest(10, self.move_counts.items(), key=lambda x: -x[1])
        return min_heap




search = pokemonCLI()
print(search.get_top_moves())
print(search.lookup_by_name('pikachu'))
print(search.lookup_by_number(1))

