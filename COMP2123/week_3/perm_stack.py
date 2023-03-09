class Cell:
    def __init__(self, elements):
        # 2D list
        self.elements = elements
        self.permuted = False
        
    def perm_complete(self, max_len):
        '''<self.elements> can hold up to maximum of 
            <max_len> 1D lists'''
        if len(self.elements) == max_len:
            return True
        else:
            return False
    
    def further_permute(self):
        '''
        returns list of further permuted cells from itself
        [[A, B]] -> [[[A], [B]] , [[B], [A]]]
        '''
        self.permuted = True
        result = []
        last_elem = self.elements[-1]
        for i in range(len(last_elem)-1, -1, -1):
            rest = last_elem[:i] + last_elem[i+1:]
            division = [[last_elem[i]], rest]
            result.append(Cell(self.elements[:-1] + division))
        
        return result
    
    def __str__(self):
        info = "["
        for lst in self.elements:
            for e in lst:
                info += (str(e) + ", ")
        info += "\b\b]"
        return info

def permutations(input_ls):
    PERM_STACK = []
    CELL_MAX_LEN = len(input_ls)
    PERM_RESULT = []
    
    PERM_STACK.append(Cell([input_ls]))

    while (len(PERM_STACK) > 0):
        cell = PERM_STACK[-1]
        
        if cell.perm_complete(CELL_MAX_LEN):
            PERM_RESULT.append(cell)
            PERM_STACK.pop()
            continue
        if cell.permuted:
            PERM_STACK.pop()
            continue
        
        cells = cell.further_permute()
        for c in cells:
            PERM_STACK.append(c)
            
    return PERM_RESULT

if __name__ == "__main__":             
    result = permutations([1, 2, 3, "A", "B"])
    print("RESULT:")
    for r in result:
        print(r)