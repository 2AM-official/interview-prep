import requests
import json
import sys
import collections
import heapq

class PokemonCLI:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/pokemon/'

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

    def get_top_moves(self, limit: int = 100, letter: str = 's') -> list:
        """Return the top 10 moves from the first 5 pages of the Pokémon API."""
        move_counts = collections.defaultdict(int)
        for i in range(1, limit+1):
            moves = self.lookup_by_number(i)
            for move in moves:
                if move.startswith(letter.lower()):
                    move_counts[move] += 1
        min_heap = heapq.nsmallest(10, move_counts.items(), key=lambda x: -x[1])
        return min_heap



def main():
    cli = PokemonCLI()
    while True:
        print("\nOptions:")
        print("1. Lookup Pokémon by name")
        print("2. Lookup Pokémon by number")
        print("3. Top 10 most common 's' moves for the first 100 Pokémon")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter Pokémon name: ")
            moves = cli.lookup_by_name(name)
            if moves:
                print(f"Moves for {name.capitalize()}:")
                print(", ".join(moves))
        elif choice == '2':
            number = input("Enter Pokémon number: ")
            try:
                num = int(number)
                moves = cli.lookup_by_number(num)
                if moves:
                    print(f"Moves for Pokémon #{num}:")
                    print(", ".join(moves))
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
        elif choice == '3':
            top_moves = cli.get_top_moves()
            print("\nTop 10 most common 's' moves for the first 100 Pokémon:")
            for move, count in top_moves:
                print(f"{move}: {count}")
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

