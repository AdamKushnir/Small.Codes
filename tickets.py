# Vstupní proměnné
mesta = [
    "Praha", "Viden", "Olomouc",
    "Svitavy", "Zlin", "Ostrava"
]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35
nabidka = \
"""1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

otdelovac = "=" * 40
# Pozdrav a nabídka
Name = input("Hi user, what is ur name? ")
print("WELCOM IN OUR APLICATION DESTINATIO", Name.upper())
print(otdelovac)
print(nabidka)
print(otdelovac)



# Vybrat destinaci, verifikace destinace 
destination = input("CHOISE UR DESTINATION: ")
IntDestination = mesta[int(destination)- 1]
if int(destination) <= 6 and int(destination) >= 1:
    print(IntDestination)
else:
    print("UR DESTINATION IS NOT IN LIST!")
print(otdelovac)

# Ověřit jestli uživatel dostane slevu
if IntDestination in slevy:
    NewPrice = 0.75 * ceny[int(destination) - 1]
    print("U HAVE SALE 25%! PRICE:", NewPrice)

else:
    NewPrice = ceny[int(destination) - 1]

# Ověřit validní jméno a přijmení
LastName = input("LASTNAME: ")
if Name.isalpha() and LastName.isalpha():
    print(f"Cele jmeno:", Name.upper(), LastName.upper())
else:
    print("Ur name or lastname is uncorect! ENDING...")
    quit()

# Ověření validni emailové adresy
email = input("EMAIL: ")

if "@" in email and email.split("@")[1] in domeny:
    print("Email is correct")
else:
    print(cara)
    print("Email is uncorrect! ENDING...")
    quit()
print(otdelovac)

# Rekapitulace objednávky
print("THANK U", Name.upper(), LastName.upper(), "FOR UR ORDER.")
print("UR DESTINATION IS:", IntDestination.upper(), "UR PRICE IS", NewPrice, "€")
print("IN UR EMAIL", email,"WE SEND U MORE INFORMATION")