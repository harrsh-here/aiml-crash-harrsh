# Program to implement a simple random number guessing game.

import random

tgt, att, max_att = random.randint(1, 100), 0, 15

while att < max_att:

    try:
        g = int(input(f"Guess ({att+1}/{max_att}): "))
        att += 1
        if g == tgt: 
            print(f"Correct in {att} tries!"); 
            break
        print("too high" if g > tgt else "too low")

    except ValueError: 
        print("Enter numbers only.")

else: 
    print(f"Game over! Number was {tgt}.")
