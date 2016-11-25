import json
import re

import requests
import scraperwiki


url = 'https://www.nwspk.com/graphs/full'
r = requests.get(url)

members = json.loads(re.search(r'"nodes": *(\[.*?\])', r.text).group(1))

for member in members:
    data = dict(member['meta'].items() + [('id', member['id'],)])
    scraperwiki.sqlite.save(unique_keys=['id'], data=data)
