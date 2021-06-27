#Imports
from news.news import New
from news.config import files,year
from nqs.resources.console import get

def journalistConsole(condition: bool = True):
  print("Journalist Console is now running")
  while condition:
    print("Title:")
    title=get("new")
    print("Day:")
    day=int(get("new"))
    print("Month:")
    month=int(get("new"))
    new=New(title,day,month,year,files)
    print("Tags:")
    tagsbycommas=get("new")
    new.tags=tagsbycommas.split(", ")
    print("Content:")
    content=""
    while True:
      i=get("new")
      if i=="$save":
        new.text=content
        new.add()
        break
      elif i[0]=="$":
        print("Error: NQS could not found the command \""+i+" \"")
      else:
        content+=i+"\n"
    print("Write $end to close the console")
    print("Press enter key to write other new")
    command=get("new")
    if command=="$end":
      print("Journalist Console stopped running")
      return "done"
		