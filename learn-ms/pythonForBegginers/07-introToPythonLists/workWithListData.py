planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

userPlanet = input('Please enter the name of the planet (with a capital letter to start) ')

planetIndex = planets.index(userPlanet)

print('Here ate the planets closer than ' + userPlanet)
print(planets[0:planetIndex])

print('Here are the planets further than ' + userPlanet)
print(planets[planetIndex + 1:])

