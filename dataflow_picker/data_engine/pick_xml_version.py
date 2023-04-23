import pandas as pd 
import numpy as np 
import data_engine.data_sorter as db 
import xml.etree.ElementTree as ET
import requests
from io import BytesIO

dataflow_file = "data\\working_dir\\file.xml"
dsd_file = "data\\working_dir\\dsd.xml"
data_file = "data\\working_dir\\data.xml"

# url = "https://api.data.abs.gov.au/datastructure/ABS/ALC"
# r = requests.get(url)
# print(type(r))
# print(type(r.content))

# tree = ET.parse(BytesIO(r.content))
# root = tree.getroot()
# print("root tag ", root.tag)
# print("root attrib ", root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

# for value in root.iter('{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsDimension'):
#     print(value.attrib['value'])



# get file 
def get_xml_tree(file_name = False, api = False):
    if file_name == False and api == False:
        print("no file was passed you need to pass a file or an api call")
    elif file_name != False:
        print("file opening")
        tree = ET.parse(file_name)
        root = tree.getroot()
        return root
    elif api != False:
        print("api called")
        tree = ET.parse(api)
        root = tree.getroot()
        return root
    
    

# parse dataflow 
def paeseDataflow(root_element):
    something = []
    for name in root_element.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}Name"):
        dataFlow.loc[dataFlow.shape[0], "name"] = name.text
    for index, metadata in enumerate(root_element.iter("Ref")):
        dataFlow.loc[index, 'dataflowId'] = metadata.attrib['id']
        dataFlow.loc[index, 'agencyId'] = metadata.attrib['agencyID']
        dataFlow.loc[index, 'version'] = metadata.attrib['version']
    for index, description in enumerate(root_element.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}Description")):
        dataFlow.loc[index, 'description'] = description.text


# parse dsd 
def paeseDsd(root_element):
    for name in root_element.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}Dimension"):
        # dsd.loc[dsd.shape[0], 'Position'] = name.attrib['position']
        # print(name.attrib['position'])
        if name.attrib:
            dsd.loc[dsd.shape[0], 'Position'] = name.attrib['position']
            dsd.loc[dsd.shape[0]-1, 'Position_id'] = name.attrib['id']
            # print(name.attrib)
            
    for time_position in root_element.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}TimeDimension"):
        dsd.loc[dsd.shape[0], 'Position'] = time_position.attrib['position']
        dsd.loc[dsd.shape[0]-1, 'Position_id'] = time_position.attrib['id']

    # for test in root_element.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}Codelist[.='Type of Volume'"):
    #     print(test.attrib)
    #     print(test[0].text)
    name_elem = root_element.find('.//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}Name[@xml:lang="en"]')
    type_of_volume = name_elem.text
    print(type_of_volume)
    print(dsd)
        

# parse data 

# api call 
def api_call():
    url = "https://api.data.abs.gov.au/datastructure/ABS/ALC?references=children"
    r = requests.get(url)
    print(type(r))
    print(type(r.content))
    root = ET.fromstring(r.text)
    tree = ET.ElementTree(root)
    tree.write("data\\working_dir\\dsd.xml")



# make working dir 
    # checek to see if the file has been saved before making a new call 
    # delete files at the end of session 

# data = pd.DataFrame(columns=['data', 'time_period'])
dataFlow = pd.DataFrame(columns=["dataflowId", "agencyId", "version", "name", "description"])
dsd = pd.DataFrame(columns=["Position", "Position_id", "Name", "Code"])


# paeseDataflow()
# paeseDataflow(get_xml_tree(dataflow_file))
paeseDsd(get_xml_tree(dsd_file))
# print(dataFlow)
# api_call()

