# Dictionary to JSON conversion

import json

d={'client_name':'company A'}
print(d)
print(type(d))
print("converting dict to JSON")
json_data=json.dumps(d)#dict->JSON
print(json_data)
print(type(json_data))

print("converting JSON to dict")
dict_convert=json.loads(json_data)#JSON->dict
print(dict_convert)
print(type(dict_convert))
