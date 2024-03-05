import json

# Read the original JSON file
with open('filmes.json', 'r') as f:
    original_data = f.readlines()

# Parse each line as JSON and store in a list
json_objects = [json.loads(line.strip()) for line in original_data]

cast = set()
genres = set()

for obj in json_objects:
    obj['id'] = obj['_id']['$oid']
    del obj['_id']
    for actor in obj['cast']:
        cast.add(actor)
    if 'genres' in obj:
        for genre in obj['genres']:
            genres.add(genre)
                

genresDict = {}
genre_id = 1
for genre in sorted(genres):
    genresDict[genre] = {
        'id': genre_id,
        'genre': genre
    }
    genre_id += 1

castDict = {}
cast_id = 1
for actor in cast:
    castDict[actor] = {
        'id': cast_id,
        'name': actor
    }
    cast_id += 1


modified_data = {"filmes": json_objects}
cast_data = {"atores": list(castDict.values())}
genres_data = {"generos": list(genresDict.values())}

combined_data = {**modified_data, **cast_data, **genres_data}

# Write the modified data to a new JSON file
with open('filmesFix.json', 'w') as f:
    json.dump(combined_data, f, indent=2)