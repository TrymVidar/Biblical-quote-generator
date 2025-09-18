import random

with open('/home/chud/Documents/bible.txt', 'r')as file:
    quotes = file.readlines()

def get_random_quote():
    return random.choice(quotes).strip()

while True:
    cmd = input('One hath come seeking wisdome..')
    print (get_random_quote())

    break
