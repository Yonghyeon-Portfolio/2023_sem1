from typing import Generic, List, TypeVar, Tuple

T = TypeVar('T')

class SeparateChaining(Generic[T]):
    _size: int  # The number of key-value pairs in the map.
    _capacity: int  # The maximum size of the underlying table
    _table: List[List[Tuple]]  # The underlying table with the entries

    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._table = [[] for n in range(capacity)]

    def hash(self, key: int) -> int:
        return key % self._capacity

    def put(self, key: int, value: T) -> None:
        bucket = self._table[self.hash(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
        # Update if key already exists
                old_val = bucket[i][1]
                bucket[i] = (key, value)
                return old_val
        # Simply append if key's new
        bucket.append((key, value))
        self._size += 1
        return None

    def get(self, key: int) -> T:
        bucket = self._table[self.hash(key)]
        for cell in bucket:
            if cell[0] == key:
        # Key Found
                return cell[1]
        # Key Not Found
        return None

    def remove(self, key: int) -> T:
        bucket = self._table[self.hash(key)]
        for i in range(len(bucket)):
            cell = bucket[i]
            if cell[0] == key:
        # element to remove Found
                self._size -= 1
                return bucket.pop(i)[1]
        # element to remove doesn't exist
        return None

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        if self._size == 0:
            return True
        return False

    def entries(self) -> List[Tuple[int, T]]:
        all_entries = []
        for bucket in self._table:
            for cell in bucket:
                all_entries.append(cell)
        return all_entries

if __name__ == "__main__":
    SC = SeparateChaining[str](5)
    SC.put(10, 'Ten')
    SC.put(3, 'Three')
    SC.put(5, 'Five')
    assert SC.size() == 3
    print(SC.entries())
    print(SC._table)
    assert SC.get(6) is None
    assert SC.get(5) == "Five"
    SC.put(10, "ten ten")
    assert SC.remove(10) == "ten ten"
    print(SC.entries())
    assert SC.remove(5) == "Five"
    assert SC.remove(3) == "Three"
    assert SC.is_empty() == True
    assert SC.entries() == []
    print(SC._table)