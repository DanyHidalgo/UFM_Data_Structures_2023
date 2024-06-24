
class Stack:

    def __init__(self, size: int):
        self.elements = [None] * size
        self.top = -1
        self.max = size 


    def __repr__(self) -> str:
        return "Top: {} | Elements: {}".format(self.top, self.elements)
    

    def push(self, value: str) -> None:
        if self.top == int(self.max) - 1:
            print('Stack overflow')
            return None

        self.top += 1
        self.elements[self.top] = value

    
    def pop(self) -> str:
        if self.top == -1:
            print('Stack underflow')
            return None

        value = self.elements[self.top]
        self.elements[self.top] = None
        self.top -= 1
        return value

    
    def peek(self) -> str:
        if self.top == -1:
           print('Stack vacio')
           return None
        
        value = self.elements[self.top]
        return value
    
    def search(self, key: str) -> int:

        for i in range(self.top + 1):
            if self.elements[i] == key:
                return i
        
        return -1

