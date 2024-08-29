import os
import json
import sys

file = open('activities.txt')
lines = file.readlines()
activities = []


def build_vert(filename='BSIMM12-vert.txt'):
    fileh = open(filename)
    rows = fileh.readlines()
    fileh.close()
    results = []
    for row in rows:
        fields = row.rstrip().split(' ')
        result = {
            'id': fields[0][1:-1],
            'isv': fields[1],
            'fin': fields[2],
            'tech': fields[3],
            'cloud': fields[4],
            'fintech': fields[5],
            'iot': fields[6],
            'healthcare': fields[7],
            'insurance': fields[8],
            'retail': fields[9]
        }
        print(result)
        results.append(result)
    return results


def vlookup(id):
    print(id)
    db = build_vert()
    for record in db:
        if (record["id"] == id):
            return record
    return None


for line in lines:
    fields = line.split('%')
    v = vlookup(fields[1])
    # print(v)
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
        'isv': v['isv'],
        'fin': v['fin'],
        'tech': v['tech'],
        'cloud': v['cloud'],
        'fintech': v['fintech'],
        'iot': v['iot'],
        'healthcare': v['healthcare'],
        'insurance': v['insurance'],
        'retail': v['retail']
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
