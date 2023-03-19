import pandas as pd 
import requests

# we need to get the DSD for what we are looking for 
    # the frist 2 things we need are 

        # flowref 

        # datakey 
#  https://api.data.abs.gov.au/data/{flowRef}/{dataKey}?{queryParameters}.

df = pd.read_csv("test_set.csv")


# Ref = "null"
# Key = "null"
# Parameters = "null"



def interface():
    print("hello")



def show_all_data(data, amount_displayed):
    print("\n")
    print("this is data.loc")
    
    test = True
    index = 0

    while test:
        for i in range(amount_displayed):
            print("\n")
            print(data.loc[index])
            index = index + 1
        userInput = input()
        if userInput == "exit":
            test = False


def show_data(data, index):
    print(data.loc[index])

def get_dsd(data, index):
    print("\n")
    ref = data["dataflowId"].loc[index]
    key = data["agencyId"].loc[index]
    # Parameters = data["version"].loc[index]
    Parameters = ""

    return create_url(ref, key)


def create_url(flowRef, agencyID, queryParameters = None):
    if queryParameters == None:
        return "https://api.data.abs.gov.au/datastructure/{}/{}".format(agencyID, flowRef)


def check_link(url):
    if requests.get(url) != 200:
        print(requests.get(url))


def test_link(index = None):
    if index == None:
        for i in range(1099):
            x = requests.get(get_dsd(df, i))
            if x.status_code == 200:
                print(get_dsd(df, i))
                print(x)
            else:
                print("-------ERROR---------")
                print(get_dsd(df, i))
                print(x)
            c = input()
    else:
        x = requests.get(get_dsd(df, index))
        print(x.status_code)




# show_data(df, 10)
# get_dsd(df, 1)
show_all_data(df,10)
# create_url(Ref, Key, Parameters)

