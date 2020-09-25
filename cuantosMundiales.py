edad = int(input("Pone tu edad capo: "))
lista = [ 
    "Russia 2018",
    "Brasil 2014",
    "Sudafrica 2010",
    "Alemania 2006",
    "Corea del Sur 2002",
    "Fracia 1998",
    "Estados Unidos 1994",
    "Italia 1990",
    "Mexico 1986 (Acá Maradona salió campeón del mundo papá)",
    "España 1982",
    "Argentina 1978",
    "Alemania 1974",
    "Mexico 1970",
    "Inglaterra 1966",
    "Chile 1962",
    "Suecia 1958",
    "Suiza 1954",
    "Brasil 1950",
    "Francia 1938",
    "Italia 1934",
    "Uruguay 1930"
        ]
cantidad = edad//4
print(f"viviste {cantidad} de mundiales los cuales fueron en :")
for index, item in enumerate(lista):
    if cantidad-1 >= index:
        print("       " + item)
