import os, json
already_written = ["ASSEMBLY_Baseplate_v2", "ASSEMBLY_CUBE_LED_Matrix_v2", "ASSEMBLY_CUBE_Mirror_45_v2", "ASSEMBLY_CUBE_Dichroic_Beamsplitter_v2", "ASSEMBLY_CUBE_Base_v2", "ASSEMBLY_CUBE_Z-STAGE_v2"]
dirs = [x for x in os.scandir() if ("ASSEMBLY" in x.name)]
dirs = [x for x in dirs if x.name not in already_written]
print(os.getcwd())
os.chdir(input("enter chdir path: ('.' to stay in current folder). we want to end up in /CAD of the repo we're generating configs for:\n"))
for d in dirs:
    print("generating config for {}".format(d.name))
    desc = input("Description (one liner):\n")
    
    print("We'll now guide you through setting up the options. enter an option, or press return when done.")
    options = {}
    selectingOptions = True
    while (selectingOptions):
        key = input("new option (camelCase'd):\n")
        if key == "":
            selectingOptions = False
        else:
            displayName = input("enter the name of the option as shown to the user:\n")
            choices = []
            for i in range(int(input("number of choices:\n"))):
                choices.append(input("choice #{}:\n".format(i+1)))
                options[key] = {
                    "displayName": displayName,
                    "choices": choices
                }
            
    print("Time to assign files to options. For all files, please input the path relative to the home dir of the module.\n e.g.: STL/file.stl")
            
    print("\n fixed files (that will always be included with the module): enter path, or return when complete")
    fixedFiles = []
    inputtingFixedFiles = True
    while (inputtingFixedFiles):
        path = input("path:\n")
        if path == "":
            inputtingFixedFiles = False
        else:
            fixedFiles.append(path)
            
    print("For each file that is included conditionally, specify the name of the files, and we'll ask for the conditions of inclusion. Again, return ends the list.")
    dynamicFiles = []
    inputtingDynamicFiles = True
    while (inputtingDynamicFiles):
        f = {}
        path = input("path:\n")
        if path == "":
            inputtingDynamicFiles = False
        else:
            f["path"] = path
            f["conditions"] = {}
            for key in options.keys():
                choices = input("enter a comma (no spaces!!) delimited list of all choices to include this file for. press return if this file is not dependent on the option:.\n for option:\t{}\n".format(key)).split(',')
                if choices != "":
                    f["conditions"][key] = choices
            dynamicFiles.append(f)
                    
                    
        
    with open(d.name + "/config.json", "w") as j:
        data = {
            "type":"module",
            "description" : desc,
            "options": options,
            "fixedFiles": fixedFiles,
            "dynamicFiles": dynamicFiles
        }
        json.dump(data, j, indent=2)
    print("config written!\n\n")
    
