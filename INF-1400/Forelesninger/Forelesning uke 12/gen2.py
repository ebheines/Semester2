
class MyStack:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        self.iter_current = None

    def __iter__(self):
        self.iter_current = self.top
        return self
    
    def __next__(self):
        if self.iter_current:
            current_data = self.iter_current.data
            self.iter_current = self.iter_current.next
            return current_data
        else:
            raise StopIteration

    def put(self, data):
        if not self.top:
            self.top = MyStack.Node(data)
        else:
            new_node = MyStack.Node(data)
            new_node.next = self.top
            self.top = new_node
    
    def peek(self):
        if self.top:
            return self.top.data
        return None

    def pop(self):
        if self.top:
            top_data = self.top.data
            self.top = self.top.next
            return top_data
        return None


if __name__ == "__main__":
    line = MyStack()
    line.put("Torsk")
    line.put("Sei")
    line.put("Hyse")
    line.put("Kveite")

    for fisk in line:
        print(fisk)
