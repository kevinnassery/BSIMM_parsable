import json


# takes JSON and builds a list of dicts that represent activities
def file_to_bsimm(filename):
    file = open(filename)
    bsimm_json = json.load(file)
    return bsimm_json


# search a list of activity by id and return the first match
def lookup(db, query):
    for record in db:
        if (record['practice'] == query[0]
                and record['level'] == query[1]
                and record['number'] == query[2]):
            return record
    return None


# decode id into parts e.g.:CMVM1.1 -> ['CMVM','1','1']
def id_decode(id):
    foo = id.split('.')
    pr = foo[0][:-1]
    lev = foo[0][-1:]
    num = foo[1]
    return [pr, lev, num]


SSF = file_to_bsimm('bsimm12.json')
print(lookup(SSF, id_decode('CR1.4')))
