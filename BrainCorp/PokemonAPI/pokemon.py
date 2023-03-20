import requests
import json
import collections
import heapq

class pokemon:
    def __init__(self) -> None:
        self.move_counts = collections.defaultdict(int)

    def get_top_moves(self, api):
        for _ in range(5):
            next_link, pokemons_apis = self.pokemons_get(api)
            api = next_link
            for pokemons_api in pokemons_apis:
                self.moves_count(pokemons_api)
        max_heap = []
        for move, count in self.move_counts.items():
            #print(move, count)
            heapq.heappush(max_heap, (count, move))
            if len(max_heap) > 10:
                heapq.heappop(max_heap)
        res = []
        while max_heap:
            count, move = heapq.heappop(max_heap)
            res.append([count, move])
        return res[::-1]

    def pokemons_get(self, api):
        response_API = requests.get(api)
        data = response_API.text
        parse_json = json.loads(data)
        next_link = parse_json['next']
        pokemons_apis = []
        for result in parse_json['results']:
            pokemons_apis.append(result['url'])
        return next_link, pokemons_apis

    def moves_count(self, api):
        response_API = requests.get(api)
        data = response_API.text
        parse_json = json.loads(data)
        for move in parse_json['moves']:
            move_name = move['move']['name']
            self.move_counts[move_name] += 1


search = pokemon()
print(search.get_top_moves('https://pokeapi.co/api/v2/pokemon'))
