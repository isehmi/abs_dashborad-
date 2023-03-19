import re 
import pandas as pd 
import numpy as np

file = "dataFlow.xml"
find = "<structure:Dataflow id="
fp = open(file, 'r')
line_test = 'Line: <structure:Dataflow id="LC_CM_15" agencyID="ABS" version="1.0.0" isFinal="true">'
save_data = []
agencyId = []
version = []

dataflow = pd.DataFrame(columns=['agencyId', 'dataflowId', 'version'])
dsd = pd.DataFrame()

def open_file(file_name, word):
    with open(file_name, 'r') as file:
        content = file.read()
        if word in content:
            print("yes")
        else:
            print("no")
        file.close()

def open_line(file_name, word):
    with open(file_name, 'r'):
        lines = fp.readlines()
        for line in lines:
            if line.find(find)!= -1:
                print('Line Number:', lines.index(line))
                print('Line:', line)
                # formang_line(line) 
        fp.close()
        lines.close()


def formang_line(line):
    start_id = "id="
    end_id = "agencyID"

    start_agencyId = 'agencyID='
    end_agencyId = 'version'

    start_version = "version="
    end_version = 'isFinal'

    temp_id = line[line.find(start_id)+4:line.find(end_id)-2]
    temp_agencyID = line[line.find(start_agencyId)+10:line.find(end_agencyId)-2]
    temp_version = line[line.find(start_version)+9:line.find(end_version)-2]

    save_data.append(temp_id)
    agencyId.append(temp_agencyID)
    version.append(temp_version)
    




# open_file(file, find)
# open_line(file, find)
# formang_line(line_test)

# df = pd.DataFrame(save_data, columns=["id"])
df = pd.DataFrame({
    'dataflowId': save_data,
    'agencyId': agencyId,
    'version' : version
})
# print(df.head())

df.to_csv("test_set")



# dataflow.append({'dataflowId': save_data}, ignore_index=True)
# print(dataflow["dataflowId"].head())




# working on dsd now 


# the input for this file is 
#   first we have dataflow 
#   then we have dsd 
# the outputs for this file 
#   we want a pandas data frame for dataflow with dataflowId, agencyId, version
#   we want a pandas data frame for dsd that has 




# def create_df(file, key_words):
#     with open(file, "r"):
#         lines = fp.readlines()
#         for line in lines:
#             if line.find(key_words) != -1:
#                 print('Line Number:', lines.index(line))
#         lines.close()
                        
tb = open("ABS_ALC_children.xml", 'r')

def test(file1):
    with open(file1, "r"):
            lines = tb.readlines()
            for line in lines:
                print(line)


# create_df("ABS_ALC_children.xml", "<Ref id=")
test("ABS_ALC_children.xml")
