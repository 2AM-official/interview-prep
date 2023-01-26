import collections
import heapq
flights = [[0,1,15],[0,2,20],[1,3,10],[2,3,20],[2,4,20],[0,5,30],[5,6,5],[3,6,30]]

class Flights():
    def __init__(self, flights):
        self.flights = flights
        self.location = collections.defaultdict(list)
        for flight in flights:
            self.location[flight[0]].append([flight[1], flight[2]])
    
    def check_direct(self, start, end):
        for nxt_location in self.location[start]:
            if nxt_location[0] == end:
                return True
        return False
    
    def check_way(self, start, end):
        #print(self.location)
        if start == end:
            return True
        visited = set()
        visited.add(start)
        
        def dfs(loc):
            returnVal = False
            if loc == end:
                return True
            for nxt_loc in self.location[loc]:
                if nxt_loc[0] in visited:
                    continue
                visited.add(nxt_loc[0])
                returnVal |= dfs(nxt_loc[0])
            return returnVal
        return True if dfs(start) else False
    
    def cheapest_flight(self, start, end):
        # use dijkstra
        print(self.location)
        minHeap = [(0, start)]
        visited = set()
        while minHeap:
            print(minHeap)
            price, dsc = heapq.heappop(minHeap)
            if dsc == end:
                return price
            if dsc in visited:
                continue
            for nxt_loc in self.location[dsc]:
                if nxt_loc[0] in visited:
                    continue
                heapq.heappush(minHeap, (price+nxt_loc[1], nxt_loc[0]))
        return -1
    
def assert_flights_could_reach(test_case_name, actual, expected):
    assert actual == expected, "Test case {}: Expecting: {}, but got: {}".format(test_case_name, expected, actual)

def assert_fligths_prices(test_case_name, actual, expected):
    assert actual == expected, "Test case {}: Expecting: {}, but got: {}".format(test_case_name, expected, actual)


schedual = Flights(flights)
assert_flights_could_reach("0 to 1", schedual.check_direct(0, 1), True)
assert_flights_could_reach("0 to 4", schedual.check_direct(0, 4), False)
print("check direct successed")
assert_flights_could_reach("0 to 4", schedual.check_way(0, 4), True)
assert_flights_could_reach("1 to 4", schedual.check_way(1, 4), False)
print("check could reach successed")
assert_fligths_prices("0 to 3", schedual.cheapest_flight(0, 3), 25)
assert_fligths_prices("0 to 6", schedual.cheapest_flight(0, 6), 35)
print("check price successed!")

