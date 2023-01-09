from files import filestartAndStop
from Adisplay import display

class AidanCore:
    def __init__(self):
        #load dependisys
        self.o = filestartAndStop()

        #load files
        #make vars
        self.weights = self.o.weights()
        self.bias = self.o.bias()
        self.other = self.o.other()


        self.window_start()





        self.update()





    def keys(self,key):
        pass



    def update(self):

        #change to false to stop the loop
        self.repeat = True

        while self.repeat and self.w.runing:
            #updating window
            self.w.update()




        self.w.close()












    def window_start(self):
        #creates window
        self.w = display(screenX=800,screenY=600,title="AIDEN Ai",)
        self.w.sendkeys(self.keys)






    def end(self):
        pass
        self.o.cw(self.weights)
        self.o.cb(self.bias)
        self.o.co(self.other)

