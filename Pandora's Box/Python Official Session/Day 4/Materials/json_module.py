import json

'''
{
    "emp1": {
        "name": "Tris",
        "location": "Chennai",
        "team": "Development"
    }
}
'''

emp = {
    "emp1": {
        "name": "Tris",
        "location": "Chennai",
        "team": "Development"
    }
}
print('-' * 50)
print('Employee ->', emp, '->', type(emp))
print('-' * 50)

# Convert to JSON Object
json_obj = json.dumps(emp)
print(json_obj, '->', type(json_obj))

print('-' * 50)

# Convert to Dictionary
json_dict = json.loads(json_obj)
print(json_dict, '->', type(json_dict))

print('-' * 50)

# Retrieve emp1
print('emp1 ->', emp['emp1'])
print('Name of emp1 ->', emp['emp1']['name'])

print('-' * 50)
