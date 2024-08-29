from json import load
from jinja2 import Environment, FileSystemLoader, select_autoescape
from sys import path as syspath
from os import path as ospath
from extract import vert_pops as vertpops

cwd = ospath.dirname(__file__)
templatedir = f'{cwd}/templates'

env = Environment(
    loader=FileSystemLoader(templatedir),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True
)

def md_link_from_act(act):
    link = "#"
    link += act["practice"].lower()
    link += act["level"]
    link += act["number"] + "-"
    link += act["name"].lower().replace(" ", "-").replace(".", "")
    return link

def get_occ_from_act(act):
    vp = vertpops()
    occurance = {}
    for key,value in vp.items():
        denominator = value
        numerator = act[key]
        incidence = int(numerator / denominator * 100)
        incstring = str(incidence) + "%"
        occurance[key] = incstring
    return occurance

bsimm14 = load(open("bsimm14.json", "r"))

template = env.get_template('appendix.j2')
output = template.render(bsimmdata=bsimm14,mdl=md_link_from_act,occ=get_occ_from_act)
print(output)
