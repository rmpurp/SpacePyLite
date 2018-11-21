import datetime
import json
import shutil
import os
from sys import argv
from utils import getch

# TODO Learn mode
# TODO Rating system
# Essentially copy algorithm from you-know-what
# May want to update text file after EVERY card review

class Card:
    necessary_fields = ['ef', 'iter_num', 'next_review', 'spacing']

    def __init__(self, description, response, metadata=None):
        self.description = description
        self.response = response
        if not metadata:
            metadata = {
                'ef': 2.5,
                'iter_num': 0,
                'next_review': datetime.date.today(),
                'iter_length': 0
            }
        else:
            try:
                metadata = json.loads(metadata)
                metadata['next_review'] = datetime.date.fromisoformat(
                    metadata['next_review'])

            except (json.decoder.JSONDecodeError, ValueError):
                print("Invalid JSON metadata string for {}: {}".format(
                    response, metadata))
                exit(1)
        self.metadata = metadata

    def is_reviewable(self, current_date=None):
        if not current_date:
            current_date = datetime.date.today()

    def rate(self, score):
        pass

    def __repr__(self):
        return 'Card({!r}, {!r}, {!r})'.format(self.description, self.response,
                                               self.metadata)

    def __str__(self):
        metadata_string_date = dict(self.metadata)
        metadata_string_date['next_review'] = self.metadata[
            'next_review'].isoformat()
        return '\n'.join((self.description, self.response,
                          json.dumps(metadata_string_date)))


def prompt_menu(items, message='Select one of the following options.'):
    while True:
        print(message)
        for idx, item in enumerate(items):
            print('{}: {}'.format(idx, item))
        input_str = getch()
        try:
            num = int(input_str)
            if 0 <= num < len(items):
                return num
        except ValueError:
            pass
        print('Invalid input.')


class CardBag:
    def __init__(self, cards, num_cards):
        eligible_cards = list(filter(lambda x: x.is_reviewable(), cards))
    
        if num_cards < 0 or num_cards > len(eligible_cards):
            num_cards = len(eligible_cards)
    
        self.cards = eligible_cards[:num_cards]
        self.last_card = None

        self.current_bag = []

    def refill_bag(self):
        new_cards = active_cards[len(current_bag):10]
        shuffle(new_cards)
        current_bag.extend(new_cards)

    def next_card(self):
        if not self.current_bag:
            self.current_bag = eligible_cards[:num_cards]

    def replace_last_card(self):


def learn(cards, current_time=None, num_cards=-1):
    if num_cards <= 0:
        return












def make_card(unit):
    return Card(*unit[:3])


def validate_unit(unit):
    return len(unit) >= 2


def get_cards(filepath):
    with open(filepath) as f:
        units = [x.strip().split('\n') for x in f.read().split('\n\n')]
        cards = map(make_card, filter(validate_unit, units))
        return cards


def write_cards(filepath, cards):
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    temp_name = os.path.join(directory, filename + '.tmp')

    with open(temp_name, 'w') as f:
        f.write('\n\n'.join(map(str, cards)) + '\n')

    shutil.copy('test.txt.tmp', 'test.txt')
    os.remove('test.txt.tmp')


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

    cards = get_cards(filename)
    write_cards(filename, cards)
