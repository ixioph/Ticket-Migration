from encodings import utf_8
import json

data = []
with open("/Users/avorobcalo/Downloads/mystuff/Python/Ticket-Migration-main/src/test.json") as jsonFile:
    s = jsonFile.read()
    data = json.loads(s)
print(data)