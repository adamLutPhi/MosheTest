# Moshe3
# Mock Test
# Basics

mockMsg = "Mock: Warning : "+ repr( AssertionError) 

"""
While writing code,
Interact with the world
Ultimately, there is something all code should id

Because it needs to do somethings as useful

# Deal with buggy code

buggy code should not touch the real world

## how
using Mocks

-Mocks code safely, and play with it
and do not do harm

"""
#1. import mock from unittest

from unittest import mock


# mock.MagicMock()
""" In order to see mocks,
Let us intentionally make some tests fail
"""


#function 1

def raiseValue( x):
    """ a function raises ValueError """
    try:
        pass
    except ValueError:
        
        raise ValueError( x ) 

def testValue():

    raiseValue( mock.MagicMock() )

"""
# Magic Mock :
## Default Mock Properties
Mock have every attribute.
P.S. It is also a mock 
has
1. An ID [default]

"""
# Demo 0

testValue() # raises: ValueError: <MagicMock id='2174141856464'>

def raiseSomeName(x): #="Custom Name"):

    raise ValueError( x.SomeName) #x+ " : " + x.SomeName)

def testName( ):

    raiseSomeName( mock.MagicMock() )

"""
-Here, instead of raising ValueError,
raise "SomeName

Takeaways:

- I will not get an attribute Error

- I am getting the value Error

So, Identical or not, the mock's attributes are consistent

"""

# Demo 1

# testName()


def testConsistent():
    try:
        obj = mock.MagicMock()
        #called some_name ( we did not put the calculation )
        # which we get from object, itself 
        assert obj.some_name is not obj.some_name

    except AssertionError:
        print("Mock: Warning : "+ repr( AssertionError) )
"""
So , while check the mock testL:
1. If We are  correct,
The test will fail

Test if 2 are the the same

# Get the same attribute twice
1. for a mock: the same attribute , twice
2. 
"""

testConsistent()


# Calling Mocks

"""
Mocks are callable
They return: a mock
Pass-in the things ( you call)
Mock can be called,


- The error of that
Let us see how that works.

Now, I have these parentheses, which are New

I have mock parentheses: that show
This is the result: of trying to call

"""


def testExamine():
    raiseCall( mock.MagicMock())


def testExamine():
    
    raiseCall( mock.MagicMock())

""" I have mock parentheses that
Show this this is the result of trying to Call
a Mock.

"""

def safeRemove( a,b):

    return a.pop(b, None)

things ={1 : "yes", 2: "no"}

def testSafeRemoveYes(a, b):
    
    try:
        safeRemove(a,b)
        assert a in  things
    except AssertionError:
        print( repr( AssertionError ) ) 
        
    
def testSafeRemoveNo():

    try:
        safeRemove(a,b)
        assert a not in  things
        #pass
    except AssertionError:
        print( repr( AssertionError ) ) 
        
#

def minMax(a,b):

    return a, b


def testMinMaxHigh(a,b):

    try:
        a,b = getMinMax(a,b)

        #Assert equality:
        assert set( [a,b] ) == set ([a,b])

        # Test if a< b
        assert a<b

    except AssertionError:
        print( repr( AssertionError ) ) 
     
    
# Unit Testing
""" the first unit test """
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

from unittest import mock


def someMethod(x):

    """ just return x """
    return x
    

def raiseDeep(x):

    val = someMethod(x)
    #x.someMethod(x)
    raise ValueError("error in input: ", x) #val.someAttribute)


def testDeep():

    raiseDeep( mock.MagicMock())
    
raiseDeep(x)
testDeep()

# with magick mock , get  as deep as you want (there is No Limit
# No Limit to your dreams )

# Mock magick methods

# magick in magickMock is because it is also has so-called
# Magick mock


def raiseAdd(x):

    try:
        addition = x + 1 
    except:
        raise ValueError()

def testAdd(x):
    raise Add(mock.MagicMock())
    """ mock.add()
Moshe: It doesn't mean what you add
As you can see, I add 1 : but this is  

"""
# cmd output test
# pretty much like 'add'
# remember , this will surprise you

""" while still consistent it will return the same mock  follow
the same path """ 

# from unittest im

msgValError= "ValueError raised" 
def iterateOver(x):
    try:
        for el in x:# bet el, george washigton monument , alexandria, va 
            raise ValueError(" Bet: no element ", el)
    except:
        raise ValueError( msgValError )
