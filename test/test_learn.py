from .. import learn
from .. import fileinput
from .generate_file import generate_file
from os import remove


def test_read():
    num_cards = 20
    filepath = generate_file(num_cards)
    cards = fileinput.read_cards(filepath)
    for i, card in enumerate(cards):
        assert card.description == f'front{i}'
        assert card.response == f'back{i}'

    remove(filepath)


def test_read_write():
    num_cards = 50
    filepath = generate_file(num_cards)
    cards = fileinput.read_cards(filepath)
    for i, card in enumerate(cards):
        assert card.description == f'front{i}'
        assert card.response == f'back{i}'

    fileinput.write_cards(filepath, cards)
    cards = fileinput.read_cards(filepath)
    for i, card in enumerate(cards):
        assert card.description == f'front{i}'
        assert card.response == f'back{i}'

    remove(filepath)
