# Violet Gonzalez
# Module 4:

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

build_graph("city_population.txt", "road_network.txt")
