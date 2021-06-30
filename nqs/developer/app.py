from nqs.developer.run import run
from nqs.core.core import compile
from nqs.resources.extensions import nqa
from nqs.resources.console import display, get, sleep

def developerDisplay(name: str):
    content=nqa.read(name)
    display(content)

def developerConsole(condition: bool = True):
  print("Developer Console is now running")
  while condition:
    i=get("nqs")
    name="temp_compile"
    if i=="$display":
      content=nqa.read(name)
      print(content)
    elif i=="$compile":
      compile(name)
    elif i=="$save":
      print("Save as:")
      adress=get("nqs")
      content=nqa.read(name)
      nqa.write(content,adress)
    elif i=="$run":
      run(name)
    elif i=="$delay":
      print("How many milliseconds?")
      delta=get("nqs")
      sleep(int(delta))
    elif i=="$end":
      try:
        nqa.delete(name)
      except:
        pass
      print("Developer Console stopped running")
      return "done"
    elif i[0]=="$":
      print("Error: NQS could not found the command \""+i+" \"")
    else:
    	nqa.append(i+"\n",name)