# EX
chaine = 'J\'aime le Python!'

# EX
chaine2 = "\"Le seul individu formé, c'est celui qui a appris comment apprendre (...)\" (Karl Rogers, 1976)"

# EX
>>> chaine3 = """Ceci est un nouvel
... essai sur plusieurs
... lignes"""
>>>

# EX
variable = variable + 1
variable += 1

# EX
>>> a = 5
>>> b = 32
>>> a,b = b,a
>>> a
32
>>> b
5
>>>

# EX
>>> x = y = 3
>>> x
3
>>> y
3
>>>

# EX
>>> type(3.4)
<class 'float'>
>>> type("un essai")
<class 'str'>
>>>

# EX
>>> print("Hello World !")

# EX
>>> age = 21
>>> if age >= 18:
...    print("Vous êtes majeur.")
... else:
...    print("Vous êtes mineur.")

# EX
>>> if a > 0:
...     print("a est positif.")
... elif a < 0:
...     print("a est négatif.")
... else:
        print("a est nul.")

# EX
if a>=2 and a<=8:
    print("a est dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")

# EX
nb = 7
i = 0
while i < 10:
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1

# EX
chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy":
        print(lettre)
    else:
        print("*")

# EX
while 1:
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break

# EX
i = 1
while i < 20:
    if i % 3 == 0:
        i += 4
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue
    print("La variable i =", i)
    i += 1
