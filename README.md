# BSIMM 12 Parseable Outputs

This is a small project to provide machine parseable BSIMM (Building Security in Maturity Model) version 12 framework data (in JSON format).

[Here](bsimm12.py) is the tool I used to parse BSIMMv12 SSF data from [bsimm.com](http://www.bsimm.com).

[Here](https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf) is the BSIMM12 foundations document that contains the vertical tables. These are annoying to copy & paste (at least via my PDF reader). I double checked my work including running the two tests outlined in vert-check.py.  Things seem to line up currently.

| file | descr | 
|------|--------|
| bsimm12.py   | This parses the data into JSON. |
| bsimm12.json | This is the JSON representation.| 
| bsimm12.psv  | This is a Pipe delimited file (suitable for excel import)|
| examples.py | Demonstrates JSON import, some example ways to interact|

## BSIMM12 Licensing

The project is operated by [Synopsys](http://www.synopsys.com). The BSIMMv12 was authored by Sammy Migues, Eli Erlikhman, Jacob Ewers, and Kevin Nassery(me).

I am no longer an employee of Synopsys, and this project contains no work product developed under my previous employment with Synopsys.

## BSIMM12 Parseable Licensing 

BSIMMv12 is relased under [CCL 3.0](https://creativecommons.org/licenses/by-sa/3.0/) Open Source License. Please review this before using as this project is similarly relased under [CCL 3.0](https://creativecommons.org/licenses/by-sa/3.0/) (ShareAlike).

