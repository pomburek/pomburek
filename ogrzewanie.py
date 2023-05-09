a = float(input("Podaj długość basenU: "))
b = float(input("Podaj szerokość basenU: "))
c = float(input("Podaj głębokość basenU: "))

m = 1000 * a * b * c

temperatura_p = 4
temperatura_k = 22

przyrost_temperatury = temperatura_k - temperatura_p

def ogrzewanie(m, przyrost_temperatury):
    w = m*4200*przyrost_temperatury
    cena = w/3600000
    print("Za ogrzanie tego basenu zapłacisz: ", cena,"zł")

ogrzewanie(m, przyrost_temperatury)