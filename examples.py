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


def getPRs(db):
    result = []
    for record in db:
        if (record['practice'] not in result):
            result.append(record['practice'])
    return result


def get_by_pr(db, pr):
    result = []
    for record in db:
        if (record['practice'] == pr):
            result.append(record)
    return result


def percent_normalize(alist, vertical='earth', firmCount=128):
    total = 0
    for activity in alist:
        total += int(activity[vertical]) / firmCount
    pnormal = total / len(alist) * 100
    return pnormal


# decode id into parts e.g.:CMVM1.1 -> ['CMVM','1','1']
def id_decode(id):
    foo = id.split('.')
    pr = foo[0][:-1]
    lev = foo[0][-1:]
    num = foo[1]
    return [pr, lev, num]


# get an array of dicts that contain percent normalized activities per pr
def get_all_pn(db, vert='earth'):
    results = []
    for pr in getPRs(SSF):
        pn = percent_normalize(get_by_pr(db, pr), vert)
        result = {
            'practice': pr,
            'vertical': vert,
            'pn': pn
        }
        results.append(result)
    return results


SSF = file_to_bsimm('bsimm12.json')

print("Example Activity Lookup:")
print(f'\t{lookup(SSF, id_decode("CR1.4"))}\n')
print("Example Practice List:")
print(f'\t{getPRs(SSF)}\n')
print("Example Percent Normalized (earth):")
for pr in get_all_pn(SSF):
    print(f'\t{pr["practice"]}:{pr["pn"]:.2f}')
