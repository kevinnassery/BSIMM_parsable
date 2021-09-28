import os
import json
import sys

file = open('activities.txt')
lines = file.readlines()
activities = []
for line in lines:
    fields = line.split('%')
    id = fields[1].split('.')
    practice = id[0][:-1]
    number = id[1]
    level = id[0][-1:]
    earth = fields[2]
    name = fields[3].split('] ')[1]
    description = fields[4].rstrip().lstrip()
    record = {
        'practice': practice,
        'level': level,
        'number': number,
        'earth': earth,
        'name': name,
        'description': description
    }
    activities.append(record)

# json
file = open('bsimm12.json', 'w')
json.dump(activities, file, ensure_ascii=False, indent=4)
file.close()

# pipe seperated values
tsv = f'practice|level|number|earth|name|description\n'
for x in activities:
    tsv += f'{x["practice"]}|{x["level"]}|{x["number"]}|{x["earth"]}|{x["name"]}|{x["description"]}\n'
file = open('bsimm12.psv', 'w')
file.write(tsv)
file.close()
