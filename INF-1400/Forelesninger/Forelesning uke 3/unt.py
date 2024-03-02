class Data:
    def __init__(self, number):
        self.number = number

    def print_info(self):
        print("This is the number: ", self.number)   

def change_number(data_obj, new_value):
    data_obj.number = new_value

if __name__ == "__main__":
    tall = Data(5)

    tall.print_info()

    change_number(tall, 18)

    tall.print_info()
