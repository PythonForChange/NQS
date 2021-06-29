from nqs.core.reader import settings
from nqs.core.quantum import quantum
from nqs.resources.extensions import nqa
from nqs.resources.parser import Parser

def compile(name: str):
  lines=nqa.getLines(name)
  T=""
  m=0
  T+="from qiskit import QuantumCircuit, execute, Aer\n"
  T+="from qiskit.visualization import plot_histogram,display\n"
  s=0
  command=""
  param=""
  Q=0
  gate=""
  gatecount=0
  qdef=0
  p=Parser()
  count=0
  for k in lines:
    for i in k:
      if  p.isDeny(i):
        if m==2:
          m=0
        else:
          m=2
      elif s==1: #settings mode on
        if i!=" ":
          command+=i
        else:
          s=2
      elif s==2:
        if i!="\t" and i!="\n":
          param+=i
        else:
          T+=settings(command,param)
          command=""
          param=""
          s=0
      elif i=="$":
        s=1
      elif qdef==1:
        if i=="q":
          Q+=1
        elif i=="\n":
          qdef=2
          T+="circuit=QuantumCircuit("+str(Q)+","+str(Q)+")\n"
      elif qdef==2:
        if i!="\n" and i!=" ":
          gate+=i
        elif i==" ":
          gatecount+=0.5
          T+=quantum(gate,gatecount)
          gate=""
        else:
          T+=quantum(gate,gatecount)
          gate=""
          gatecount=0
      elif i=="q":
        qdef=1
        Q+=1
  return T