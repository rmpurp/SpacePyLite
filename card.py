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


