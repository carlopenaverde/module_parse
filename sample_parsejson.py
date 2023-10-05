import json

x = '{"name":"Penaverde", "age":"21", "city":"San Mateo"}'

y = json.loads(x)

print ("The output of the json file is", y)
print ("Name", y["name"])
print ("age", y["age"])
print ("city", y["city"])
