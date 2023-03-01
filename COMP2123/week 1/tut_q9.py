# Given a string (which you can see as an array of characters) of length n,
# determine whether the string contains k identical consecutive characters. You can
# assume that 2 ≤ k ≤ n. For example, when we take k = 3, the string ”abaaab”
# contains three consecutive a’s and thus we should return true, while the string
# ”abaaba” doesn’t contain three consecutive characters that are the same.
# Your task is to design an algorithm that always correctly returns whether the
# input string contains k identical consecutive characters. Your solution should run in
# O(n) time. In particular, k isn’t a constant and your running time shouldn’t depend
# on it.

def consecutive_k(k, string):
    if len(string) < 1 or k < 1:
        return None

    consecutive_num = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            consecutive_num += 1
        else:
            consecutive_k = 1
        if consecutive_num >= k:
            break
    if consecutive_num >= k:
        return True
    else:
        return False

if __name__ == "__main__":
    assert consecutive_k(4, "aaabbbbaa") == True
    print(consecutive_k(1, ""))
    assert consecutive_k(1, "a") == True
    assert consecutive_k(3, 'aabbaabbaabb') == False
