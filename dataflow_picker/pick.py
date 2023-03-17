import re 
import pandas as pd 
import numpy as np

file = "dataFlow.xml"
find = "<structure:Dataflow id="
fp = open(file, 'r')
line_test = 'Line: <structure:Dataflow id="LC_CM_15" agencyID="ABS" version="1.0.0" isFinal="true">'
save_data = []

def open_file(file_name, word):
    with open(file_name, 'r') as file:
        content = file.read()
        if word in content:
            print("yes")
        else:
            print("no")

def open_line(file_name, word):
    with open(file_name, 'r'):
        lines = fp.readlines()
        for line in lines:
            if line.find(find)!= -1:
                # print('Line Number:', lines.index(line))
                # print('Line:', line)
                formang_line(line)


def formang_line(line):
    start = "id="
    end = "agencyID"
    index_start = line.find(start)
    index_end = line.find(end)
    # print(index_start," --- ", index_end)
    temp = line[index_start+4:index_end-2]
    # print(temp)
    save_data.append(temp)




# open_file(file, find)
open_line(file, find)
# formang_line(line_test)

df = pd.DataFrame(save_data, columns=["id"])
print(df.head())

