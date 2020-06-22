import os, json
import glob # the readme isn't all the same capitalization anymore
import re   # the descrptions are getting messy here

def get_modules(dirname):
    """ Basically look through the STL names to try to find a unique match in the CAD subfolder. just an estimate for now, this needs to be gone through manually"""
    modules = []
    try:
        fs = os.scandir(dirname + "/STL")
    except FileNotFoundError: # some incomplete applications
        fs = []
        print("file not found :( no module completion")
    for f in fs:
        matches = glob.glob("../CAD/ASSEMBLY_*/STL/" + f.name)
        if len(matches) == 1:
            modname = re.search(r"ASSEMBLY.*?(?=/)", matches[0]).group(0)
            modules.append({
                "name":modname,
                "fixedOptions": {}
            })
    return modules

    
sentence = re.compile(r"[A-Z][a-z]+.*\.")
dirs = [x for x in os.scandir() if "APP" in x.name]
for d in dirs:
    print(d.name)
    with open(glob.glob(d.name + "/*.md")[0], "r") as f:
        f.readline()
        x = ""
        while not sentence.match(x): x = f.readline()
        desc = x.replace("This is the repository for ", "").replace("The stl-files can be found in the folder [STL](./STL).", "").replace("\n", "") # quick and dirty estimate.
        if "STL" in desc: desc = "TODO: This, and the readme, needs more documentation."
        #print(desc)
        with open(d.name + "/config.json", "w") as j:
            data = {
                "type":"application",
                "description" : desc,
                "modules": get_modules(d.name)
                }
            json.dump(data, j, indent=2)
