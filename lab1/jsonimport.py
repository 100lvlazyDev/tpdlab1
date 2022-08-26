import json

with open('tasks.json', 'r') as file:
    data = json.load(file)
#print(data["var4"])
print(type(data))
def getmatrix(var):
    mat = (data[var])
    return mat


# for row in data["var4"]:
#     for col in row:
#         print(col)
