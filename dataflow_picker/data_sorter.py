file_dataFlow = "dataFlow.xml"
find_dataFlow = "<structure:Dataflow id="

file_dsd = "ABS_ALC_children.xml"

dsdKeyword = ['position="','">',"<structure:Enumeration>", ""]

# these list are prepared with there usecase in mind forexample string that 
# that are used in the same file will be keeped in the same list

parsing_dataflows = [
    ["this is the file name for dataflow", "dataFlow.xml"],
    ["this is the keyword we use to get the lines with ID information", "<structure:Dataflow id="],
    ["this is the starting keystring for parsing the ID out of line", "id=" ],
    ["this is the ending keystring for parsing the ID out of line", "agencyID" ],
    ["this is the starting keystring for parsing the agencyID out of line", "agencyID" ],
    ["this is the ending keystring for parsing the agencyID out of line", "version" ],
    ["this is the starting keystring for parsing the version out of line", "version" ],
    ["this is the ending keystring for parsing the version out of line", "isFinal" ],
]





# this where all the test is going to be saved for the interface part of the progame 
main_meun_text = "Welcome to the main menu if you would like a full list of command type in help "

# error messages 
int_error = "you need to enter a number"
options_error = "this options does not exits type help for a list of commands"



