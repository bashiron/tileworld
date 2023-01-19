from random import choice, randint

def take_rand(ls, min_am, max_am):
    """Takes from `min` up to `max` amount of elements from the list, arbitrarily. Allows duplicates.
    """
    res = []
    amount = randint(min_am, max_am)
    while amount > 0:
        res.append(choice(ls))
        amount -= 1
    return res
