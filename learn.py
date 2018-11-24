from random import shuffle


class CardBag:
    def __init__(self, cards, num_cards, shuffle=True):
        eligible_cards = list(filter(lambda x: x.is_reviewable(), cards))

        if num_cards < 0 or num_cards > len(eligible_cards):
            num_cards = len(eligible_cards)

        self.cards = eligible_cards[:num_cards]
        self.last_card = None

        self.current_bag = []
        self.shuffle = shuffle

    def refill_bag(self):
        new_cards = self.cards[:10 - len(self.current_bag)]
        del self.cards[len(self.current_bag):10]

        if self.shuffle:
            shuffle(new_cards)

        self.current_bag.extend(new_cards)

    def recycle_last(self):
        self.current_bag.append(self.last_card)

    def __next__(self):
        if self.cards and len(self.current_bag) < 3:
            self.refill_bag()

        if not self.current_bag:
            raise StopIteration

        self.last_card = self.current_bag.pop(0)

        return self.last_card

    def __iter__(self):
        return self


def learn(cards, show_fn, rate_fn, num_cards=-1):
    if num_cards <= 0:
        return

    bag = CardBag(cards, num_cards)

    for card in bag:
        show_fn(card)
        rating = rate_fn(card)
        if rating < 2:
            bag.recycle_last()
