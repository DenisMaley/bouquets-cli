from src.models.flower import Flower
from src.models.design import Design


class Parser:
    def __init__(self, input):
        self.lines = input.splitlines()

    def parse(self):
        designs = self.parse_until_empty(Design)
        flowers = self.parse_until_empty(Flower)

        return designs, flowers

    def parse_until_empty(self, model):
        result = []
        while self.lines:
            line = self.lines.pop(0)
            if not line:
                break
            result.append(model(line))
        return result
