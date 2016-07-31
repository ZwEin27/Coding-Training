import re

text = "SELECT ?business  (count(?ad) AS ?count)(group_concat(?ad;separator=',') AS ?ads)"

re_select_variables = re.compile(r'[\{\(](?:\(.*?\)|[\s\w!\"#\$%&()\*+\,-\./:;<=>\?@[\]\^_`{|}~])+?[\}\)]')

variable_fileds = re_select_variables.findall(text)
for variable_filed in variable_fileds:
    text = text.replace(variable_filed, '').strip()
variable_fileds += text.split(' ')
print variable_fileds

#
# # text = "ORDER BY DESC(?iwe)"
# # text = "qpr:image_with_phone ?iwp"
# text = "ORDER BY ?posting_date"
#
# # re_ = re.compile(r'(?:^|\s|\b|(?<=\()])\?[a-zA-Z]+(?=\))')
# re_ = re.compile(r'(?<=[\(\b\s])\?[_a-zA-Z]+(?=[\)\b\s\Z]|$)')
#
# print re_.findall(text)


#######################

# text = "?ad a qpr:Ad ; qpr:location 'Vermont' ; qpr: business_type ?bt . FILTER(?bt = 'Spa' || ?bt = 'Massage Parlor') ?ad qpr:services 'sex' . OPTIONAL { ?ad qpr:business_name ?business_name} OPTIONAL { ?ad qpr:physical_address ?physical_address } BIND( IF(BOUND(?business_name) && BOUND(?physical_address), CONCAT(?business_name, \",\", ?physical_address), IF(BOUND(?business_name), ?business_name, ?physical_address)) AS ?business)"

# text = "PREFIX qpr: <http://istresearch.com/qpr> SELECT ?cluster ?ad WHERE {   ?cluster a qpr:cluster ; qpr:seed '6476877096' ; qpr:ad ?ad . OPTIONAL { ?ad qpr:image_with_phone ?iwp } OPTIONAL { ?ad qpr:image_with_email ?iwe } FILTER(bound(?iwp) || bound(?iwe)) }"
#
#
# SQ_INNER_KEYWORDS = ['FILTER', 'OPTIONAL', 'BIND']
# re_statement_inner_keyword = re.compile(r'(?:'+r'|'.join(SQ_INNER_KEYWORDS)+r')\s*?[\{\(](?:\(.*?\)|[\s\w!\"#\$%&()\*+\,-\./:;<=>\?@[\]\^_`{|}~])+?[\}\)]')
# re_statement_others = re.compile(r'.*?(?=;|\s\.\s)')
#
# statements = [_.strip() for _ in re_statement_inner_keyword.findall(text)]
# print statements
# for statement in statements:
#     text = text.replace(statement, '')
# statements += [_.strip() for _ in re_statement_others.findall(text) if _.strip() != '']
# # print statements
