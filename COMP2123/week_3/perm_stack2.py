def stack_perm(ls):
    cell_stack = [ls]
    complm_stack = [[]]
    status_stack = [False]
    result_list = []
    
    while len(cell_stack) > 0:
        parent_cell = cell_stack[-1]
        
        if len(parent_cell) == 1:
            # indicates that the permutation is complete
            # print(complm_stack[-1] + parent_cell)
            result_list.append(complm_stack[-1] + parent_cell)
            cell_stack.pop()
            complm_stack.pop()
            status_stack.pop()
            continue
        if status_stack[-1]:
            cell_stack.pop()
            complm_stack.pop()
            status_stack.pop()
            continue
            
        """
        -  Add child(new) cell to cell_stack.
            new cell has one less element than parent cell
        -  Add popped element from child cell to complm_stack
        -  Adjust element of status_stack with same idx as the
            parent cell to be True. Also add False(s) to 
            status_stack as many as number of child cells created
        """
        status_stack[-1] = True
        parent_complm = complm_stack[-1]
        for i in range(len(parent_cell)-1, -1, -1):
            child_cell = parent_cell.copy()
            child_complm = parent_complm.copy()
            child_complm.append(child_cell.pop(i))
            complm_stack.append(child_complm)
            cell_stack.append(child_cell)
            status_stack.append(False)
    return result_list
                      
if __name__ == "__main__":
    ls = [1, 2, 3]
    stack_perm(ls)
