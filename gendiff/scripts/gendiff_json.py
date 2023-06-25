import json


def gendiff_json(file1, file2):
    file1 = json.load(open('files/file1.json'))
    file2 = json.load(open('files/file2.json'))

    c = {}
    for key, value in sorted(file1.items()):
        if key not in file2:
            c['- ' + key] = value
        elif value != file2[key]:
            c['- ' + key] = value
            c['+ ' + key] = file2[key]
        else:
            c[key] = value

    for key, value in sorted(file2.items()):
        if key not in file1 and key not in c:
            c['+ ' + key] = value
    return json.dumps(c, indent=4)


if __name__ == '__main__':
    gendiff_json('files/file1.json', 'files/file2.json')
