import os, json
dirs = [x for x in os.scandir() if "ASSEMBLY" in x.name]
for d in dirs:
    print(d.name)
    with open(d.name + "/Readme.md", "r") as f:
        f.readline()
        desc = f.readline().replace("This is the repository for ", "").replace("The stl-files can be found in the folder [STL](./STL).", "").replace("\n", "") # quick and dirty estimate.
        with open(d.name + "/config.json", "w") as j:
            data = {
                "type":"module",
                "description" : desc,
                "options": {}
                }
            json.dump(data, j, indent=2)
