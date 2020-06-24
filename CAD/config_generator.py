import os, json
already_written = ["ASSEMBLY_Baseplate_v2", "ASSEMBLY_CUBE_LED_Matrix_v2", "ASSEMBLY_CUBE_Mirror_45_v2"]
dirs = [x for x in os.scandir() if ("ASSEMBLY" in x.name)]
dirs = [x for x in dirs if x.name not in already_written]
for d in dirs:
    print(d.name)
    with open(d.name + "/Readme.md", "r") as f:
        f.readline()
        desc = f.readline().replace("This is the repository for ", "").replace("The stl-files can be found in the folder [STL](./STL).", "").replace("\n", "") # quick and dirty estimate.
        with open(d.name + "/config.json", "w") as j:
            data = {
                "type":"module",
                "description" : desc,
                "options": {},
                "fixedFiles": [],
                "dynamicFiles": []
                }
            json.dump(data, j, indent=2)
