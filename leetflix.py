import json 
import requests
import subprocess

API_URL = "https://leetflix.haghiri75.com"

def program():
    movie_name = input("Enter a movie name (or keywords): ")
    response = requests.post(API_URL, data=json.dumps({"keyword" : movie_name}), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0', 'content-type': 'application/json'})
    response = json.loads(response.text)
    if len(response) == 0:
        return print('Nothing found!')
    index = 1
    for result in response:
        print(f'{index} : {result["title"]}')
        index += 1
    choice = int(input("Enter an index: "))
    if choice > 15:
        return print("Not in list!")
    magnet_link = response[choice - 1]['magnet']

    execution_array = """webtorrent "{}" --vlc""".format(magnet_link)
    subprocess.run(execution_array, shell=True)

while 1:
    program()
