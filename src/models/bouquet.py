from collections import defaultdict


class Bouquet:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.flowers = defaultdict(int)

    def __repr__(self):
        flowers_spec = "".join(["".join([key, str(val)]) for key, val in sorted(self.flowers.items())])
        return "{0}{1}{2}".format(self.name, self.size, flowers_spec)

    def add(self, flower):
        if flower.size == self.size:
            self.flowers[flower.name] += 1
