class filestartAndStop:
    def __init__(self):
        pass
    def loadFile(self, file):
        mid = []
        parced = []
        #looping thru every line
        for x in file:

            #spliting by coma
            mid = x.split(",")
            for i in range(len(mid)):
                #takeing out newlines
                sub = mid[i].split("\n")
                #puting vaules back in
                mid[i] = sub[0]
            #adding line

            parced.append(mid)
        #cleaning vars



        mid = []
        sub = []
        sc = False
        #run thru evry line
        for i in range(len(parced)):
            #checking if the line starts with a semicolan
             if parced[i][0] == ";":
                 #if yes ad mid witch wil later be parced but adding sub to it. sub is the lines before the semi colon puting it in to 3d
                 mid.append(sub)
                 #clearing sub
                 sub = []
                 #telling program that its 3d
                 sc = True
             else:
                 #adding line to sub
                 sub.append(parced[i])
                #making parced = mid
        #checks if it needs to be 3d
        if sc == True:
            #sets parced to 3d vertion
            parced = mid
        #if else it is already 2d
    #returning parced array

        return parced


    def weights(self):
        # preopen file
        f = open("files/weights")
        # send file to be parced then returning to the caller
        return self.loadFile(f)
        # cleaning file
        f.close()
    def bias(self):
        #preopen file
        f= open("files/bias")
        #send file to be parced then returning to the caller
        return self.loadFile(f)
        #cleaning file
        f.close()
    def other(self):
        #preopen file
        f= open("files/other")
        #send file to be parced then returning to the caller
        return self.loadFile(f)
        #cleaning file
        f.close()

    def cw(self,data):

        # preopen file
        f = open("files/weights","w")
        #close file
        self.closefile3d(f, data)
        # close file
        f.close()
        return 0
    def cb(self,data):

        # preopen file
        f = open("files/bias","w")
        #close file
        self.closefile2d(f, data)
        # close file
        f.close()
        return 0
    def co(self,data):

        # preopen file
        f = open("files/other","w")
        #close file
        self.closefile2d(f, data)
        # close file
        f.close()
        return 0







    def closefile2d(self, file, data):
        ffi = ""

        for x in range(len(data)):
            for y in range(len(data[x])):
                if y != len(data[x])-1:
                    ffi = ffi + f"{data[x][y]},"
                else:
                    ffi += f"{data[x][y]}"
            ffi+="\n"

        file.write(ffi)

        return 0
    def closefile3d(selfself,file,data):
        ffi = ""
        for x in range(len(data)):
            for y in range(len(data[x])):
                for z in range(len(data[x][y])):
                    if z != len(data[x]) - 1:
                        ffi = ffi + f"{data[x][y][z]},"
                    else:
                        ffi += f"{data[x][y][z]}"
                ffi+="\n"
            ffi += ";\n"
        file.write(ffi)
        return 0


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

