import json
from pprint import pprint

with open('artistas.json') as data_file:    
    data = json.load(data_file)
    #for artista in data:
    #    print('Name: ' + artista['nombre'])
    #    print('url: ' + artista['url'])
    #    print('')
    
    index = 0
    while index < 5 and index < len(data):
        print(index, data[index])
        index += 1


#pprint(data)