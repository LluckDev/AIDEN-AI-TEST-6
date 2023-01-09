from files import filestartAndStop


class AidanCore:
    def __init__(self):
        #load dependisys
        self.o = filestartAndStop()

        #load files
        #make vars
        self.weights = self.o.weights()
        self.bias = self.o.bias()
        self.other = self.o.other()


    def end(self):
        pass
        self.o.cw(self.weights)
        self.o.cb(self.bias)
        self.o.co(self.other)

