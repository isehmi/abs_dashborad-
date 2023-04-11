import pandas as pd
import numpy as np
import data_engine.data_sorter as db 
# import data_sorter as db# this is where alot of var live 

def get_line(file_name):
    fp = open(file_name, "r")
    with open(file_name, "r"):
        lines = fp.readlines()
    fp.close()
    return lines

def make_dataFlow_df():
    test = 0
    lines = get_line(db.file_dataFlow)
    for line in lines:
        if line.find(db.find_dataFlow)!= -1:
            dataFlow.loc[dataFlow.shape[0]+1, "dataflowId"] = line[line.find(db.parsing_dataflows[2][1])+4:line.find(db.parsing_dataflows[3][1])-2]
            dataFlow.loc[dataFlow.shape[0], "agencyId"] = line[line.find(db.parsing_dataflows[4][1])+10:line.find(db.parsing_dataflows[5][1])-2]
            dataFlow.loc[dataFlow.shape[0], "version"] = line[line.find(db.parsing_dataflows[6][1])+9:line.find(db.parsing_dataflows[7][1])-2]
        if line.find('<common:Name xml:lang="en">')!= -1:  #adding Name 
            dataFlow.loc[dataFlow.shape[0], "name"] = line[line.find('<common:Name xml:lang="en">')+27:line.find("</common:Name>")-14]
        if line.find('<common:Description xml:lang="en">')!= -1: #adding description
            dataFlow.loc[dataFlow.shape[0], "description"] = line[line.find('<common:Description xml:lang="en">')+34:line.find("</common:Description>")-21]

def positions_data(line):
    dsd.loc[dsd.shape[0]+1, "Position"] = line[line.find(db.dsdKeyword[0])+10:line.find(db.dsdKeyword[2])-2]
    
def id_data(lines, i):
    line_temp = lines[i+1]
    if pd.isna(dsd["Position_id"].loc[dsd.shape[0]]):
        dsd["Position_id"].loc[dsd.shape[0]] = line_temp[line_temp.find('<Ref id="')+9:line_temp.find(' version')-1]
        name_data(section(lines), lines)
        code_data(section(lines),lines)
    else:
        old_cell =  dsd["Position_id"].loc[dsd.shape[0]]
        new_data = line_temp[line_temp.find('<Ref id="')+9:line_temp.find(' version')-1]
        new_cell = old_cell + "," + new_data
        dsd["Position_id"].loc[dsd.shape[0]] = new_cell
    

def name_data(section, lines):
    items = []

    for line in lines[section[0]:section[1]]:
        if line.find('<common:Name xml:lang="en">') != -1:
            items.append(line[line.find('<common:Name xml:lang="en">')+27:line.find('/common:Name')-1])
    dsd.loc[dsd.shape[0], 'Name'] = items


def code_data(section, lines):
    items = []
    for line in lines[section[0]:section[1]]:
        if line.find('<structure:Code id="') != -1:
            items.append(line[line.find('<structure:Code id="')+20:line.find('">')])
    dsd.loc[dsd.shape[0], 'Code'] = items


def section(lines):
    keyword_start = '<structure:Codelist id="' + dsd.loc[dsd.shape[0], "Position_id"]
    keyword_end = '</structure:Codelist>'
    section = []
    key = False
    for i, line in enumerate(lines):
        if line.find(keyword_start) != -1 and key == False:
            section.append(i)
            key = True
        elif line.find(keyword_end) != -1 and key:
            section.append(i)
            key = False
    return section    


def make_dsd_df():
    lines = get_line(db.file_dsd)
    
    for i, line in enumerate(lines):
        if line.find(db.dsdKeyword[0]) != -1: # this is looking for all the lines with positions in it 
            positions_data(line)
        elif line.find(db.dsdKeyword[2]) != -1: # this is looking for all the lines with the ids 
            id_data(lines, i)
            section(lines)



dataFlow = pd.DataFrame(columns=["dataflowId", "agencyId", "version", "name", "description"])
dsd = pd.DataFrame(columns=["Position", "Position_id", "Name", "Code"])




if __name__ == '__main__':

    make_dataFlow_df()
    make_dsd_df()
    print("------- this is the DataFlow Df ---------")
    print(dataFlow.head())
    print("\n\n-------- this is the DSD DF ---------")
    print(dsd.head())



