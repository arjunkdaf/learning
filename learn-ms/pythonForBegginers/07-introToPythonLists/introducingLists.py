planets = ["Mercury", "Venus", "Earth", "Mars", 
           "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

#redefining lists values

planets[3] = "Red planet"
print("Mars is also known as", planets[3])

planets.append("Pluto") # .append(value) adiciona um valor ao final 

numberOfPlanets = len(planets)
print("There are actually", numberOfPlanets, "planets in the solar system.")

planets.pop() # .pop() remove the last value on list
numberOfPlanets = len(planets)
print("No, there are definitely", numberOfPlanets, "planets in the solar system")

# using negative index
# -1 is the last item in list
# -2 is the last item but one...

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# locate items using index

jupiterIndex = planets.index("Jupiter")
print("Jupiter is the", jupiterIndex +1, "planet from the sun")

# with [0] being the first item we need to add number to see the correct number

mercuryIndex = planets.index("Mercury")
print("Mercury is the", mercuryIndex + 1, "planet from the sun")

