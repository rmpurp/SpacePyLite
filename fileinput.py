import shutil
import os
from .card import Card
from .utils import getch

# TODO Learn mode
# TODO Rating system


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


def make_card(unit):
    return Card(*unit[:3])


def validate_unit(unit):
    return len(unit) >= 2


def read_cards(filepath):
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

    shutil.copy(filename + '.tmp', filename)
    os.remove(filename + '.tmp')



