students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printNames(nameArr):
    for item in nameArr:
        print item['first_name'], item['last_name']

printNames(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printUsers(usersDict):
    for key,data in usersDict.iteritems():
        print key
        i = 1
        for item in data:
            print "{} - {} {} - {}".format(i, item['first_name'].upper(), item['last_name'].upper(), len(item['first_name']) + len(item['last_name']))
            i += 1

printUsers(users)
