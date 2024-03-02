
class ReverseList(list):
    def __init__(self):
        super().__init__()
        self.current_idx = 0

    def __iter__(self):
        self.current_idx = len(self)-1
        return self
    
    def __next__(self):
        if self.current_idx < 0:
            raise StopIteration
        data = self[self.current_idx]
        self.current_idx -= 1
        return data
    

if __name__ == "__main__":
    numbers = ReverseList()
    for i in range(10):
        numbers.append(i)
    
    for element in numbers:
        print(element)