import json


def gendiff_json(file1_path, file2_path):
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))

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
    file1 = 'file1.json'
    file2 = 'file2.json'
    result = gendiff_json(file1, file2)
    print(result)
