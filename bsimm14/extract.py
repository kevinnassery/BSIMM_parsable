import os
from json import dumps

def vert_pops():
  return {
    'cloud': 31,
    'financial': 41,
    'fintech': 12,
    'healthcare': 10,
    'insurance': 15,
    'iot': 21,
    'isv': 33,
    'tech': 39,
  }
  
def id_split(id):
  left,right = id.split(".")
  number = int(right)
  level = left[-1]
  practice = left[:-1]
  return practice, level, number

def pcoef(ipercent):
  percentstring = str(ipercent)[:-1]
  percent = int(percentstring)
  fraction = percent / 100
  return fraction

def get_percs():
  percfile = open("verts.txt", "r")
  perclines = percfile.readlines()
  percfile.close()
  percs = []

  for line in perclines:
    entry = {}
    fields = line.rstrip().split(" ")
    entry["practice"], entry["level"], entry["number"] = id_split(fields[0][1:-1])
    entry['cloud'] = int(pcoef(fields[1]) * vertpops['cloud'])
    entry['financial'] = int(pcoef(fields[2]) * vertpops['financial'])
    entry['fintech'] = int(pcoef(fields[3]) * vertpops['fintech'])
    entry['healthcare'] = int(pcoef(fields[4]) * vertpops['healthcare'])
    entry['insurance'] = int(pcoef(fields[5]) * vertpops['insurance'])
    entry['iot'] = int(pcoef(fields[6]) * vertpops['iot'])
    entry['isv'] = int(pcoef(fields[7]) * vertpops['isv'])
    entry['tech'] = int(pcoef(fields[8]) * vertpops['tech'])
    percs.append(entry)
  return percs

def lookup_percs(practice, level, number):
  for perc in get_percs():
    if perc["practice"] == practice and perc["level"] == level and perc["number"] == number:
      return perc
  return None

def decode_tag(inputact):
  act = {}
  fields = inputact.split("]")
  act["name"] =  fields[1].lstrip().rstrip()
  tag = fields[0][1:]
  act["id"] = tag.split(":")[0]
  act["earth"] = int(tag.split(":")[1].lstrip().rstrip())
  act["level"] = act["id"].split(".")[0][-1]
  act["number"] = act["id"].split(".")[1]
  act["practice"] = act["id"].split(act["level"]  + ".")[0]
  act["cloud"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["cloud"]
  act["financial"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["financial"]
  act["fintech"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["fintech"]
  act["healthcare"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["healthcare"]
  act["insurance"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["insurance"]
  act["iot"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["iot"]
  act["isv"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["isv"]
  act["tech"] = lookup_percs(act["practice"], act["level"], int(act["number"]))["tech"]
  return act

def get_acts():
  file = open("activities.txt", "r")
  lines = file.readlines()
  file.close()
  acts = []
  lindex = 0
  for line in lines:
    if line[0] == "[":
      x = decode_tag(line)
      x["description"] = lines[lindex + 1].rstrip()
      acts.append(x)
    lindex+=1

