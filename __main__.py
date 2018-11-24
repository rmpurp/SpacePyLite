from .fileinput import read_cards, write_cards
from sys import argv
from learn import learn
from functools import partial

if __name__ == '__main__':
    if len(argv) <= 1:
        print("Error: no file specified.")
        exit(1)
    filename = argv[1]
    if len(argv) >= 3:
        try:
            num_to_learn = int(argv[2])
        except ValueError:
            print("Invalid number of cards to learn.")
    else:
        num_to_learn = None

    cards = read_cards(filename)

    learn(cards,
          show_fn=None,
          rate_fn=None,
          write_fn=partial(write_cards, filename, cards),
          num_cards=num_to_learn)
