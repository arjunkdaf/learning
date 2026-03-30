# separar a string em linhas com \n
multiline = "Facts about the Moon:\nThere is no atmosphere.\nThere is no sound."

# deixar as iniciais das palavras maiúsculas usando .title()
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# separar em todos os espaços com .split()
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

# separar somente no indicado com \n com .split()
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures .split('\n')
print(temperatures_list)

# buscando uma palavra em uma string com in
print("Moon" in "This text will describe facts and challenges with space travel") # False
print("Moon" in "This text will describe facts about the Moon") # True

# localizar a posição de uma palavra com .find()
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon")) # retornará -1 pois não encontrou

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars")) # retornará 64 que é a posição na cadeia de caracteres

# contando o total de ocorrências de uma palavra com .count()
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon")) # lembrando que Moon != moon

# minúsculo e maiúsculo em todo o texto para facilitar buscas e contagens
moon = "The Moon And The Earth"
print(moon.lower())
print(moon.upper())

# extraindo a informação da temperatura de um texto regular
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':') # separará a string no caractere :
print(parts)
print(parts[-1]) # imprimirá o último elemento da array

# buscando por um item da array com .isnumeric() e, sendo numérico, será impresso
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric(): # um número negativo não retornaria pois - não é número
        print(item) # poderia ser .isdecimal() para números decimais

# .startswitch() e .endswitch()
print("-60".startswith('-')) # retornará True pois começa com -
if "30 C".endswith("C"): # imprimirá a string abaixo pois termina com C
    print("This temperature is in Celsius")

# utilizando .replace() para substituir termos
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

# normalizando o texto antes de buscar
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text) # False
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower()) # True

# juntar uma string dividida em uma array novamente para um string com .join()
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts)) # usando ' ' para a string
