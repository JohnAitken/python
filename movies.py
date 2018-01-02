import requests
from pprint import pprint
r = requests.get('http://server.com/api/2/....')
pprint(r.json())
