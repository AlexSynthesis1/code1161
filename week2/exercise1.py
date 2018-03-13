"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']
# I think that this will print the tuple allocated to some words.
for word in some_words:
    print(word) # The words are printed but vertically rater than horizontally.
# I think nothing will happen because there is no variable x within the tuple of some_words.
for x in some_words:
    print(x) # It is still printed, and stll printed vertically.
# It will print out the tuple associated with some_words horizontally.
print(some_words)# The tuple associated with some_words was printed out within square brackets.
# The code will test to see if there ware more than 3 values within the tuple of some_words, and because there are it will print the next line
if len(some_words) > 3:
    print('some_words contains more than 3 words') # This line is printed because the condition of length is fulfilled.

def usefulFunction():# UsefulFunction isrun, and thus platform.name is printed. This refers to a list composed of System OS, Computer Node/Network Name, System Release Number, System Version, Machine Type, and Processor Name in that order.
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction() # The aforementioned list of different computer based details is printed out.
