import time
from concurrent.futures.thread import ThreadPoolExecutor
import requests
import json

trs = []
all_data = []


def collect(i):
    url = f"https://jsonplaceholder.typicode.com/posts/{i}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    all_data.append(data)

print(time.perf_counter())

with ThreadPoolExecutor(max_workers=20) as executor:
    for i in range(1,78):
        thread = executor.submit(collect,i)
        trs.append(thread)

with open('data.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)

print(time.perf_counter())



