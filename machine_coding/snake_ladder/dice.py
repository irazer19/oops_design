import concurrent.futures
import random


class Dice:
    def __init__(self, dice_count):
        self.dice_count = dice_count

    def roll_dice(self):
        result = 0
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for _ in range(self.dice_count):
                future = executor.submit(self.get_val)
                val = future.result()
                result += val
        return result

    def get_val(self):
        return random.randint(1, 6)
