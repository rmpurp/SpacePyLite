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

