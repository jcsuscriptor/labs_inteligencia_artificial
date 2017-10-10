import requests

def exist(url):
    
    try:
        request = requests.get(url)
        if request.status_code == 200:
            print('Web site exists : ' + url)
        else:
            print('Web site does not exist' + url) 
    except Exception as ex:
        print('Problem: '+ url)
        print(type(ex))
        print(ex)

exist('http://www.example.com')        
exist("http://t.co/KTvOnJjDck") 