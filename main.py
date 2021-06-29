from nqs.app import developerConsole
from news.app import journalistConsole

f1="examples/circuit"
#write(f1)
#developerDisplay(f1)
#developerConsole()
#journalistConsole()

from user.index import Index
from nqs.resources.functions import Func

'''
params=["name","mob"]
actions=["print(\"I am \"+name+\" and my favourite mob is \"+mob)"]
maicra=Func("maicra",params,actions,"user/index","user/definitions")
maicra.add()

Index["maicra"]("Mario","creeper")
'''

i=Index["__init__"]()
print(i)