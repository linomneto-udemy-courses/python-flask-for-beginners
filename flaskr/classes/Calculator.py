#!python3

class Calculator:
    
    def __init__(self, n1, op, n2):
        self.n1 = n1
        self.op = op
        self.n2 = n2

    def run(self):
        if (self.op == '+'):
            self.result = self.n1 + self.n2
        elif (self.op == '-'):
            self.result = self.n1 - self.n2
        elif (self.op == '/'):
            self.result = self.n1 / self.n2
        elif (self.op == '*'):
            self.result = self.n1 * self.n2
        else:
            raise Exception("Not supported calculation operation.")
        return self.result
    