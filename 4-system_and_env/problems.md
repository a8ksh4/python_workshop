# os module
* def getEnvironVariable(string) -> string
  * 40
  * Given the name of an env variable, return the value of that environment variable. 
* setEnvironVariable(string, string)
  * 40
  * Given the name of an env variable and a value to set it to, set the value to the var. 
* nPendEnvPath([paths], prepend=False, append=False)
  * 41
  * Given a list of paths, either prepend them to the environment PATH variable or append them, depending on which 
    arg is true, and do nothing of neither prepend or append is True. 
* 


# sys module
* getScriptLoc() -> (real_path, file_name)
  * 41
  * Use sys.argv to get and return the path to the program that's being run and the name of the program as a tuple.
* checkDebugArg() -> bool
  * 41
  * Check the progam args (sys.argv) to see if the user passed in a -d or --debug flag.  if so, return True, otherwise
    return false. 
* parseArgs1() -> dictionary
  * 42
  * Write a functoin that will parse the arguments for some fine program.  The program allows the following argumetns:
    our_prog.py \[--num_tries <num>] [--user_name <name>] [--fail_message <message]  
    The function shouold return a dictionary like this: {'num_tries': ..., 'user_name': ..., 'fail_message': ...}. The
    value assocaiated with each key should be pulled from the args, and if an argument isn't specified, set it's value
    to None in the dictionary. If an unknown argument is encountered, return None instaead of the dict.
                                                                                     
# argparse
* parseArgs2() -> dictionary
  * 42
  * Redo parseArgs1 but use the argparse module. Put your function in its own script to test, check the output you get
    for --help. 

# platform
* n/a

# subprocess
* runGetOutputShell(command) -> string
  * 43
  * use subprocess check_output to run the given command and return its output. 
    Assume that the command will be a string.
    and set shell=True. 
    If there is an exception (any), return None. 
* runGetOutput(command) -> string
  * 44
  * check if command is a string or a list.  Set shell=True if it is a list, otherwise, leave it as false (unset). 
    Same as above, catch any exceptoins and return None, or return the ouptut of the given command as a string. 
* runGetStatus(command) -> bool
  * 44
  * run the given command and return True if the exit status is 0, or False if the exit status is not zero. 
  * Return None for any exceptions.  
  * Assume tha the command will be a list and keep shell=False. 

