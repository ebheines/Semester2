class Otter:
    def __init__(self):
        self.plist = []

    def add_stone_on_belly(self, stone):
        self.plist.append(stone)

    def remove_one_stone(self):
        return self.plist.pop(0)

o = Otter()
o.add_stone_on_belly(42)
o.add_stone_on_belly(4222)
print("Got", o.remove_one_stone())
