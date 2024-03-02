
class Otter(list):
    def __init__(self):
        pass

    def add_stone_on_belly(self, stone):
        self.append(stone)

    def remove_one_stone(self):
        return self.pop(0)

o = Otter()
o.add_stone_on_belly(42)
o.add_stone_on_belly(4222)
print("Got", o.remove_one_stone())



