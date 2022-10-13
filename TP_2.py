
import random

guess = random.randint(0, 100)
appreciation = "?"
nbr = 0
print("devinez le nombre que je pense(indice il est entre 0 et 100)")


while True:
    var = input("quell est votre choice")
    var = int(var)
    if var < guess :
        nbr += 1
        print("non, je pensais a un notre chiffre, il est plus grand:", var)

    else :
        nbr = nbr + 1
        print("non, je pensai a un notre chiffre, il est plus petit:", var)
    if var == guess:
        appreciation ="wow, le nombre etait:"
        print(appreciation, var, "vous avez assaiye:", nbr)





