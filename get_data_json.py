import os

import pandas as pd
import requests
import wget
from bs4 import BeautifulSoup

url = "https://datasets.imdbws.com/"
raw_data_location = "data/raw"
json_data_location = "data/json"
num_of_records = 1000000


def get_datasets(url, raw_data_location, json_data_location, num_of_records):
    # create folders
    os.makedirs(raw_data_location, exist_ok=True)
    os.makedirs(json_data_location, exist_ok=True)

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')
             if "datasets" in link.get('href')]

    for link in links:
        wget.download(link, out=raw_data_location)

    # Convert to Json
    for filename in os.listdir(raw_data_location):
        df = pd.read_csv(f"{raw_data_location}/{filename}",
                         sep='\t', compression="gzip", low_memory=False)
        filename = filename.replace(".", "_")
        df = df.head(num_of_records)
        df.to_json(f"{json_data_location}/{filename}.json", orient="records")


get_datasets(url, raw_data_location, json_data_location, num_of_records)
