
# A slice creates a new list. It doesn't modify the current list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planetsBeforeEarth = planets[0:2] # that will show only two first planets, the index 2 (third planet) will not shown
print(planetsBeforeEarth)

planetsAfterEarth = planets[3:8] # that will show index 4 to index 7
print(planetsAfterEarth)

planetsAfterEarthToTheEnd = planets[3:] # without the second parameter will show to the end
print(planetsAfterEarthToTheEnd)

# The operator '+'(join)  can be used with two lists to return a new list.
# Joining lists creates a new list. It doesn't modify the current list.
amaltheaGroup = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galileanGroup = ['Io', 'Europa', 'Ganymede', 'Callisto']

regularSatelliteMoons = amaltheaGroup + galileanGroup
print('The regular satellite moons of Jupiter are', regularSatelliteMoons)

# Use .sort() to sort an alphabetical/numerical list and .sort(reverse=True) to reverse sort
regularSatelliteMoons.sort()
print('The regular satellite moons of Jupiter are', regularSatelliteMoons)

regularSatelliteMoons.sort(reverse=True)
print('The regular satellite moons of Jupiter are', regularSatelliteMoons)

# Join (+) do not modify the current list and create a new. 
# .sort() modifies the current list.

