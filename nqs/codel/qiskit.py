import nqs.resources.utils as utils

def settings(command: str,param):
  t=""
  if command=="host":
    t0="s=1024\nbackend=Aer.get_backend('"+param+"')\n"
    t1="job=execute(circuit, backend, shots=s)\n"
    t2="result=job.result()\n"
    t3="counts=result.get_counts(circuit)\n"
    t=t0+t1+t2+t3
  elif command=="shots":
    t="s="+param
  elif command=="hist":
    t1="graph=plot_histogram(counts)\n"
    t2="display(graph)\n"
    t=t1+t2
  elif command=="draw":
    t="circuit.draw('mpl')\n"
  elif command=="inject":
    t=param+"\n"
  return t

def quantum(gate: str,n):
  t=""
  N=utils.floor(n)
  n=str(N)
  T="circuit."
  if len(gate)==1:
    t=T+gate.lower()+"("+n+")\n"
  elif gate==".---X":
    t=T+"cx("+n+","+str(N+1)+")\n"
  elif gate=="X---.":
    t=T+"cx("+str(N+1)+","+n+")\n"
  else:
    number=""
    b=0
    for i in gate:
      if i!="c":
        number+=i
      else:
        b=1
    if b==1:
      t=T+"measure("+n+","+number+")\n"
  return t
