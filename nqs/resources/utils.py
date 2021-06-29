import json, math

def dump(structure, file):
  json.dump(structure, file, indent=2)

def floor(f: float):
  return math.floor(f)