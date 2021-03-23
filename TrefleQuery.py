
import requests
import asyncio
from urllib.error import HTTPError

class PlantSpecies:
    def __init__(self, name):
        self.name = name

class TrefleQuery:
    def __init__(self):
        self.token = "kKyidyz_nnAAIvqcgDbfTjGgYU0W6l3Uh-7VcqzaPGY" # this should be hidden in a config file
        self.base_url = "https://trefle.io/api/v1/"

    def species_search(self, species):
        search_url = self.base_url + "species/search"
        params = {'limit': 1, 'q': species, 'token':self.token}
        print('Starting Request: ', species)
        r = requests.get(search_url, params=params)
        print('Collecting Request: ', species)
        if r.status_code != 200:
            raise HTTPError(code=r.status_code, reason=r.text)
        search_results = [item['common_name'] for item in r.json()['data']]
        print(search_results)
        if search_results:
            return PlantSpecies(search_results[0] or 'Missing Name')
        else:
            return PlantSpecies('Unknown ' + species)
        
    
