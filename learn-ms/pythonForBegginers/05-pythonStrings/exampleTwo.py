# usando o %s para uma variavel na string, que será informada na sequência
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
# sendo mais de uma a formatação precisa ser alterada
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# também pode ser feito com {} e .format() (preferível)
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
# no caso de mais de uma variável
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

# atribuindo variaveis para melhorar e legibilidade ao invés de usar {0} e {1}
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

# cadeia de caracteres com f e {}
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
# são menos detalhadas mas podem usar funções dentro de {}
# print(round(100/6, 1)) teria como saída 16.7
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

# também pode ser usado para .title(), .upper(), .lower(), etc.
# ainda não vi sentido nisso, já que removendo f"" do heading teria o mesmo resultado, mas ok
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)



