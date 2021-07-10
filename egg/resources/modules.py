import pip

def install(name: str):
    pip.main(['install', name])
    return "Done"