from collections import deque

def permmutations(ls):
    if len(ls) == 0:
        return []
    if len(ls) == 1:
        return [ls]
    
    # prev_perm : list[ permutations(list) ]
    prev_perm = permmutations(ls[:-1])
    # print(prev_perm)
    new_perm = []
    for pp_idx in range(len(prev_perm)):
        for idx in range(len(ls)):
            new_perm_elem = prev_perm[pp_idx].copy()
            new_perm_elem.insert(idx, ls[-1])
            new_perm.append(new_perm_elem)      
    return new_perm

def permutations_B(input_list):
    if len(input_list) == 1:
        return [input_list]
    perms = []
    for idx in range(len(input_list)):
        rest = input_list[:idx] + input_list[idx+1:]
        rest_perm = permutations_B(rest)
        for rp in rest_perm:
            perms.append([input_list[idx]] + rp)
    return perms

# result = permmutations([1, 2, 3])
# for r in result:
#     print(r)
if __name__ == "__main__":
    result = permutations_B(['A', 'B', 'C', 'D'])
    for r in result:
        print(r)