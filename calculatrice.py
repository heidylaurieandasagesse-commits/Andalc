print("========================")
print("         ANDALC")
print("  Ma calculatrice Python")
print("========================")

nombre1 = float(input("Entre le premier nombre : "))
operation = input("Choisis une opération (+, -, *, /) : ")
nombre2 = float(input("Entre le deuxième nombre : "))

if operation == "+":
    resultat = nombre1 + nombre2

elif operation == "-":
    resultat = nombre1 - nombre2

elif operation == "*":
    resultat = nombre1 * nombre2

elif operation == "/":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        resultat = None
        print("Erreur : impossible de diviser par zéro.")

else:
    resultat = None
    print("Erreur : opération inconnue.")

if resultat is not None:
    print("Résultat :", resultat)

print("========================")
print("Merci d'avoir utilisé ANDALC !")
