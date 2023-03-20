from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        times = len(self.q)
        for i in range(times-1):
            self.q.append(self.q.pop())
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]
        
    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == "__main__":
    m = MyStack()
    m.push(5)
    m.push(3)
    m.pop()
    print(m.q)
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()