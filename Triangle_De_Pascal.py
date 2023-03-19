from math import factorial

def print_pascal_triangle(n):

    for i in range(n):
        # Boucle pour obtenir les elements de la ligne i
        for j in range(n - i + 1):
            print(end=" ")

        # Boucle pour les espaces
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

        # Affichage
        print()

# test du programme
print_pascal_triangle(9)

