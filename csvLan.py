import csv
from os import read

# {"en": {"{key}": "{content}"}, "ja": {"{key}": "{content}"}}
with open('lan.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    dict = {}
    for name in reader.fieldnames:
        if name == 'key':
            continue
        dict[name] = {}

    for row in reader:
        for key in dict.keys():
            dict[key][row['key']] = row[key]

    list = []
    for key in dict.keys():
        list.append(key)
        list.append('\n')
        items = dict[key]
        for item in items:
            s = '"{key}" = "{content}";'
            list.append(s.format(key=item, content=items[item]))
            list.append('\n')
        list.append('-------')
        list.append('\n\n')

    # content = ''.join(str(s) for s in list)
    # print(content)

    with open('output', 'w') as file:
        file.write(''.join(str(s) for s in list))
        file.close()
        pass
    pass
