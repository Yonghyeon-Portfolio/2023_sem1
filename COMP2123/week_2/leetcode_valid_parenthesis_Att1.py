class Solution:
    def __init__(self):
        self.match = {'{' : '}', '(' : ')', '[' : ']'}

    def loop(self, ls_in):
        ls_out = []
        skip = False
        modified = False
        for i in range(0, len(ls_in)-1):
            if skip:
                skip = False
                continue
            if self.match.get(ls_in[i]) == ls_in[i+1]:
                skip = True
                modified = True
            else:
                ls_out.append(ls_in[i])
        if not skip:
            ls_out.append(ls_in[-1])
        return ls_out, modified

    def isValid(self, s: str) -> bool:
        ls_in = list(s)
        
        while True:
            ls_in, modified = self.loop(ls_in)
            if not modified:
                break
            if len(ls_in) == 0:
                break
        if len(ls_in) > 0:
            return False
        return True


