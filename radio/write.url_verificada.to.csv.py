
import json, csv


def getData():
    with open('radio_url_verificada.json') as data_file:    
        data = json.load(data_file)

    return data   

def getItem(item):
    data = {} 
    data['direccion'] = item['Direccion']
  
    if 'twiiterInfo' in item and item['twiiterInfo'] is not None:
        if 'location' in item['twiiterInfo']:
            data['location'] = item['twiiterInfo']['location']
        else:
            data['location'] = ''
    else:
        data['location'] = ''
    
    if item['url_verified']['exist'] or item['url_verified']['exist_url_twitter']:
        data['titulo'] = item['titulo']
        if item['url_verified']['exist']:               
            data['url'] = item['Sitio Web']
        else:
                data['url'] = item['url_verified']['url_twitter']
        return data
    else:
        return None

data = getData()

#not writter line blank
#https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
with open("radio_url_verificada.json.csv", "w+",newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    count = 0
    for item in data:
        #if count == 0:
        #     header = item.keys()
        #     csv_writer.writerow(header)
        #     count += 1
        data = getItem(item)
        if data is not None:
            csv_writer.writerow([data['titulo'],data['url'],data['direccion'],data['location']])
           #csv_writer.writerow({'post':'jc','otro':'foo'})
           #csv_writer.writerow(['SNo', 'States', 'Dist', 'Population'])

        