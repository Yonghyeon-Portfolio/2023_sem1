class MStack:
    def __init__(self):
        # holds colors in MStack
        self.colors = [None]        
        self.mono_streak = 0
        self.ms_rec = [0] # mono-streak record
        self.max_ms_rec = [0] # max mono-streak record
    
    def get_MonoMax(self):
        return self.max_ms_rec[-1]
    
    def push(self, col):
        if col == self.colors[-1]:
            self.mono_streak += 1
        else:
            self.mono_streak = 1
            
        self.colors.append(col)
        self.ms_rec.append(self.mono_streak)
        
        if self.mono_streak > self.max_ms_rec[-1]:
            self.max_ms_rec.append(self.mono_streak)
        else:
            self.max_ms_rec.append(self.max_ms_rec[-1])
    
    def pop(self):
        if len(self.colors) <= 1:
            return None
        popped = self.colors.pop()
        self.ms_rec.pop()
        self.mono_streak = self.ms_rec[-1]
        self.max_ms_rec.pop()
        return popped
        
    def __str__(self):
        s = "Colors: %s\n" % str(self.colors)
        s += "Streak Record: %s\n" % str(self.ms_rec)
        s += "MaxMono Idx: %s\n" % str(self.max_ms_rec)
        s += "MaxMone returns %s\n" % self.get_MonoMax()
        return s
    
if __name__ == "__main__":
    MS = MStack()
    MS.pop()
    print(MS)
    MS.push("red")
    MS.push("yellow")
    print(MS)
    MS.push("yellow")
    MS.push("yellow")
    MS.push("blue")
    print(MS)
    MS.push("blue")
    MS.push("green")
    MS.push("green")
    MS.push("green")
    MS.push("green")
    MS.push("green")
    print(MS)
    MS.pop()
    MS.pop()
    MS.pop()
    
    print(MS)
    
                        
        
     