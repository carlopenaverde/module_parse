import json
with open('sample.json', 'r') as json_file:
    json_data = json.load(json_file)
    print (json_data)
    print (json.dumps(json_data,indent=4))

    Courses = []
    for cert in json_data['certifications']:
        for course in cert['courses']:
            Courses.append(course)

    print ("Course:", Courses)

    Name = []
    for name in json_data['certifications']:
        for names in name['courses']:
            names.append(name)

    print ("Course:", Name)
