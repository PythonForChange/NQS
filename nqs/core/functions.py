import user.config as config
from nqs.resources.extensions import py

class Func():
  def __init__(self,name: str,params,actions,indexfile: str,definitionsfile: str):
    self.name=name
    self.params=params
    self.actions=actions
    self.indexfile=indexfile
    self.definitionsfile=definitionsfile
  def index(self):
    lines=py.getLines(self.indexfile)
    lines.pop()
    newline="\'"+self.name+"\': Definition."+self.name+", "
    lines.append(newline)
    lines.append("}")
    text=""
    for i in lines:
      text+=i+"\n"
    py.write(text,self.indexfile)
  def define(self):
    T="\tdef "+self.name+"("
    last=self.params[-1]
    j=self.params
    j.pop()
    for i in j:
      T+=i+","
    T+=last+"):\n"
    for i in self.actions:
      T+="\t\t"+i+"\n"
    py.append(T,self.definitionsfile)
  def add(self):
    self.define()
    self.index()

def clear(param: str):
  if param=="all":
    t1="from user.definitions import Definition\nIndex = { \n\'__init__\': Definition.__init__,  # Do not remove this function, Index must not be void\n}\n"
    py.write(t1,config.index)
    t2="class Definition():\n\tdef __init__(): # Do not remove this function, Definition must not be void\n\t\treturn \"done\""
    py.write(t2,config.definitions)
