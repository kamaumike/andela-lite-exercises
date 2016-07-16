from datetime import datetime

year = datetime.now().year

student = {'name': ['Michael', 'Kamau'],
'date_of_birth': 1990,
'phone_number': '0725033033'
}

last_name = student.get('name')

print last_name[1]
print last_name[0], last_name[1]
print student.get('phone_number')
print student.get('date_of_birth')
print year  - student.get('date_of_birth')

