"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will declare a variable called some_words
# and it will put a list of strings into it
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think this will print out 1 word from some_words according to the order
for word in some_words:
    print(word)

# I think x is = word and it will print out one of the words in the list "some_words"
for x in some_words:
    print(x)

# I think this will just print the list of words in (some_words)
print(some_words)

# I think this will identify the words that has more than 3 letters
# and come back at true as there're a few words that contains more that 3 letters
if len(some_words) > 3:
    print('some_words contains more than 3 words')

# This function will give you the system, node, release, version, machine
# and the processer tuple
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
