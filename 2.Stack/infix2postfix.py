class conversion:
    def __init__(self,n):
        self.capacity=n
        self.top=-1
        self.stack=[]
        self.output=[]
        self.precedance={'+':1, '-':1, '*':2, '/':2,'^':3}

    def precd(self,char):
        
        try:
            
            if len(self.stack)!=0:
                a=self.precedance[char]
                b=self.precedance[self.stack[-1]]
                if a<b:
                    return True
                else:
                    return False
        except KeyError:
            return False
        
    def convert(self,exp):
        for char in exp:
            if char.isalpha():
                self.output.append(char)
            else:
                if not self.stack:
                    self.stack.append(char)
                if char=="(":
                    self.stack.append(char)
                if char==")":
                    while (x!="(" and len(self.stack)!=0):
                        x=self.stack[-1]
                        self.stack.pop()
                        self.output.append(x)
                    if (x!="(" and len(self.stack)!=0):
                        return -1
                    else:
                        self.output.pop()
                else:
                    while (self.precd(char) and len(self.stack)!=0):
                        x=self.stack.pop()
                        self.output.append(x)
                    self.stack.append(char)
        while len(self.stack)!=0:
            x=self.stack.pop()
            self.output.append(x)
        print(self.output)
exp="p*q^r+s"
e=conversion(len(exp))
e.convert(exp)
