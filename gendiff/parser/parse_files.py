import json
import yaml

MODIFIED = 'modified'
ADDED = 'added'
NESTED = 'nested'
DELETED = 'deleted'
UNCHANGED = 'unchanged'


def load_json_file(file_path):
    with open(file_path) as file:
        return json.load(file)


def load_yaml_file(file_path):
    with open(file_path) as file:
        return yaml.safe_load(file)


def get_file_extension(file_path):
    return file_path.split('.')[-1]


def generate_diff(dict1, dict2):
    result = []

    keys = dict1.keys() | dict2.keys()

    for key in sorted(keys):
        if (key in dict1) and (key not in dict2):
            result.append(dict(key=key,
                               value=dict1[key],
                               type='deleted'))

        elif (key in dict2) and (key not in dict1):
            result.append(dict(key=key,
                               value=dict2[key],
                               type='added'))

        elif (key in dict1) and (key in dict2):
            dict2_value = dict2[key]
            dict1_value = dict1[key]

            if isinstance(dict1_value, dict) and isinstance(dict2_value, dict):
                result.append(dict(key=key,
                                   type='nested',
                                   value=generate_diff(dict1_value, dict2_value)))

            elif dict2_value == dict1_value:
                result.append(dict(key=key,
                                   value=dict1_value,
                                   type='unchanged'))

            elif dict1_value != dict2_value:
                result.append(dict(key=key,
                                   value=(dict1_value, dict2_value),
                                   type='changed'))

    return result


def format_added(key, value, depth=1):
    return f"{get_space(4 * depth - 2)}+ {key}: {value}"


def format_removed(key, value, depth=1):
    return f"{get_space(4 * depth - 2)}- {key}: {value}"


def format_unchanged(key, value, depth=1):
    return f"{get_space(4 * depth)}{key}: {value}"


def get_space(num):
    return num * " "


def resolve_value(value, depth=0):
    if value is None:
        return "null"
    elif isinstance(value, dict):
        return resolve_nested(value, depth)
    return value


def resolve_nested(dict_value, depth=0):
    result = ['{']
    depth += 1
    for key, value in dict_value.items():
        if isinstance(value, dict):
            result.append(format_unchanged(key, resolve_nested(value, depth), depth))
        else:
            result.append(format_unchanged(key, resolve_value(value), depth))

    result.append(f'{get_space(4*(depth-1))}}}')

    return '\n'.join(result)


def format_stylish(diff, depth=0):
    result = ['{']
    depth += 1
    for el in diff:
        if el['type'] == 'unchanged':
            result.append(
              format_unchanged(el['key'],
                               resolve_value(el['value'], depth),
                               depth))

        elif el['type'] == 'changed':
            result.append(
              format_removed(el['key'],
                           resolve_value(el['value'][0], depth),
                           depth))
            result.append(
              format_added(el['key'],
                             resolve_value(el['value'][1], depth),
                                        depth))

        elif el['type'] == 'nested':
            result.append(
              format_unchanged(el['key'],
                              format_stylish(el['value'], depth), depth))
        elif el['type'] == 'added':
            result.append(
              format_added(el['key'],
                           resolve_value(el['value'], depth),
                           depth))

        elif el['type'] == 'deleted':
            result.append(
              format_removed(el['key'],
                           resolve_value(el['value'], depth),
                           depth))

    result.append(f'{get_space(4*(depth-1))}}}')

    return '\n'.join(result)


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

    differences = format_stylish(generate_diff(file1, file2))

    return differences


if __name__ == '__main__':
    file1 = 'file1.json'
    file2 = 'file2.yaml'
    result = parse_files(file1, file2)
