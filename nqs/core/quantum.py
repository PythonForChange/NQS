import nqs.resources.utils as utils

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
