class MyQueue:
    def __init__(self):
        self.main_stack = []
        self.temp_stack = []
    
    def enqueue(self, e):
        self.main_stack.append(e)
    
    def dequeue(self):
        self.temp_stack.clear()
        for elem in self.main_stack[::-1]: # stack transfer
            self.temp_stack.append(elem)
        self.temp_stack.pop()
        self.main_stack = self.temp_stack[::-1] # stack transfer
    
    def __str__(self):
        return str(self.main_stack)


if __name__ == "__main__":
    Q = MyQueue()
    Q.enqueue(1)    
    Q.enqueue(2)    
    Q.enqueue(3) 
    print(Q)   
    Q.dequeue()
    print(Q)
    Q.dequeue()  
    print(Q)