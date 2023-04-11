file_dataFlow = "data\\xml_files\\dataFlow.xml"
find_dataFlow = "<structure:Dataflow id="

file_dsd = "data\\xml_files\\ABS_ALC_children.xml"
file_dsd = "data\\xml_files\\ABS_ACLD_LFSTATUS_test.xml"

file_dsd = "data\\xml_files\\ABS_ALC_children.xml"
file_dsd = "data\\xml_files\\ABS_ACLD_LFSTATUS_test.xml"

dsdKeyword = ['position="','">',"<structure:Enumeration>", ""]

# these list are prepared with there usecase in mind forexample string that 
# that are used in the same file will be keeped in the same list

parsing_dataflows = [
    ["this is the file name for dataflow", "data\\xml_files\\dataFlow.xml"],
    ["this is the keyword we use to get the lines with ID information", "<structure:Dataflow id="],
    ["this is the starting keystring for parsing the ID out of line", "id=" ],
    ["this is the ending keystring for parsing the ID out of line", "agencyID" ],
    ["this is the starting keystring for parsing the agencyID out of line", "agencyID" ],
    ["this is the ending keystring for parsing the agencyID out of line", "version" ],
    ["this is the starting keystring for parsing the version out of line", "version" ],
    ["this is the ending keystring for parsing the version out of line", "isFinal" ],
]

# need to move data from pcik.py for dsd to here 
# parsing_dsd = [

# ]







# this where all the test is going to be saved for the interface part of the progame 
main_meun_text = "Welcome to the main menu if you would like a full list of command type in help "

# error messages 
int_error = "you need to enter a number"
options_error = "this options does not exits type help for a list of commands"

# --------------------------
#  users interface 
welcome_message = """Welcome to our data picking program powered by the ABS API! 

With this program, you can easily access the data you need for your research, analysis, or any other purpose. 

If you need any assistance or have any questions, don't hesitate to reach out to i'm always here to help! 

Thank you for trying my program, and i hope you find the data you need."""

welcome_art = """ 
 \ \        / /  ____| |    / ____/ __ \|  \/  |  ____| 
  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__    
   \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|   
    \  /\  /  | |____| |___| |___| |__| | |  | | |____  
     \/  \/   |______|______\_____\____/|_|  |_|______
     """

3