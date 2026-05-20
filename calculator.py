import math



def orbital_period():
    G = 6.6743e-11 #Gravitational Constat
    M = 1.989e30 #Mass of the Sun

    planet = input("Please select a planet from our solar system to calculate its orbital period: ")

    if planet == "Earth":
        a = 1.496e11

    print(str(round(((2 * math.pi * math.sqrt(a ** 3/(G * M)))/86400), 2)) + " days")

orbital_period()