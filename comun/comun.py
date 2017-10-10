

def datetime_handler(obj):
    #https://stackoverflow.com/questions/35869985/datetime-datetime-is-not-json-serializable

    #Use ISO 8601
    #https://stackoverflow.com/questions/10286204/the-right-json-date-format
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Unknown type")