def permutations(input_list):
    perms = []
    if len(input_list) == 1:
        return [input_list]
    
    for idx in range(len(input_list)):
        # rest = idx element를 제외한 list
        rest = input_list[:idx] + input_list[idx+1:]
        rest_perm = permutations(rest)
        for rp in rest_perm:
            perms.append([input_list[idx]] + rp)
    return perms

# def permutation(raw_list: list) -> list:
#     for elem in raw_list:
#         print(f"{elem} " )

# result = permmutations([1, 2, 3])
# for r in result:
#     print(r)
if __name__ == "__main__":
    result = permutations([1, 2, 3])
    for r in result:
        print(r)