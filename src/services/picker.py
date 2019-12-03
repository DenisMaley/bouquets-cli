from src.models.bouquet import Bouquet


class Picker:
    def __init__(self, designs, storage):
        self.designs = designs
        self.storage = storage

    def handle(self, flower):
        self.storage.insert(flower)

    def pick_up(self):
        design = self.get_least_sufficient_design()
        if design:
            return self.pick_up_bouquet(design)
        return False

    def get_least_sufficient_design(self):
        sufficient_designs = self.sufficient_designs()
        if not sufficient_designs:
            return False
        sufficient_designs.sort(key=lambda design: design.total_amount, reverse=True)
        return sufficient_designs[0]

    def sufficient_designs(self):
        return list(filter(self.sufficient, self.designs))

    def sufficient(self, design):
        if design.total_amount > self.storage.count_by_size(design.size):
            return False
        for flower_spec in design.flowers:
            if flower_spec['amount'] > self.storage.stock[design.size][flower_spec['flower'].name]:
                return False
        return True

    def pick_up_bouquet(self, design):
        bouquet = Bouquet(design.name, design.size)
        bouquet = self.pick_up_spec_flowers(bouquet, design)
        bouquet = self.pick_up_non_spec_flowers(bouquet, design)

        return bouquet

    def pick_up_spec_flowers(self, bouquet, design):
        for flower_spec in design.flowers:
            for _ in range(flower_spec['amount']):
                flower = self.storage.extract(flower_spec['flower'])
                bouquet.add(flower)
        return bouquet

    def pick_up_non_spec_flowers(self, bouquet, design):
        for _ in range(design.get_extra_amount()):
            suitable_flower = self.storage.first_by_size(design.size)
            flower = self.storage.extract(suitable_flower)
            bouquet.add(flower)
        return bouquet
