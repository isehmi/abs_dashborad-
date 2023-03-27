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
                    DSD_add_to_df(lines)
                
    fp.close()
    return lines

# this needs to be moved into DataFlow_add_to_df 
def test(lines):
    for line in lines:
        if line.find(find)!= -1:
             DataFlow_add_to_df(line, db.parsing_dataflows) 



def DataFlow_add_to_df(line, keystring):

    df.loc[df.shape[0]+1, "dataflowId"] = line[line.find(keystring[2][1])+4:line.find(keystring[3][1])-2]

    df.loc[df.shape[0], "agencyId"] = line[line.find(keystring[4][1])+10:line.find(keystring[5][1])-2]

    df.loc[df.shape[0], "version"] = line[line.find(keystring[6][1])+9:line.find(keystring[7][1])-2]
    

# this is dataflow in a pandas dataframe 
# get_line(file)
# print(df)

def DSD_add_to_df(lines):
    keyword = ['position="','">',"<structure:Enumeration>", ""]
    positions_counter = 0
    positions_counter_id = 0

    for i, line in enumerate(lines):
        if line.find(keyword[0]) != -1: # this is looking for all the lines with positions in it 
            dsd.loc[dsd.shape[0]+1, "Position"] = line[line.find(keyword[0])+10:line.find(keyword[2])-2]
            positions_counter = positions_counter + 1

        elif line.find(keyword[2]) != -1: # this is looking for all the lines with the ids 
            line_temp = lines[i+1]
            if pd.isna(dsd["Position_id"].loc[dsd.shape[0]]):
                dsd["Position_id"].loc[dsd.shape[0]] = line_temp[line_temp.find('<Ref id="')+9:line_temp.find(' version')-1]
            else:
                old_cell =  dsd["Position_id"].loc[dsd.shape[0]]
                new_data = line_temp[line_temp.find('<Ref id="')+9:line_temp.find(' version')-1]
                new_cell = old_cell + "," + new_data
                dsd["Position_id"].loc[dsd.shape[0]] = new_cell
    
    # now we want to fill code and name columns using the infomation we just got 
    NameCode(lines)


    # checking pandas value  
    print("this is the full data frame")
    print(dsd.head(10))
    print("this is just positions ID col")
    print(dsd["Position_id"].head(10))
    print("looking at the last element in positions IDS")
    print(dsd.loc[dsd.shape[0], "Position_id"])
            # positions_counter_id = positions_counter_id + 1
            #  check to see if the spot is free (null) if it is save the data if something is there then get the old data and make an list with it 




def NameCode(lines):
     looking_for = '<structure:Codelist id="' + dsd.loc[1, "Position_id"]
     print(looking_for)
     print("hello")
#  add a for loop here that runs over the dad 
    #  for i, line in enumerate(lines):
    #       if line.find() != -1:
    #            print("hello")









# getting dsd 

#  get the order 

# get what the values are 

# to find positions use this keyword position="
# to find position id use this keyword <structure:Enumeration> and then get the line under it in that line we want <Ref id="

dsd = pd.DataFrame(columns=["Position", "Position_id", "Name", "Code"])
dsd_file_name = "ABS_ALC_children.xml"
get_line(dsd_file_name, True)


# dsd will have all the information you need to make an api call 



