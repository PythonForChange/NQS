from nqs import write, run
from egg import py, sleep, eggConsole, install

f="example2"
#eggConsole()
#run(f)
#write(f)

from github_com.PythonForChange import covidplot
install("matplotlib")
c=covidplot.CovidData()
c.plot("casos")