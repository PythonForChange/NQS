from nqs.developer.write import write
from nqs.resources.extensions import py

def run(name: str):
    write(name)
    py.execute(name)