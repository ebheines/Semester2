

class Sorter:
    def __init__(self, items):
        self.items = items

    def bubblesort(self):
        print("Bubblesort, I choose you")
    
    def quicksort(self):
        print("Quicksort, I choose you! rawr")

    def sort(self):
        if len(self.items) < 100:
            self.bubblesort()
        else:
            self.quicksort()
    
    def __call__(self):
        self.sort()

    

nummeren = [x for x in range(50)]
nummerto = [x for x in range(10000)]

sorten = Sorter(nummeren)
sortto = Sorter(nummerto)

sorten()
sortto()
