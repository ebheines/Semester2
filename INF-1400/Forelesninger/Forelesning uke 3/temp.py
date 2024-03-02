def add_one(number):
    number = number + 1

def flip(words):
    tmp = words[0]
    words[0] = words[1]
    words[1] = tmp

if __name__ == "__main__":
    greetings = ["Hello", "world"]

    flip(greetings)

    print(greetings)
