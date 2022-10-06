
import random

n = random.randint(0,100)
appreciation = "?"
nrb = 0
print("devinez le nombre que je pense(indice il est entre 0 et 100)")
while True:
    var = input("quell est votre choice")
    var = int(var)
    if var < n :
        nbr = +1
        appreciation = "non, je pensais a un notre chiffre, il est plus grand:"
        print(appreciation, var)

    else :
        nbr = +1
        appreciation = "non, je pensai a un notre chiffre, il est plus petit:"
        print(appreciation, var)
    if var == n:
        appreciation ="wow, le nombre etait:"
        print(appreciation, var, "vous avez assaiye:", nbr)
        break