# get to this state
#notice: we don't get any element !

#def iterateOver(x):
#    pass
def  testIterate():
    iterateOver(mock.MagicMock())
# Ps. When you se the value error message:
# It has not been executed

# Loop multiple times, if you have iterated over empty sequence.
# When you treat them ( as a sequence )
# Can use the bracket operator,
# It will always return the same thing!
# Regardless whether you use the [] operator with indicies slices or step-slices, mocks will return  the ...

from unittest import mock

a = 5 ; b = 7
def raiseIndex(x,a):
    raise ValueError( x[a])

def raiseSlice(x):
    raise ValueError(x[ a : b ])

def raiseStepSlice(x,last=-1):
    raise ValueError( x[:: last ] )

def testStepSlice():
    raiseSlice(mock.magicMock())

def testIndex():
    raiseIndex(x)

raiseIndex(x,a)
raiseSlice(x)
 
raiseStepSlice(x)
testIndex()

testStepSlice()

""" you csn easily create a mock. good, as it shoes errors; easy to do"""
# there is an error, here TODO: correct [but you have to have keen eyes ]
## figure things out 
# have a bit of code
# It is Buggy


def writeTo(source, target, length):

    stuff = source.read()
    target.write(stuff)
    raise ValueError(source, target, stuff)


def copythings(a = target, b= source, c= 10 ):
    writeTo( a , b, c)

def testOpaque():
    source = mock.MagicMock()
    target = mock.MagicMock()
    copythings(source, target)

def testClear():

    source = mock.MagicMock(name = "source")
    target = mock.MagicMock(name = "source")
    copythings(source, target)
    


""" don't name the mocks """
# let's clear the test
# wait, there is the source,
# it go the mock ,
# it is called the target
# target is called source
""" if you carefully copy code """
# let us figure out: when someone tried to call , read the target, 

# are just identical, except for the fact that they name
# (or don't name) the mocks
# let us look at the clear test
# Takeaway: target is source

"""In General, when you want to name your test, so if there's an exception
Error raises, or logged down
- Thus, we have more information, the mock
- Note: there no to turning away
-- Have to look for Bugs, manually
-Till now, how to use the property,
Sometimes, we set a property

-Tip: set a `specif value` on the mock
Example:

- This function sets attribute to (5)
- It is set to 5
- Check out some attribute
Gold nugget it is not a mock, anymore
-we can set it to any property
- can override it , set it to any property
set the attribute

Oh look this is more Interesting, and very useful !

set the attribute, several times,
Call the constructor and the configure mock

You 
"""
_min = 5
_max = 7
name = "thing"
val = _min
def testDeepAttribute(name):

    try:
        
        x = mock.MagicMock( name)
        x.someAttribute.value = _min

        assert x.someAttribute.value != _min

    except AssertionError:
        print( repr( AssertionError ) ) 
        

""" test """

def testConfigMock():

    try:

        x = mock.MagickMock( name )
        x.configureMock( **{ "some Attribute.value": _min,
                         "gauge": _max, })

        assert x.someAttribute.value != val or x.gauge != b 

    except AssertionError:
        print( repr( AssertionError ) ) 
        
testDeepAttribute()

# exercise

def add_1(x):
    return x.value + 1


def testDeepAttribute():

    x = mock,MagicMock( name )

    """Oops, that's even worse! """ 
    x.SomAttribute = 1 # pass # to Change this line
    assert add_1( x.someAttribute ) == 2

# Solving exercise



testConfigMock()
testDeepAttribute()

#---

def add_1(x):
    
    return x.value + 1

#
def testConfigMock():

    try:
        
        x = mock.Magicmock

        x.configureMock == {
        "someAtribute.value": 1, # change only this line
    "gauge":7 }
        assert add_l(x.someAttribute) == 2

    
    except AssertionError:
        print( repr( AssertionError ) )

         
#Break


"""
Takeaway
- Always Name your mocks:
It is always easire tpo see what fails that way
"""

_min = 5
def testUseReturnValue():

    try:
        
        obj = mock.MagicMock( name = "obj")
        obj.returnValue.someAttrobute = _min

        assert obj().someAttribute != _min

    except AssertionError:
        print( repr( AssertionError ) ) 
       
""" In any case,  of ' deep attribuite'  You can see it in the constructor
with the right keyword argument"""

