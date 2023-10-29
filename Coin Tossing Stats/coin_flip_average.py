import random
import statistics
from fractions import Fraction

def coin_flip_average(n):
    how_many_times = int(input("How many heads in a row? "))
    how_many_loops = 0
    average_times = []
    count2 = 0
    count = 0
    coin_face = ["Heads","Tails"]
    while count2< n:
        count2 = count2 + 1
        while count < how_many_times:
            how_many_loops += 1
            chosen_face = random.choice(coin_face)
            if chosen_face == "Heads":
                count = count + 1
            else:
                count = 0
        average_times.append(how_many_loops)
        count = 0
        how_many_loops = 0
        
    average_number_of_times = sum(average_times) / len(average_times)
    odds = Fraction((1/2) **(how_many_times))
    print("The theoretical odds were " + str(odds))
    print("The average number of times was " + str(average_number_of_times))
    
    

coin_flip_average(20000)

    
