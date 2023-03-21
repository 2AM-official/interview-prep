# Pokémon CLI
A simple command-line interface (CLI) application that uses the RESTful Pokémon API to lookup Pokémon by name or number, and display the top 10 most common moves that begin with the letter 's' for the first 100 Pokémon.

## Features
Lookup Pokémon by name
Lookup Pokémon by number
Display the top 10 most common 's' moves for the first 100 Pokémon
## Dependencies
Python 3.6+ \
requests library
## Installation
Make sure you have Python 3.6 or higher installed on your system.
Install the requests library using the following command:
```
pip install requests
```
## Usage
To run the script, simply execute the following command in your terminal or command prompt:
```
python pokemon.py
```
You will be presented with a menu of options:
```
Options:
1. Lookup Pokemon by name
2. Lookup Pokemon by number
3. Top 10 most common moves for the first 100 Pokemon start with letter 's'
3. Exit
```
Enter your choice (1-4) and follow the prompts. The script will display the relevant information based on your input.
## Design Overview
1. **API Endpoint Analysis:** Upon analyzing the Pokémon API's base URL ('https://pokeapi.co/api/v2/pokemon/'), it was determined that the API allows searching for Pokémon by their ID number or lowercase name by appending the relevant query to the base URL.
2. **CLI Class Construction:** A PokemonCLI class was created to facilitate interaction with the Pokémon API.
3. **Lookup Functions:** Two functions, lookup_by_name and lookup_by_number, were implemented to return the sorted moves (in alphabetical order) for a given Pokémon based on its name or number. Error handling was added to account for cases where a Pokémon is not found, returning an error message. Upon retrieving the Pokémon data, a for loop was used to extract and sort the move names.
4. **Top Moves Function:** The get_top_moves function was created to find the top 10 most common moves (starting with a specified letter) for the first 100 Pokémon. A dictionary was used to count the occurrences of each move, and the lookup_by_number function was employed to obtain the moves for the first 100 Pokémon. After counting all moves, a heapq data structure was utilized to efficiently sort the dictionary and retrieve the top 10 most common moves. To enhance flexibility, the number of Pokémon to search and the initial letter for moves can be specified as input parameters with default values of 100 and 's', allowing users to customize the search criteria.
5. **CLI Implementation:** With the core functions in place, the CLI was developed to provide users with a menu-driven interface. Prompts are displayed for users to select from four options, including the three functions specified in the project requirements and an exit option. Error handling was incorporated to provide feedback to users when invalid input is entered.