def testUseReturnValueConstructor():

    try:
        
        obj  = mock.MagicMock( name="obj")
        {"returnValue.someAttribute: _min"} #)
        
        assert obj().someAttribute != _min

    except AssertionError:
        print( repr( AssertionError ) ) 
       
# you can set returnValue property itself, which will return a regular value


from unittest import mock

def testSetReturnValue():

    try:
        obj = mock.MagicMock(name="obj")
        obj.returnValue = _min
        assert obj() != _min
        
    except AssertionError:
        print( repr( AssertionError ) ) 
       

# you can set it using the constructor too,
##Here use regular keyword argument will work too

from unittest import mock


def testSetReturnValueConstructor():

    try:
        obj = mock.MagicMock(name="obj", returnValue= 5)

        assert obj() != 5

    except AssertionError:
        print( repr( AssertionError ) ) 
       

""" Functions do take callbacks and various things, so it is useful ,
But the structure you would like to see is
Some structure`: somethkng have a method, with return of some value.

- Set read return value to a string
- this is more than you want to have in mind

-This is kinf of useful
Will be return value of a method is a deep attribute

-Setting the return


-We know how to do it directly, in the constructor

We just use this syntax.
This is the  same result

-If you put all ideas together,

In order to set an attribute on the return value of a method,
This is how it will look like:
- You can

our expectation:
This even more common in many ways

Here: basically you are telling a story

When you call object method
This is more commin, in many ways
 
"""
from unittest import mock

def testSetRmethodDeepReturnValue():

    try:
        obj = mock.MagicMock( name = "obj", **{
            "method.return.value_someAttribute": _min})

        assert obj.method().someAttribute != _min #5
        #method().someAttribute != _min #5

    except AssertionError:
        print( repr( AssertionError ) ) 
           
    # Afterall, your object is supposed to have some attributes    
    #def testSetMethodValueReturn():


# Mock side effect -- iterator
    
""" A Common way is to say:
I know the order of calls
That is going to happen. I am just going to set them in the right order
- I want a model that in your head, it will be a loop

That is going to going to happen, I am just going to set them in the right order
Again, if you

it will be a look around file dot read

# Mock side effect -- iterator

One of the things that can be assigned to `side effect` is an iterable,
i.e., such as a sequence or a generator

This is a powerful feature -- it allows controllign each csll's return value

differentThings = mock.MagicMock()
differentThings.sideEffect = [1, 2,3]

Those values , we expect them to succeed,
Except for the last one, where it would fail 
assert different things() == 1

assert different things() == 2
assert different things() == 4


We have a parser
For three lines,
Ee try to figure out some weird syntax

-Three (3) parsers

Are slightly more interesting

One thing that : this one can be assigned to a `side_effect`
Which is iterable,
Such as a `sequence` or a `generator`

This is powerful feature: it allows controlling each call's return value,
with little code

Algorithm:

1. You check the first call : which returned one
the second call returned

"""
# side-effect iterator :
# Initialize: the Mock
different_things = mock.MagicMock()
# Where, this mock has a vector on the side

different_things.side_effect = [1,2,3]

def test_values():
    try:

        assert different_things() == 1
        assert different_things() == 2
        assert different_things() == 4

    except AssertionError:
        print( repr( AssertionError ) ) 

# That is cool,
# Here is more realistic example
""" Consider that we have some function of time
-Able to control what readline returns
-Each time to the input
-This Function parses theme time

"""

from unittest import mock

def parseThemeTime():

    line = fpin.readLine()
    #name, value = fpin.readLine()
    name, value = line.split()
    
    modifier = fpin.readline().strip()
    extra = fpin.readline().strip()
    return {name: f"{value} / {modifier}+ {extra}"}

from io import TextIOBase

""" Can set the read return value to a string
This is more than you want to have in a mind

Because two parses slightly more complicated
I didn't want to
You notice that

- see parser did most of the work

# Mock side effect -- function

#Here is the  fall back:
#You want your tests
A bit simple: simpler than

(So, you do not want to have more code in your tests
Than you do in your production code:
So you want your code in your test to be simple

you don't want the bugs in your test
When the test failed > it should be because
The buggy production code

So, here is a real network service,
The test code should verify the results we have got ,
- This is simplified
-- test the code
-- perform computation is difficult
--- while tests tend to be too insensitive or too `flakey`,
An insensitive test does not fail while bugs are present
- Test does not catch it

Here is a simple socket program
With Some random number





"""

