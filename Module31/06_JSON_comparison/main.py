import json


def json_comparison(old_dict: dict, new_dict: dict, diff_dict: dict =dict()) -> dict:

    for key, value in old_dict.items():
        if value != new_dict[key]:
            if isinstance(value, dict):
                result = json_comparison(value, new_dict[key])
                diff_dict.update(result)
            else:
                diff_dict[key] = new_dict[key]

    return diff_dict


with open('json_old.json', 'r') as old_file:
    old_data = json.load(old_file)

with open('json_new.json', 'r') as new_file:
    new_data = json.load(new_file)

updated_values = json_comparison(old_data, new_data)

diff_list = ["services", "staff", "datetime"]
result = {
    key: updated_values[key]
    for key in diff_list
    if key in updated_values
}
print(result)

with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result, result_file, indent=4)

