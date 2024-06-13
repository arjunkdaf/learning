gravityOnEarth = 1.0
gravityOnTheMoon = 0.166
gravityOnPlanets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

busWeight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weights", busWeight, "N")
print("On Mercury, a double-decker bus weights", busWeight * gravityOnPlanets[0], "N")
print("The lightest a bus would be in the solar system is", busWeight * min(gravityOnPlanets), "N")
print("The heaviest a bus would be in the solar system is", busWeight * max(gravityOnPlanets), "N")

