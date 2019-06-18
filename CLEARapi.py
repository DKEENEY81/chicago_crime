#!/usr/local/bin/python3

from requests import get
import pandas as pd
import json

url = "https://data.cityofchicago.org/resource/crimes.json"
response = get(url, headers={"X-App-Token":"eQexwCiZsieQyjfCAdnzDBlUs"})

#print(response.status_code)
#print(response.headers['content-type'])


def get_info():
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

data = get_info()

Crime = pd.DataFrame(data)


