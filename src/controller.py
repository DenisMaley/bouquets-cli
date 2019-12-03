from tqdm import tqdm
from src.services.parser import Parser
from src.services.picker import Picker
from src.models.storage import Storage


class Controller:
    def __init__(self, capacity):
        self.storage = Storage(capacity)

    def run(self, input):
        parser = Parser(input)
        try:
            designs, flowers = parser.parse()
        except Exception as err:
            print("Error: {}".format(err))
            return

        picker = Picker(designs, self.storage)

        bouquets = []
        with tqdm(total=len(flowers)) as pbar:
            for i, flower in enumerate(flowers):
                pbar.update(1)
                try:
                    picker.handle(flower)
                    bouquet = picker.pick_up()
                    if bouquet:
                        bouquets.append(bouquet.__repr__())
                except Exception as err:
                    print("Error: {} parsing flowers' input at {} position".format(err, i))
                    return

        return '\n'.join(bouquets)
