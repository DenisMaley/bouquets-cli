from collections import defaultdict


class Storage:
    def __init__(self, capacity=None):
        self.capacity = capacity
        # Instead of counting each time how many items we have in the stock
        # Not ideal, but will save some resources
        self.tape = []
        self.stock = defaultdict(lambda: defaultdict(int))

    def full(self):
        return self.capacity is not None and self.count() >= int(self.capacity)

    def insert(self, flower):
        if self.full():
            raise Exception('Storage is full, no room for the flower {}'.format(flower.__repr__()))
        self.stock[flower.size][flower.name] += 1
        self.tape.append(flower)

    def extract(self, flower):
        if self.stock[flower.size][flower.name] == 0:
            raise Exception('The flower {} is out of stock'.format(flower.__repr__()))
        self.stock[flower.size][flower.name] -= 1
        flower_in_tape = next((x for x in self.tape if x.spec == flower.spec), None)
        index = self.tape.index(flower_in_tape)
        return self.tape.pop(index)

    def first_by_size(self, size):
        if self.count_by_size(size) == 0:
            raise Exception('The flowers of size {} are out of stock'.format(size))
        index = list(map(lambda flower: flower.size == size, self.tape)).index(True)
        return self.tape[index]

    def count_by_size(self, size):
        return sum(self.stock[size].values())

    def count(self):
        return len(self.tape)
