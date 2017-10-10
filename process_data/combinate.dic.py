import pprint

dic1 = [{'name': 'foo', 'dataA': 'abc'},
        {'name': 'bar', 'dataA': 'xyz'}]

dic2 = [{'name': 'foo', 'infoB': 12},
        {'name': 'foobar', 'infoB': 200}]

c = dic1 | dic2
 
pprint(len(c))