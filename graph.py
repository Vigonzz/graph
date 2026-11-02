# Violet Gonzalez
# Module 4:

from collections import deque

# Task 1:
class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.neighbors = []

    def add_neighbor(self, city):
        """ Adds neighbors to the list """

        # Check to see if the city is already inside the lists, add if it isnt 
        if city not in self.neighbors:
            self.neighbors.append(city)
    
    def __repr__(self):
        """ Helps with printing the neighbor list"""
        return f"{self.name} : {self.population}"
    
# Task 2:
def build_graph(population_file, road_file):
    # Creating a dictionary that will eventually hold the city, and city object
    city_by_name = {}

    # Open the population file and loop through it
    with open(population_file, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # split the lines and ensure to change the pop to a int
            city_name, population = line.split(":", 1)
            city_name = city_name.strip()
            population = int(population.strip())

            # Skip the duplicate names (The file actually holds some duplicates but the assignment ask
            # for an assumption of a unique name)
            if city_name in city_by_name:
                continue

            # Create the city and store it
            new_city = City(city_name, population)
            city_by_name[city_name] = new_city

    # Open the road file
    with open(road_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
             # split the lines into the two connected names
            city_a, city_b = line.split(":", 1)
            city_a = city_a.strip()
            city_b = city_b.strip()

            # Look up the city objects
            first_city = city_by_name[city_a] 
            second_city = city_by_name[city_b] 

            first_city.add_neighbor(second_city)
            second_city.add_neighbor(first_city)

    #  Return the list:
    return list(city_by_name.values())


cities = build_graph("city_population.txt", "road_network.txt")
print(len(cities))
for city in cities:
    if city.name == "Irvine":
        print(city.neighbors)


for city in cities:
    if city.name == "Long Beach":
        print(city.neighbors)


def _get_island_cities(start_city, visited):
    """ Helper function to collect the found cities """
    queue = deque([start_city])

    # Add city to visited so we dont count it twice
    visited.add(start_city)

    # Collect the island cities
    island_cities = []
    while queue: 
        # Take the next city
        current = queue.popleft()
        island_cities.append(current)

        for neighbor in current.neighbors:
            # Check for unvisited neighbors
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return island_cities
        
# Task 3 Island counter
def count_islands(cities):
    visited = set()
    counter = 0

    # Loop through every city
    for city in cities:
        # Start a new island when a city hasnt been visited 
        if city not in visited:
            counter += 1
            _get_island_cities(city, visited)
    return counter

print(count_islands(cities))

# Task 4:

def island_populations(cities):
    # Keep the helpers result and add its population to find the island population
    visited = set()
    island_total_pop = []

    # Loop through every city
    for city in cities:
        # Start a new island when a city hasnt been visited 
        if city not in visited:
            island = _get_island_cities(city, visited)
            total = 0
            # Get the island and total it together
            for island_city in island:
                total += island_city.population
            island_total_pop.append(total)
    return island_total_pop

print(island_populations(cities))

# Task 5: Min highway between two cities

def min_highway(start, end):
    # Check to see if it is the same city
    if start == end:
        return 0

    visited = set()
    visited.add(start)

    # queue the distance 
    queue = deque([(start, 0)])
    while queue:
        current, distance = queue.popleft()
    
    # Check each neighbor
        for neighbor in current.neighbors:
            if neighbor == end:
                return distance + 1
            elif neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    # Only occurs when the cities are on different islands
    return -1

# Find city
def _find_city(island_cities, name):
    for city in island_cities:
        if city.name == name:
            return city
    return None

# Testing min_highway
irvine = _find_city(cities, "Irvine")

to_irvine = _find_city(cities, "Irvine")
to_lb = _find_city(cities, "Long Beach")
to_albany = _find_city(cities, "Albany")
to_gg = _find_city(cities, "Garden Grove")
to_ny = _find_city(cities, "New York")

print(min_highway(irvine, to_irvine))
print(min_highway(irvine, to_lb))
print(min_highway(irvine, to_albany))
print(min_highway(irvine, to_gg))
print(min_highway(irvine, to_ny))
