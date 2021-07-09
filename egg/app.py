#Imports
from egg.resources.console import get
from egg.resources.extensions import py
from egg.resources.constants import *
from nqs.developer.app import developerConsole
from news.app import journalistConsole

def eggConsole(condition: bool = True):
  print(white+"Egg Console is now running")
  logged=0
  while condition:
    i=get("egg")
    if i=="$nqs":
      developerConsole()
    elif i=="$new":
      journalistConsole()
    elif i=="$login":
      print(white+"Username:")
      j=get("egg")
      try:
        from user.private import username,password
        if j==username:
          print(white+"Password:")
          k=get("egg")
          if k==password:
            logged=1
            print(white+"Done") 
      except:
        pass
    elif i=="$register":
      try:
        print(white+"Username:")
        j=get("egg")
        print(white+"Password:")
        k=get("egg")
        py.write("user/private","username,password=\"username\",\"password\"")
        print(white+"Done")
      except:
        pass 
    elif i=="$end":
      print(white+"Egg Console stopped running")
      return "done"
    else:
    	pass
		