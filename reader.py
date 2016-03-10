class CodeJamReader:
    def __init__(self, file):        
        self.text = []
        for line in file.readlines():
            self.text += line.strip().split()
        self.pos = 0

    def getStr():
        s = self.text[self.pos]
        self.pos += 1
        return s

    def getInt():
        return int(self.getStr())

    def getFloat():
        return float(self.getStr())

