# import pick as pick
# import pandas as pd 

# df = pick.dataFlow
# save = 0

# def make_url():
#     print(pick.dataFlow)

# def ask_users():
#     key = True
#     while key:
#         print("Welcome here we will look at the data flow to get the right dsd for you")
#         for i, item in df.iterrows():
#             print(item["name"])
#             print("does this look like what you are looking for if you would like more info type 'more' if not press enter if this is the one you want type in select")
#             user = input()
#             if user == 'more':
#                 print(item["description"])
#             elif user == 'select':
#                 save = i
#                 key = False



#         key = False

# # make_url()
# ask_users()\
import pick
import pandas as pd 

df = pick.dataFlow
save = 0

def make_url():
    print(df)

def ask_users():
    global save # Make 'save' a global variable
    key = True
    while key:
        print("Welcome here we will look at the data flow to get the right dsd for you")
        for i, item in df.iterrows():
            print(item["name"])
            print("Does this look like what you are looking for? If you would like more info, type 'more'. If not, press enter. If this is the one you want, type 'select'.")
            user = input()
            if user == 'more':
                print(item["description"])
            elif user == 'select':
                save = i
                key = False
                break # Exit the for loop if an item is selected


# make_url()
ask_users()