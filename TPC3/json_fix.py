import json

# Read the original JSON file
with open('filmes.json', 'r') as f:
    original_data = f.readlines()

# Parse each line as JSON and store in a list
json_objects = [json.loads(line.strip()) for line in original_data]

for obj in json_objects:
    obj['id'] = obj['_id']['$oid']
    del obj['_id']

# Create a new dictionary with the key "filmes" and assign the list of JSON objects
modified_data = {"filmes": json_objects}

# Write the modified data to a new JSON file
with open('filmesFix.json', 'w') as f:
    json.dump(modified_data, f, indent=2)