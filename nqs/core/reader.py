from nqs.core.functions import Func,clear
from nqs.resources.console import sleep
from user.config import index, definitions

stdCommands=[
  "host",
  "shots",
  "hist",
  "draw",
  "inject",
  "function",
  "clear",
  "delay"
]

def settings(command: str,param):
  t=""
  if command=="host":
    t="s=1024\nbackend=Aer.get_backend('"+param+"')\n"
    t+="job=execute(circuit, backend, shots=s)\n"
    t+="result=job.result()\n"
    t+="counts=result.get_counts(circuit)\n"
  elif command=="shots":
    t="s="+param
  elif command=="hist":
    t="graph=plot_histogram(counts)\n"
    t+="display(graph)\n"
  elif command=="draw":
    t="circuit.draw('mpl')\n"
  elif command=="inject":
    t=param+"\n"
  elif command=="function":
    p=Parameter(param)
    f=Func(p.name,p.params,p.actions,index,definitions)
    f.add()
  elif command=="clear":
    clear(param)
  elif command=="delay":
    sleep(int(param))
  return t

class Parameter():
  def __init__(self,param: str):
    arr=param.split("|")
    self.name=arr[0]
    paramsBeforeSplit=arr[1]
    self.params=paramsBeforeSplit.split(",")
    actionsBeforeSplit=arr[2]
    self.actions=actionsBeforeSplit.split(",")
