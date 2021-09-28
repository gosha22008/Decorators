import requests
from pprint import pprint
from task_1 import my_decorator

names = ['Hulk', 'Captain America', 'Thanos']
url = "https://superheroapi.com/api/2619421814940190/"
@my_decorator
def list_id(url, names):
    list_id = []
    for name in names:
        url_1 = url + 'search/' + name
        result = requests.get(url_1)
        id = result.json()['results'][0]['id']
        list_id.append(id)
    return list_id
@my_decorator
def list_intelligence(list_id):
    list_intelligence = []
    for id in list_id:
        res = requests.get(url + id + '/powerstats')
        intel = res.json()['intelligence']
        list_intelligence.append(int(intel))
    return list_intelligence
@my_decorator
def sort_fun(names, list_intel):
    n = 0
    my_list = []
    while n < len(names):
        my_list.append((names[n], list_intel[n]))
        n += 1
    my_list.sort(key=lambda x: x[1])
    pprint(f'Самый умный {my_list[-1][0]} с интелектом {my_list[-1][1]}')
sort_fun(names, list_intelligence(list_id(url, names)))