name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

#template = "Gravity Facts about {name}\n--------------------------\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2"
#print(template.format(name=name, planet=planet, gravity=gravity))
# ou

template = f"""Gravity Facts about {name}\n--------------------------\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2"""
print(template)
