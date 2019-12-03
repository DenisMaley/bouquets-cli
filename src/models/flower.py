import re


class Flower:
    FORMAT = '^(?P<name>[a-z])(?P<size>[S|L])$'

    def __init__(self, spec):
        match = re.search(self.FORMAT, spec)
        if match is None:
            raise Exception('Wrong format of the flower: {}'.format(spec))

        self.spec = spec
        self.name = match.group('name')
        self.size = match.group('size')

    def __repr__(self):
        return self.spec