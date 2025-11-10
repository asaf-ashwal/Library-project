import json
with open ("DB.json","r") as file:
    data = json.load(file)
    print(data['data'])