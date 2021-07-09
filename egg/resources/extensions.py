import os

class Lang:
    def __init__(self,name: str):
        self.name=name
        self.extension="."+self.name
    def write(self,T: str,name: str):
        f=open(name+self.extension,"w")
        f.write(T)
        f.close()
    def append(self,T: str,name: str):
        f=open(name+self.extension,"a")
        f.write(T)
        f.close()
    def read(self, name: str):
        f=open(name+self.extension,"r")
        text=f.read()
        f.close()
        return text
    def execute(self,name: str):
        try:
            t="/usr/bin/python "+name+self.extension
            os.system(t)
        except:
            print("Execute error in: "+"/usr/bin/python "+name+self.extension)
    def delete(self,name: str):
        os.remove(name+self.extension)
    def getLines(self,name: str):
        h=open(name+self.extension,"r")
        lines=h.readlines()
        h.close()
        return lines

py=Lang("py")
txt=Lang("txt")
nqa=Lang("nqa")
pfcf=Lang("pfcf")