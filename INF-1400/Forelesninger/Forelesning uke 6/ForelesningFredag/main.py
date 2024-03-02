

class Node:
    def __init__(self, frekvens):
        self.frekvens = frekvens

    def __str__(self):
        return "Node, frekvens: " + str(self.frekvens)


class Rack:
    def __init__(self, max_noder):
        self.max_noder = max_noder
        self.noder = []
    
    def har_plass(self):
        return len(self.noder) < self.max_noder
    
    def add_node(self, frekvens):
        self.noder.append(Node(frekvens))
    
    def gjennomsnitt_frekvens(self):
        snitt = 0
        for node in self.noder:
            snitt += node.frevens
        return snitt / len(self.noder)
    
    def __str__(self):
        s = "== Rack =="
        s += "\nPlasser: " + str(self.max_noder)
        s += "\nInneholder " + str(len(self.noder)) + " noder:\n"
        for node in self.noder:
            s += str(node) + "\n"
        return s


class Cluster():
    def __init__(self):
        self.rack = []

    def add_rack(self, max_plasser):
        self.rack.append(Rack(max_plasser))

    def add_node(self, frekvens):
        for rack in self.rack:
            if rack.har_plass():
                rack.add_node(frekvens)
                return
        print("Space no more")

    def gjennomsnitt_frekvens(self):
        snitt = 0
        for rack in self.rack:
            snitt += rack.gjennomsnitt_frekvens()
        snitt = snitt / len(self.rack)
        print("Snittfrekvens i systemet: " + str(snitt))
    
    def __str__(self):
        r = "==== Cluster ====\n\n"
        for rack in self.rack:
            r += str(rack) + "\n"
        return r


if __name__ == "__main__":
    abel = Cluster()

    abel.add_rack(5)
    abel.add_rack(3)

    for i in range(5):
        abel.add_node(3.0)
    abel.add_node(2.5)
    abel.add_node(2.0)
    abel.add_node(2.0)
    
    print(abel)
    