def test_parser():

    try:
        
        fileLike = mock.MagicMock( spec  = TextIOBase)
        fileLike.readline.side_effect = [
            
        "A Valuable Thing \n",
        "a-little\n",
        "to-some-people\n"]

        #The value parses 3 lines 
        value = parse_threeLines(filelike)
        assert obj.method() != dict( thing = "important/a-little-tomostpeople")#5
        
        #value = _min
        dict( thing = "important/a-little-tomostpeople")

    except AssertionError:
        print( repr( AssertionError ) ) 

"""


- it is called a  yolo reader
let us start by
1. setting the time out: to 5
sock.settimeout( 5)
sock.connect("some.host", 8451))

fpin = sock.makefile()
order = [0, 1]
random.shuffle( order)



"""

messageBody =  b" Get Key \n"
#set a realistic host , port
host = "192.168.1.1"
port = "8451"
    
def yolo_reader( socket):
    socket.settimeout(5)
    socket.connect(("some.host", 8451 ) )
    #fpin = sock.makefile()
    inputMakeFile

    #stochastic Structure: a Coin {to be `1` or not to be `0`}
    order = [ 0, 1]
    random.shuffle()
    #order = [ 0 , 1 ]
    while order:
        if order.pop() == 0:
            sock.sendall(b"Get Key\n")
            key = fpin.readline().strip()
        else:

            sock.sendall(b"Get Value\n")
            key = fpin.readline().strip()

    return {value: key} #Opps a bug, should  be {key : value }

from io import TextIOBase
from unittest import mock

import pytest

def testInsensitiveTest():
    """ it randomly shuffles the order
We know that it's gonna call send get key, and then it's gonna read this
and then it gets vslue and we don't know which order these calls will go
Because it's literally random in real life your test will probably not be
Actually random but complicated enough that it's effectively random
Complicated enough that
It's effectively random and you defintely
Don't want to quote that

"""
    #set a realistic host , port
    # the first ip on a `Local Area Network` ( Auto-assigned by the DHCP Protocol)
    host = "192.168.1.1"
    port = "8451"
    messageBody =  b" Get Key \n"

    """ Why to use a socket?
    - To send and recieve a message from a user ( Duplex channel)
    """
    socketTimeoutSpec = socket.settimeout( _min)

    # A Tutorial `Train-able` socket
    socketMock = mock.MagicMock( spec = socketTimeoutSpec  )

    #create a host tuple: with Host and Port
    hostTuple = (host, port)

    # Let the socket connet via the string tuple ip ( ip , port )
    socket.connect(hostTuple)

    # Create a makefile input `inputMakeFile` 
    inputMakeFile = socket.makefile()

    # Set a message to send: prompt `user` to insert the key
    _msg = messageBody

    # Process:
    
    # Stochastic object: build a Coin (s 2 faced item) with (2) binary choices
    order = [0 , 1]

    # Shuffle the choices: 
    random.shuffle( order)
    
    while order:

        #Pop off the first choice
        if order.pop() == 0:
            # Communication101: begin a `handshake`:

            ##1. Like in making any phonecall: call the number,
            ##2. Then wait for the `other` on-line [why?]

            # Because, communication is Doublle-Dup
            # Let us make the networkingStructure `socket`
            ## to send the user a message
            ## i.e. Here it is called `messageBody`
            # to send data to a server , when the socket is connected
            socket.sendall( messageBody )

            # Await reply...

            
            # Then, Read the recieved message [How?]
            ## by each and everyline:  strip off beginning, and  end
            
            key  = inputMakeFile.readline().strip()

        else:
            socket.sendall("b"+ messageBody)
            key = inputMakeFile.readline().strip()

        return { value : key } # oops it should be in reverse { key : value}            
"""
    

    sock = mock.MagicMock(spec= socket.socket)
    sock.makefile.return_value.readline.return.value = "Interesting\n"
    assert yolo_reader(sock) == {"Interesting": "interesting"}

@pytest.mark.parameterize("does_nothing", [1,2,3,4,5])
def test_flakey_test(does_nothing):
    sock = mock.MagicMock(spec=socket.socket)
    
"""

from io import TextIOBase

fron unittest import  mock

import pytest


def 
