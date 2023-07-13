import json
import yaml


def load_json_file(file_path):
    with open(file_path) as file:
        return json.load(file)


def load_yaml_file(file_path):
    with open(file_path) as file:
        return yaml.safe_load(file)


def get_file_extension(file_path):
    return file_path.split('.')[-1]


def compare_files(file1, file2):
    differences = {}
    for key, value in sorted(file1.items()):
        if key not in file2:
            differences['- ' + key] = value
        elif value != file2[key]:
            differences['- ' + key] = value
            differences['+ ' + key] = file2[key]
        else:
            differences[key] = value

    for key, value in sorted(file2.items()):
        if key not in file1 and key not in differences:
            differences['+ ' + key] = value

    return differences


def parse_files(file1_path, file2_path):
    file1_extension = get_file_extension(file1_path)
    file2_extension = get_file_extension(file2_path)

    if file1_extension == 'json':
        file1 = load_json_file(file1_path)
    elif file1_extension == 'yaml' or file1_extension == 'yml':
        file1 = load_yaml_file(file1_path)
    else:
        raise ValueError(f"Unsupported file format: {file1_extension}")

    if file2_extension == 'json':
        file2 = load_json_file(file2_path)
    elif file2_extension == 'yaml' or file2_extension == 'yml':
        file2 = load_yaml_file(file2_path)
    else:
        raise ValueError(f"Unsupported file format: {file2_extension}")

    differences = compare_files(file1, file2)

    if file1_extension == 'json' and file2_extension == 'json':
        return json.dumps(differences, indent=4)
    else:
        return json.dumps(differences, indent=4)


if __name__ == '__main__':
    file1 = 'file1.json'
    file2 = 'file2.yaml'
    result = parse_files(file1, file2)
    print(result)
