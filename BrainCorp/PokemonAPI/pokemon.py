import requests
import sys
import collections
import heapq

class PokemonCLI:
    def __init__(self):
        # Set the base URL for the Pokémon API
        self.base_url = 'https://pokeapi.co/api/v2/pokemon/'

    def lookup_by_name(self, name: str):
        """Return the sorted moves from the searching name Pokémon of the Pokémon API."""
        # Build the API URL using the Pokémon name
        api = f"{self.base_url}{name.lower()}"
        # Send a request to the API
        response = requests.get(api)
        # Check if the response is successful
        if response.status_code != 200:
            print("Error: Pokémon not found.")
            return []
        # Parse the JSON data
        data = response.json()
        # Extract and sort the moves for the Pokémon
        moves = [move['move']['name'] for move in data['moves']]
        return sorted(moves)
    
    def lookup_by_number(self, number: int):
        """Return the sorted moves from the searching number Pokémon of the Pokémon API."""
        # Build the API URL using the Pokémon number
        api = f"{self.base_url}{number}"
        # Send a request to the API
        response = requests.get(api)
        # Check if the response is successful
        if response.status_code != 200:
            print("Error: Pokémon not found.")
            return []
        # Parse the JSON data
        data = response.json()
        # Extract and sort the moves for the Pokémon
        moves = [move['move']['name'] for move in data['moves']]
        return sorted(moves)

    def get_top_moves(self, limit: int = 100, letter: str = 's') -> list:
        """Return the top 10 moves from the first 100 Pokémon of the Pokémon API."""
        # Initialize a defaultdict to store move counts
        move_counts = collections.defaultdict(int)
        # Iterate through the Pokémon IDs from 1 to limit
        for i in range(1, limit+1):
            # Get the moves for the Pokémon by ID
            moves = self.lookup_by_number(i)
            # Increment the move count for each move that starts with the specified letter
            for move in moves:
                if move.startswith(letter.lower()):
                    move_counts[move] += 1
        # Create a min heap of the top 10 most common moves
        min_heap = heapq.nsmallest(10, move_counts.items(), key=lambda x: -x[1])
        return min_heap



def main():
    # Instantiate the Pokémon CLI class
    cli = PokemonCLI()
    
    # Main loop for user interaction
    while True:
        # Display the menu options
        print("\nOptions:")
        print("1. Lookup Pokémon by name")
        print("2. Lookup Pokémon by number")
        print("3. Top 10 most common 's' moves for the first 100 Pokémon")
        print("4. Exit")
        
        # Receive user's choice
        choice = input("Enter your choice (1-4): ")

        # Execute the appropriate action based on the user's choice
        if choice == '1':
            # Receive Pokémon name input
            name = input("Enter Pokémon name: ")
            # Get the moves for the entered Pokémon name
            moves = cli.lookup_by_name(name)
            if moves:
                # Display the moves for the entered Pokémon name
                print(f"Moves for {name}:")
                print(", ".join(moves))
        elif choice == '2':
            # Receive Pokémon number input
            number = input("Enter Pokémon number: ")
            try:
                # Convert input to integer
                num = int(number)
                # Get the moves for the entered Pokémon number
                moves = cli.lookup_by_number(num)
                if moves:
                    # Display the moves for the entered Pokémon number
                    print(f"Moves for Pokémon #{num}:")
                    print(", ".join(moves))
            except ValueError:
                # Display an error message for invalid input
                print("Error: Invalid input. Please enter a valid number.")
        elif choice == '3':
            # Get the top 10 most common 's' moves for the first 100 Pokémon
            top_moves = cli.get_top_moves()
            # Display the top 10 most common 's' moves
            print("\nTop 10 most common 's' moves for the first 100 Pokémon:")
            for move, count in top_moves:
                print(f"{move}: {count}")
        elif choice == '4':
            # Exit the program and display a goodbye message
            print("Thanks for using my Pokémon API! Goodbye!")
            sys.exit()
        else:
            # Display an error message for an invalid choice
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

