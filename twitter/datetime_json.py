import json
import datetime
 

#Code from
#https://code-maven.com/serialize-datetime-object-as-json-in-python

d = {
   'name' : 'Foo'
}
print(json.dumps(d))   # {"name": "Foo"}
 
d['date'] = datetime.datetime.now()
 
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def datetime_handler(x):
    #https://stackoverflow.com/questions/35869985/datetime-datetime-is-not-json-serializable

    #Use ISO 8601
    #https://stackoverflow.com/questions/10286204/the-right-json-date-format
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

 
print(json.dumps(d, default = myconverter))    # {"date": "2016-04-08 11:43:36.309721", "name": "Foo"}
print(json.dumps(d, default=datetime_handler))
 
 