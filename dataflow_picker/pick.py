import pandas as pd
import numpy as np

file = "dataFlow.xml"
find = "<structure:Dataflow id="
df = pd.DataFrame(columns=["dataflowId", "agencyId", "version"])

def get_line(file_name):
    fp = open(file_name, "r")
    with open(file_name, "r"):
        lines = fp.readlines()
        for line in lines:
            if line.find(find)!= -1:
                # print('Line Number:', lines.index(line))
                # print('Line:', line)
                formang_line(line) 
    fp.close()

def formang_line(line):
    start_id = "id="
    end_id = "agencyID"

    start_agencyId = 'agencyID='
    end_agencyId = 'version'

    start_version = "version="
    end_version = 'isFinal'

    df.loc[df.shape[0]+1, "dataflowId"] =line[line.find(start_id)+4:line.find(end_id)-2]

    df.loc[df.shape[0], "agencyId"] = line[line.find(start_agencyId)+10:line.find(end_agencyId)-2]

    df.loc[df.shape[0], "version"] = line[line.find(start_version)+9:line.find(end_version)-2]
    

    



get_line(file)
print(df)