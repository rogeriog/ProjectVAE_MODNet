import re
with open("log.txt","r") as f:
    ## get entries between [ ], but only those with number and floats separated by spaces
    # like [1.7000000000000002 150 0.0014000000000000002 32 0].
    entries = re.findall(r"\[(\d+\.\d+\s\d+\s\d+\.\d+\s\d+\s\d+)\]|(Generation)", f.read())
    # get non empty entries
    for entry in entries:
        if entry[0] != "":
            print(entry[0])
        else:
            print(entry[1])

    
    
