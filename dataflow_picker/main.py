import pick
import pandas as pd 
from datetime import datetime

now = datetime.now()

file = "dataFlow.xml"
find = "<structure:Dataflow id="
df = pd.DataFrame(columns=["dataflowId", "agencyId", "version"])


list_of_functions = ["get_line", "formatting_line, "]

log = pd.DataFrame(columns=["time", "command"])

def interface():
    loop = True
    print("this is a ABS toolkit made to help find and display data \nthis is a command line base version made for testing")
    while loop:
        user_input_log("hello")
        if log.loc[log.shape[0], "command"] == "exit":
            loop = False
        else:
            validating_input()
            
def validating_input():
    print("hello")

        

def user_input_log(text):
    print(text)
    log.loc[log.shape[0]+1, "time"] = now.strftime("%H:%M:%S")
    log.loc[log.shape[0], "command"] = input()


def print_log(num):
    print(log.tail(num))

# def makeactions():
#     if 

def last_entry():
    return log.loc[log.shape[0], "time"]

# interface()

last_entry()