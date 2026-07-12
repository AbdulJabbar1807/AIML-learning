import random

coin = random.choice(["heads","tails"])
print(coin)

choose_random = random.randint(1, 10)
print(choose_random)

cards = ["king","queen","jack"]
random.shuffle(cards)
for card in cards:
    print(card)