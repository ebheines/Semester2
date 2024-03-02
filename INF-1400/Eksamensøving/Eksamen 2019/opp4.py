
class Document:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.contents = []

    def get_info(self):
        return (self.id, self.name, self.contents)
    
    def set_id(self, id):
        if id < 0:
            raise ValueError("Id has to be a positive value")
        
        else:
            self.id = id
        


if __name__ == "__main__":
    
    d = Document()
    d.set_id(5)

    print(d)
