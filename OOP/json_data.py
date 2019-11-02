import json
'''
people_string = '{'people':[{'name': 'John K', 'phone': '0701000000', 'emails': ['john1@bogusemail.com', 'johnk@work-paceemail.com'], 'has_license': 'false'}, {'name': 'Jane D', 'phone': '0702000000', 'email': 'null', 'has_license': 'true'}]}'

data = json.loads(people_string)
print(data)
'''

'''Convert from JSON to Python:'''
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

'''Convert from Python to JSON:'''
import json

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x ,sort_keys=True)

# the result is a JSON string:
print(y)

#Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

#Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))

#Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
