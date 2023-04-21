from typing import List
from item import Item

class PriorityQueue():
    _sorted_list : List[Item]
    def __init__(self, initial: dict = {}) -> None:
        self._sorted_list = []
        for key, value in initial.items():
            self.insert(key, value)

    def size(self) -> int:
        return len(self._sorted_list)

    def is_empty(self) -> bool:
        if self.size() == 0:
            return True
        return False

    def insert(self, k: int, v: str) -> None: 
        insert_item = Item(k, v)
        self._sorted_list.append(insert_item)
        idx = self.size() - 1
        while idx > 0:
            if self._sorted_list[idx - 1].get_key() > insert_item.get_key():
                self._sorted_list[idx] = self._sorted_list[idx - 1]
                idx -= 1
            else:
                break
        self._sorted_list[idx] = insert_item
        
        
    def remove_min(self):
        if self.size() == 0:
            return
        to_be_poppsed =  self._sorted_list[0]
        self._sorted_list = self._sorted_list[1:]
        return to_be_poppsed
        
    def min(self) -> Item:
        if self.size() == 0:
            return None
        return self._sorted_list[0]
    
    def __str__(self):
        s = "[ "
        for elem in self._sorted_list:
            s += f"({elem.get_key()} : {elem.get_value()}) "
        s += "]"
        return s

if __name__ == "__main__":
    sampleA = {1 : 'A', 5 : 'A', 100 : 'C', -1 : 'D', 1 : 'C'}
    pq = PriorityQueue(sampleA)
    pq.insert(1, 'D')
    pq.remove_min()
    print(pq)