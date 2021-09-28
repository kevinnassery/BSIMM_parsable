import os
import json
import sys

file = open('activities.txt')
lines = file.readlines()
activities = []

# splicing in vert tables from PDF
file = open('BSIMM12-vert.txt')
vertlist = file.readlines()
file.close()
index = 0
for line in lines:
    v = vertlist[index].rstrip().split(' ')
    v.pop(0)  # removing id from this list, they are ordered the same
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
        'name': name,
        'description': description,
        'earth': earth,
        'isv': v[0],
        'fin': v[1],
        'tech': v[2],
        'cloud': v[3],
        'fintech': v[4],
        'iot': v[5],
        'healthcare': v[6],
        'insurance': v[7],
        'retail': v[8]
    }
    activities.append(record)

# json
file = open('bsimm12.json', 'w')
json.dump(activities, file, ensure_ascii=False, indent=4)
file.close()

# pipe seperated values
tsv = f'practice|level|number|earth|isv|fin|tech|cloud|fintech|iot|healthcare|insurance|retail|name|description\n'

# splicing in vert tables from PDF
file = open('BSIMM12-vert.txt')
vertlist = file.readlines()
file.close()

index = 0
for x in activities:
    v = vertlist[index].rstrip().split(' ')
    v.pop(0)
    tsv += f'{x["practice"]}|{x["level"]}|{x["number"]}|{x["earth"]}|'
    tsv += f'{x["isv"]}|{x["fin"]}|{x["tech"]}|{x["cloud"]}|{x["fintech"]}|'
    tsv += f'{x["iot"]}|{x["healthcare"]}|{x["insurance"]}|{x["retail"]}|'
    tsv += f'{x["name"]}|{x["description"]}\n'
    index += 1


file = open('bsimm12.psv', 'w')
file.write(tsv)
file.close()
