class SQueue:
    def __init__(self):
        self.queue = []
        self.ptr_start = 0
        self.ptr_end = -1
        self.even_ss_result = 0
        self.odd_ss_result = 0
    
    def get_first(self):
        return self.queue[self.ptr_start]

    def get_last(self):
        if not self.is_empty():
            return self.queue[self.ptr_end]
        return None
    
    def enqueue(self, e):
        self.queue.append(e)
        self.ptr_end += 1
        if (self.ptr_end % 2 == 0):
            self.even_ss_result += e
            self.odd_ss_result += 1/e
        else:
            self.even_ss_result += 1/e
            self.odd_ss_result += e
    
    def dequeue(self):
        if self.is_empty():
            return None
        if self.ptr_start % 2 == 0:
            self.even_ss_result -= self.get_first()
            self.odd_ss_result -= 1/self.get_first()
        else:
            self.even_ss_result -= 1/self.get_first()
            self.odd_ss_result -= self.get_first()
            
        self.ptr_start += 1      
        
    def seesaw(self):
        if self.ptr_start % 2 == 0:
            return self.even_ss_result
        else:
            return self.odd_ss_result
    
    def __str__(self):
        string = "["
        for i in range(self.ptr_start, self.ptr_end+1):
            string += str(self.queue[i]) + ", "
        string += "\b\b]"
        return string
    
    def is_empty(self):
        if self.ptr_start > self.ptr_end:
            return True
        return False
    

if __name__ == "__main__":
    Q = SQueue()
    Q.enqueue(4)
    Q.enqueue(2)
    Q.enqueue(2)
    Q.enqueue(4)
    print(Q)
    print(Q.seesaw())
    Q.enqueue(2)
    print(Q)
    print(Q.seesaw())
    Q.dequeue()
    print(Q)
    print(Q.seesaw())
    Q.dequeue()
    print(Q)
    print(Q.seesaw())
    
    
    
    
        
    