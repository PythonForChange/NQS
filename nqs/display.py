from nqs.execute import run
from nqs.core import compile
from nqs.resources.extensions import nqa
from nqs.resources.console import display

def developerDisplay(name: str):
    content=nqa.read(name)
    display(content)

def developerConsole(condition: bool = True):
	print("Developer Console is now running")
	while condition:
		i=input("$nqs> ")
		name="temp_compile"
		if i=="$display":
			content=nqa.read(name)
			print(content)
		elif i=="$compile":
			compile(name)
		elif i=="$save":
			adress=input("Save as:")
			content=nqa.read(name)
			nqa.write(content,adress)
		elif i=="$run":
			run(name)
		elif i=="$end":
			nqa.delete(name)
			print("Developer Console stopped running")
			return "done"
		elif i[0]=="$":
			print("Error: NQS could not found the command \""+i+" \"")
		else:
			nqa.append(i+"\n",name)