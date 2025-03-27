from hashlib import new
import os
from prefect import flow, task
import tomllib
import requests
# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up two levels to reach the project root
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

# Construct the full path to the TOML file
toml_path = os.path.join(project_root, "pyproject.toml")

with open(toml_path, "rb") as f:
    config = tomllib.load(f)

@task
def extract(locations):
    apikey = config["api"]["apikey"]

    weatherData = list()
    for i in locations:
        url = "https://api.weatherapi.com/v1/current.json?key={0!s}&q={1!s}&aqi=yes".format(apikey, i)
        response = requests.get(url)
        weatherData.append(response.json())
        #print(response.json())
        #print()
    return weatherData


@task
def transform(data):
    for i in data:
        print(i)
        print('NEXT!!')
    return data


@task
def load(data):
    return 

@flow
def etl_pipeline():
    data = extract({'Amsterdam', 'London', 'Berlin', 'Madagaskar'})
    transform(data)
    ##load(data)

if __name__ == "__main__":
    etl_pipeline()
