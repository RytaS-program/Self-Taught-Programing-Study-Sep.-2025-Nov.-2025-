import re

t="The ghost that says boo haunts the loo"
found=re.findall("boo" and "loo",t)
for match in found:
    print(match)

import re

t="The ghost that says boo haunts the loo"
found=re.findall("boo|loo",t)
for match in found:
    print(match)

import re

match = re.findall(".oo", "The ghost that says boo haunts the loo.")
print(match)
