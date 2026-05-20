import math



def orbital_period():

    G = 6.6743e-11 #Gravitational Constat
    M = 1.989e30 #Mass of the Sun
    
    while True:
        planet = input("Please select a planet from our solar system to calculate its orbital period. Type 'Exit' to quit: ").lower()
        if planet == "earth":
            a = 1.496e11
        elif planet == "mercury":
            a = 5.791e10
        elif planet == "venus":
            a = 1.082e11
        elif planet == "mars":
            a = 2.279e11
        elif planet == "jupiter":
            a = 7.786e11
        elif planet == "saturn":
            a = 1.427e12
        elif planet == "uranus":
            a = 2.873e12
        elif planet == "neptune":
            a = 4.495e12
        elif planet == "pluto":
            a = 5.906e12
        elif planet == "exit":
            break
        else:
            print("That was not a valid input, please try again.")
            continue
        print(str(round(((2 * math.pi * math.sqrt(a ** 3/(G * M)))/86400), 2)) + " days")

orbital_period()