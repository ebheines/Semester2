class A:
    def __init__(self, val):
        self.val = val

class B:
    def __init__(self, val):
        self.val = val
    

l = [A(45), B(100)]

for klasse in l:
    print(klasse, klasse.val)




# Oppgave 4 a
'''
A classattribute is a attribute connected to a class.
An Attribute is a element in the class, it can be a list, a 
varible, a string etc. It can be whatever you want it to be
This attribute stores data connected to the class, for example
if you have a class Airport, you want to have a list of all
the planes in the airport. Then you can make the attribute
planelist which will be a list that can keep track of all
planes in the Airport. 
'''


    
