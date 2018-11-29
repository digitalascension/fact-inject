import json

# Read the JSON file file and convert to a dictionary.
def parse_input(json_file):
    input_json = None
    input_obj = None
    # Read the json file into memory.
    try:
        input_json = open(json_file, 'r').read()
    except IOError:
        print('Error: Could not read {}.'.format(json_file))
        exit(code=1)

    try:
        input_obj = json.loads(input_json)
    except json.JSONDecodeError as e:
        print('Error: Could not decode the supplied JSON.')
        print('Message: {}'.format(e))
        exit(code=1)
    return input_obj

# Convert each key value pair to a fact.
def convert_to_fact(object):
    facts = {}
    for item in object.keys():
        facts['FACTER_{}'.format(item)] = object[item]
    return facts