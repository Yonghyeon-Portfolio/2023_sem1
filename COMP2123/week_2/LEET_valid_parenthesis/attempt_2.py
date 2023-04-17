class Solution:
    def match_algo(self, elem):
        try:
            return self.match.get(self.stack[-1]) == elem
        except Exception as e:
            return False
        
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        self.match = {'{' : '}', '(' : ')', '[' : ']'}
        self.stack = [s[0]]
        
        for i in range(1, len(s)):
            if self.match_algo(s[i]):
                self.stack.pop(-1)
            else:
                self.stack.append(s[i])  
        
        if len(self.stack) == 0:
            return True
        else:
            return False              

if __name__ == "__main__":
    s = Solution()
    result1 = s.isValid("(){}[]")
    result2 = s.isValid("(([(){}{}[()()]]))")
    result3 = s.isValid("[]]")
    
    print("results:", result1, result2, result3)