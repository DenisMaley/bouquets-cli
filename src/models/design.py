import re

from .flower import Flower


class Design:
    FLOWER_FORMAT = '(?P<flower_amount>\d+)(?P<flower_name>[a-z])'
    DESIGN_FORMAT = '^(?P<design_name>[A-Z])(?P<size>[S|L])(?P<flowers_set>({flower})*)(?P<total_amount>\d+)$'.format(
        flower=FLOWER_FORMAT)

    def __init__(self, spec):
        match = re.search(self.DESIGN_FORMAT, spec)
        if match is None:
            raise Exception('Wrong format of the bouquet design: {}'.format(spec))

        self.spec = spec
        self.name = match.group('design_name')
        self.size = match.group('size')
        self.total_amount = int(match.group('total_amount'))
        self.flowers = self.parse_flowers_set(match.group('flowers_set'))

        if not self.validate_amount():
            raise Exception('Wrong amount of the flowers in the design: {}'.format(spec))

    def __repr__(self):
        return self.spec

    def parse_flowers_set(self, spec):
        flowers = []
        for match in re.finditer(self.FLOWER_FORMAT, spec):
            flower_spec = '{name}{size}'.format(name=match.group('flower_name'), size=self.size)
            flowers.append({'flower': Flower(flower_spec), 'amount': int(match.group('flower_amount'))})
        return flowers

    def get_extra_amount(self):
        return self.total_amount - self.get_fixed_amount()

    def get_fixed_amount(self):
        return sum([flower_spec['amount'] for flower_spec in self.flowers])

    def validate_amount(self):
        return self.total_amount >= self.get_fixed_amount()