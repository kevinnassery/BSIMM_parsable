import os
import json 
import sys
# file generated with shell 1-liner:
'''
curl -s https://www.bsimm.com/framework.html | grep "framework/" | awk '{print $3}' | grep href | awk -F= '{print $2}' | tr -d '\"%' | awk '{printf("lynx -dump -nonumbers https://www.bsimm.com%s\n",$1)}' | sh \
	| LC_ALL=C sed -n '/Level 1/,/Download BSIMM/p' \
	| grep -v --regexp="Download" | sed -e '/^$/d' \
	| awk '{ if ( substr($1,1,1) == "\[" && substr($1,length($1),1) == ":") printf("\n_record_%%%s%%%s%%%s%%",substr($1,2,length($1)-2),substr($2,1,length($2)-1),$0) ; else if (substr($0,1,1) == " ") printf("%s", $0)}' | LC_ALL=C sed -n '/_record_/,/NEVEREVERGOONNAASDF/p' \
	| tr -s ' ' | tr -d '\t' 
'''

print(os.getcwd())
file = open('bsimm-tools/activities.txt')
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

print(json.dump(activities,sys.stdout,indent=4))

