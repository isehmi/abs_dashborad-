import pandas as pd
import numpy as np
import data_sorter as db # this is where alot of var live 

# getting dataflow 

file = "dataFlow.xml"
find = "<structure:Dataflow id="
df = pd.DataFrame(columns=["dataflowId", "agencyId", "version"])

def get_line(file_name, formatLine):
    fp = open(file_name, "r")
    with open(file_name, "r"):
        lines = fp.readlines()
        if formatLine == True:
                    # DataFlow_add_to_df(line, db.parsing_dataflows) 
                    DSD_add_to_df(line)
                
    fp.close()
    return lines

# this needs to be moved into DataFlow_add_to_df 
def test(lines):
    for line in lines:
        if line.find(find)!= -1:
             DataFlow_add_to_df(line, db.parsing_dataflows) 



def DataFlow_add_to_df(line, keystring):

    df.loc[df.shape[0]+1, "dataflowId"] =line[line.find(keystring[2][1])+4:line.find(keystring[3][1])-2]

    df.loc[df.shape[0], "agencyId"] = line[line.find(keystring[4][1])+10:line.find(keystring[5][1])-2]

    df.loc[df.shape[0], "version"] = line[line.find(keystring[6][1])+9:line.find(keystring[7][1])-2]
    

# this is dataflow in a pandas dataframe 
# get_line(file)
# print(df)

def DSD_add_to_df(lines):
    for line in lines:
        if line.find(find)!= -1:
            keyword = ['position="','">',]
            print("helloo")
            print("we are trying to find the positions", line[line.find(keyword[0]):line.find(keyword[1])])



# getting dsd 

#  get the order 

# get what the values are 

# to find positions use this keyword position="
# to find position id use this keyword <structure:Enumeration> and then get the line under it in that line we want <Ref id="

dsd = pd.DataFrame(columns=["Position", "Position_id", "version"])
dsd_file_name = "ABS_ALC_children.xml"
get_line(dsd_file_name, True)

