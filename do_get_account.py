import json
import grequests
from collections import defaultdict

headers = {}
races = defaultdict(dict)
api_token = 'nrdcxnhn9ejq9n8q7qzqwz3n3nc5km2v'
countries = ['en_GB','de_DE','es_ES','fr_FR','it_IT','pl_PL','pt_PT','ru_RU']
api_url_base = 'https://eu.api.battle.net' #/wow/data/character/races
s = grequests.Session()


for country in countries:

    api_url='{0}/wow/data/character/races?locale={1}&apikey={2}'.format(api_url_base,country,api_token)
    print("BEFORE")
    response = s.get(api_url, headers = headers)
    print("AFTER")
    result = json.loads(response.content)
    for item in result['races']:
        races[item['id']][country] = item['name']
    print("{0} done \n".format(country))
print(races)