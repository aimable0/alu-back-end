import json

sample_dict = {
    "userid": [
        {
            "task": "suscipit repellat esse quibusdam voluptatem incidunt",
            "completed": "false",
            "username": "Antonette",
        },
        {
            "task": "suscipit repellat esse quibusdam voluptatem incidunt",
            "completed": "false",
            "username": "Antonette",
        },
        {
            "task": "suscipit repellat esse quibusdam voluptatem incidunt",
            "completed": "false",
            "username": "Antonette",
        },
    ]
}

sample_list = list()
dict1 = {"name": "Omar", "age": 12}
dict2 = {"name": "Omar", "age": 12}
# with open("file.json", "w") as file:
# json.dump(sample_dict, file, indent=1)
sample_list.append(dict1)
sample_list.append(dict2)
print(sample_list)

big_dict = {"2": sample_list}
print(big_dict)
