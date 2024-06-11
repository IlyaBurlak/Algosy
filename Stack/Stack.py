class Stack:
    def __init__(self) -> None:
        self.arr = list()

    def push (self , element):
        self.arr.append(element)

    def get (self):
        if len(self.arr) == 0:
            pass
        else:
            return self.arr.pop()

    def isEmpty(self) -> bool:
        return  len(self.arr) == 0 

    def size(self):
        return len(self.arr)
    
   


