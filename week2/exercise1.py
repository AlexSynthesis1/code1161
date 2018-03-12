"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think that this will associate the values withhin the brackets to the function some_words
some_words = ['what', 'does', 'this', 'line', 'do', '?']
##I think this will print "what does thisline do?" by calling the print function
for word in some_words:
    print(word) # It printed the words out but downt the page
# nothing happens because thevalue x was never associated with some_words
for x in some_words:
    print(x)    #It printed all the words doen the page again
# I think it will print out the tuple that has been associated with the funcion some_words
print(some_words)   # It prints out the values within the tuple on a single line rather tha downwards 
# The line some_words contains more than 3 words will be printed since the function some_words has more than 3 values within its tuple
if len(some_words) > 3:
    print('some_words contains more than 3 words')  #this line was printed
#   returns the System OS name, computer's network name, the release value, the OS version, the machine type, and the processor name in
# that order as tuple.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()    # returned the aforemetioned tuple list, denoting all details listed within
