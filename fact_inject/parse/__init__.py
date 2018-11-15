import json

# Read the JSON file file and convert to a dictionary.
def parse_input(json_file):
    try:
        input_json = open(json_file, 'r').read()
        # Convert the json to a dictionary.
        input_obj = json.loads(input_json)
        return input_obj
    except IOError:
        print('Error: Could not read {}.'.format(json_file))
        exit(code=1)

# Convert each key value pair to a fact.
def convert_to_fact(object):
    facts = {}
    for item in object.keys():
        facts['FACTER_{}'.format(item)] = object[item]
    return facts