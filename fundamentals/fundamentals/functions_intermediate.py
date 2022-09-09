x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print("change x to 15:", x)
students[0]['last_name']="Bryant"
print("change students last name to bryant:", students)
sports_directory['soccer'][0]='Andres'
print("change sports directory soccer to andres:", sports_directory)
z[0]['y']=30
print("change z to 30:", z)


students1 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterateDictionary(list):
    for i in range (0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
            print(output)

iterateDictionary(students1)

def iterateDictionary2(key_name,list):
    for i in range (0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)


iterateDictionary2('first_name',students1)
iterateDictionary2('last_name',students1)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dict):
    for key,val in dict.items():
        print("----------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)