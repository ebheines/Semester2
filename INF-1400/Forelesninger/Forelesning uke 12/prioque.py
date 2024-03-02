from gen2 import MyStack


class PrioQue(MyStack):

    class PrioNode(MyStack.Node):
        def __init__(self, task, priority):
            super().__init__(task)
            self.priority = priority

    def __init__(self):
        super().__init__()

    def put(elem):
        raise DeprecationWarning("Put is not supposed to be used")

    def add_task(self, name, priority):
        prev = self.top
        if not prev:
            self.top = PrioQue.PrioNode(name, priority)
            return
        elif self.top.priority < priority:
            prev_top = self.top
            self.top = PrioQue.PrioNode(name, priority)
            self.top.next = prev_top
        else:
            prev = self.top
            current = prev.next
            if not current:
                prev.next = PrioQue.PrioNode(name, priority)
                return
            while current and current.priority < priority:
                prev = current
                current = current.next
            newnode = PrioQue.PrioNode(name, priority)
            newnode.next = current
            prev.next = newnode

    def __next__(self):
        if self.iter_current:
            current_data = self.iter_current.data
            current_prio = self.iter_current.priority
            self.iter_current = self.iter_current.next
            return current_data, current_prio
        else:
            raise StopIteration


if __name__ == "__main__":
    tasks = PrioQue()
    tasks.add_task("Gaming", 2)
    tasks.add_task("Oblig", 3)
    tasks.add_task("Tull", 9)
    tasks.add_task("Dishwasher", -10)

    for task, prio in tasks:
        print(task, prio)