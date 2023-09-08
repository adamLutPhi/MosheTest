from io import TextIOBase

""" Why to use a socket?
  - To send and recieve a message from a user ( Duplex channel)

I am using a speck [why?]

because this is supposed to bs 
"""
#line =

# assign TextIOBase to TextMockSpec
messageBody = "Insert Message \n"
differentThings = " some teaching:Meta"
textMockSpec = TextIOBase
ipAddress = '192.168.1.1'
port = '8085'
socketTuple = ( ipAddress, port)

def textParser():

    magicTextParserMock = mock.MagicMock(spec = textMockSpec)
# First:  Set Your Priorities Right:

    magicTextParserMock.readline.sideEffect =[

"The Most important ",
"medium priority",
"low priority"]
    
    value = parseLines(magicTextParserMock)
#try to assert
        # rule: always enclose your assertions with 
    try:
            assert value == dict( priorityGlossary =
                                  'from high to low Descending ' )
            
    except AssertionError:
            print(repr(AssertionError))

# The ultimate power is: Just to Write Code - Moshe Z )Zadka(

""" but you want to keep your test code to be simple [why?]

Because when test fails , probably because of some buggy code block
in production code
your objective: Zero-in on the code blocks, then reachoing the buggy line
understanding )2(:
1. the error
2. the type of error

-this side effect mock test is easy
it has )little to ( no computation code
'''

'''
the above example was simplified : real  network  service test code that 
should verify the results  it got
'the server' works correctly
meaning:
1. doing a synthetic request
2. while looking for the correct result

Hence, the mock object  emulates  `some` computation  on the input

But,
testing such code is difficult )without performing any computation (

the test would be either )2(:

1. too insensitive 
2. too flaky

[new definition:
insensitive test:
a test which does not fail in the presence of error  )because it is error-invariant(

flakey test :
A test that does fail , even when the Bug is fixed
)code is debugged(


"""

import socket
import random


time = 5

def yoloReader(_socket, time, msg = messageBody ):
    _socket.settimeout(time )
    _socket.connect(socketTuple)

    inputMakeFile =  _sock.makefile()

    # Stochastic Structure: a cont )two faced structure( set the
    ## with )2( possible outcomes:
    order = [ 0, 1 ]
    #    ], [

    # shuffle:  the list [Why?]  to ensure  faireness
    ## before we actually draw samples
    random.shuffles(order)
    while order:
        if order.pop() == 0:
            # use the one functionality that sockets are good at
            ## multicasting: it possibly mean : 
            _socket.sendall(msg)
            key = inputMakeFile.readline().strip()
        else:
            #MultiCast: send a multicast message to everyone on the
            ## Local Area Network LAN 
            
            _socket.sendall(msg)
            value = inputMakeFile.readline().strip()
    #Human error: detected
    return { value : key } # Oops,  buggy line [did the tester observe this ?]

            
from io import TextIOBase
from unittest import mock
import pytest

def insensitiveTest():

    _socket = mock.MagickMock(spec = socket.socket )
    _socket.makefile.return_value.readline.side_effect = ["key\n", "value\n"]

    # assertion statement
    try:

        assert yolo_reader(_socket) == {"key" : "value"}
    # output is entirely random
    except AssertionError:
        print( repr(AssertionError) )
        
"""
Whenever there is a buggy code,
We want to write a test
That will fail when there is a buggy code
If we actually fix the code, we will succeed 
Because of this, we actuall now have to write
You know the right order of things
Is going to get repeatewd
Thus, you can assign to side effect,
Which is an iterable
Let us see how we can do this

"""





"""


"""
from unittest import mock 
differentThings
sideEffects = {1, 2 , 3}

assert differentThings == 1
assert differentThings == 2
assert differentThings == 4

#example : parse 3 lines

from io import TextIOBase

def test_parser():

    filelike = mock.MagicMock(spec = TextIOBase)
    
    filelike.readline.side_effect = ["low\n", "to-some-only\n", "High\n"]

    value = parse_three_lines(filelike)

        # Assert
    try:
        #dictum
        
        assert value == dict(thing = "important/a-little+to-most-people")

    except AssertionError:
        print( repr(AssertionError) )

""" stories are in the air: strytelling is in and a part of life
in our

"""

#Mock sise effect -- function

##This the last fallback.
# We  want our code to stay simple
"""
Keep things simple , as no bugs in test ,
It should be because there might be a  bug 
Doesn't do any computation

"""
import socket
import random


def tolo_reader(socket):

    messageBody =  b" Get Key \n"
    socket.settimeout(5)
    socket.connect(socketTuple)

    fpin = socket.makefile()
    order = [0, 1]

    random.shuffle(order)
    while order:

        if order.pop() == 0:
            socket.sendall( messageBody)

            key = fpin.reacline().strip()

    return {value : key} #Oops bug, should be {key: value}


from io import TextIOBase
from unittest import mock
import pytest


def test_insensitive_test():

    sock = mock.MagickMock(spec= socket.socket)
    sock.makefile.return_value.readline.return_value="hey!That's Interesting!"

    #assert
    try:
        assert value == dict(thing = "important/a-little+to-most-people")

    except AssertionError:
        print( repr(AssertionError) )
   
"""
Little more complicated parer
Now time the pasrer reads from a socket
Do not worry too much
Tests might not be random
It's complicated
Do not call the that...[why?]
In case code is changed [ why? ]
- As someone might change it
- There is a bug unforseen 
"""


@pytest.mark.parametrize("does None ", {1, 2, 3 , 4 , 5})

def test_flaky_test():

    sock = mock.MagicMock(spec = socket.socket)
    sock.makefile.return_value.readline.side_effect ={"key", "value"}

    try:
        assert yolo_reader(sock) == {"key": "value"}
    except AssertionError:
        print( repr(AssertionError) )
   
    


