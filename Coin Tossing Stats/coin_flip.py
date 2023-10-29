import random
from fractions import Fraction

how_many_times = int(input("How many heads in a row? "))
how_many_loops = 0
def coin_flip():
    count = 0
    coin_face = ["Heads","Tails"]
    while count < how_many_times:
        global how_many_loops
        how_many_loops += 1
        chosen_face = random.choice(coin_face)
        if chosen_face == "Heads":
            count = count + 1
        else:
            count = 0
    odds = Fraction((1/2) **(how_many_times))
    print("It has taken " + str(how_many_loops) + " tries to flip " + str(how_many_times) + " heads in a row.")
    print("The theoretical odds were " + str(odds))
    
coin_flip()






