import pandas as pd 
import numpy as np 
import data_engine.data_sorter as db 
import xml.etree.ElementTree as ET
import requests
from io import BytesIO
import os.path as os 

files = {
    "dataflow_file.xml" : "data\\working_dir\\dataflow_file.xml",
    'dsd_file.xml' : "data\\working_dir\\dsd_file.xml",
    "data_file.xml" : "data\\working_dir\\data.xml"
}

dsd_url = 'https://api.data.abs.gov.au/datastructure/ABS/ALC?references=children'
dataflow_url = 'https://api.data.abs.gov.au/dataflow'
data_url = 'https://api.data.abs.gov.au/data/ALC/1.2.1.4.A.'
ns = [
    '{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message}',
    '{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}',
    '{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}'
]


def api_call(url, file_name):
    file_name = 'data\\working_dir\\' + file_name 
    try:
        r = requests.get(url)
        r.raise_for_status()

        root = ET.parse(BytesIO(r.content))
        with open(file_name, 'wb') as f:
            root.write(f)
        
        if root:
            return root
        else:
            print("their has been an error in the api call")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")


def open_local_file(file_name):
    print(file_name)
    root = ET.parse(file_name)
    return root

def get_xml(file_name):
    file = files[file_name]
    if os.isfile(file):
        print('the file is here opening now')
        return open_local_file(file)
    else:
        print('calling api')

        return api_call(get_url(), file_name)


def get_url():
    # this is a WIP it will link to the webapp and get the url that is needed
    return dsd_url

def paeseDataflow():
    root = get_xml("dataflow_file.xml")
    for name in root.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}Name"):
        dataFlow.loc[dataFlow.shape[0], "name"] = name.text
    for index, metadata in enumerate(root.iter("Ref")):
        dataFlow.loc[index, 'dataflowId'] = metadata.attrib['id']
        dataFlow.loc[index, 'agencyId'] = metadata.attrib['agencyID']
        dataFlow.loc[index, 'version'] = metadata.attrib['version']
    for index, description in enumerate(root.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}Description")):
        dataFlow.loc[index, 'description'] = description.text


def get_name(section, root, index):
    key = section[1][0][0].attrib['id']
    title_for_position = root.find('{0}Structures/{1}Codelists/{1}Codelist[@id="{3}"]/{2}Name'.format(ns[0], ns[1], ns[2], key))
    names = [title_for_position.text]

    values_for_name = root.findall('{0}Structures/{1}Codelists/{1}Codelist[@id="{3}"]/{1}Code/{2}Name'.format(ns[0], ns[1], ns[2], key))
    for name in values_for_name:
        names.append(name.text)
    dsd.loc[index, 'Name'] = names

    Code = root.findall('{0}Structures/{1}Codelists/{1}Codelist[@id="{3}"]/{1}Code'.format(ns[0], ns[1], ns[2], key))
    code = []
    for i in Code:
        code.append(i.attrib['id'])
    dsd.loc[index, 'Code'] = code


def get_dsd_df():
    root = get_xml('dsd_file.xml')
    count = 0
    for i in root.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}Dimension"):
        if i.attrib:
            dsd.loc[dsd.shape[0], "Position"] = i.attrib["position"]
            get_name(i, root, count)
            dsd.loc[dsd.shape[0] - 1, 'Position_id'] = i.attrib['id']
            count = count + 1


data = pd.DataFrame(columns=['data', 'time_period'])
dataFlow = pd.DataFrame(columns=["dataflowId", "agencyId", "version", "name", "description"])
dsd = pd.DataFrame(columns=["Position", "Position_id", "Name", "Code"])

paeseDataflow()
print(dataFlow)
get_dsd_df()
print(dsd)