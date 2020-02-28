import csv
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    dictonary = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
    writer = csv.DictWriter(f, dictonary, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user) 
         