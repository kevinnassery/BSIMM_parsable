# provided only for reference
# there is no need to run against bsimm.com, use activities.txt or json directly
# curl -s https://www.bsimm.com/framework.html | grep "framework/" | awk '{print $3}' | grep href | awk -F= '{print $2}' | tr -d '\"%' | awk '{printf("lynx -dump -nonumbers https://www.bsimm.com%s\n",$1)}' | sh \
	| LC_ALL=C sed -n '/Level 1/,/Download BSIMM/p' \
	| grep -v --regexp="Download" | sed -e '/^$/d' \
	| awk '{ if ( substr($1,1,1) == "\[" && substr($1,length($1),1) == ":") printf("\n_record_%%%s%%%s%%%s%%",substr($1,2,length($1)-2),substr($2,1,length($2)-1),$0) ; else if (substr($0,1,1) == " ") printf("%s", $0)}' | LC_ALL=C sed -n '/_record_/,/NEVEREVERGOONNAASDF/p' \
	| tr -s ' ' | tr -d '\t' 
