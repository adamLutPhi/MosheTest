#Moshe Z part 2
#requires (?)
## pip install pytest-diff ( an OOP package ) 

import pytest
import pytest_diff
from sys import stderr

"""
Lesson learned:

1. For every assert,
 - Define an assert and enclose it with `try-except` statement.
 - Sandwich it with a try , except statement,
    With the except handling the Assert Error

2. Lesson #1:  Know what you are expecting

3. Algorithm(testing):

4. If everything works, that is great

5. If some worked, then some has failed

    - Probably, I broke something ( in the code behind the test code )


6. for multiple Exceptions:  in the except statement :

    except [AssertionError, TypeError]


"""

##Seach statement
##statement has a truth value

"""Takeaway:
Because of assert function is built-in and independent from pytest, 
It is possible to use assert with out py test


np.random.randint(0,2,10)
>> array([0, 1, 1, 0, 1, 1, 0, 0, 1, 0])

"""

class Test1:
    
    #Field members:
    # tuple1 = ("apple", "banana", "cherry")
    tuple1 = tuple((0, 0))
    tuple2 = tuple((0,0))

    #tuple1(0, 0) , tuple2(0,0)
    lhs1 = 0
    rhs1 = 0
    
    lhs2 = 0
    rhs2 = 0

    #tuple2(1,0), tuple2(1,1)
    lhs1 = 1
    rhs1 = 0

    lhs2 = 1
    rhs2 = 1


    #tuple3(1,1) , tuple3(1, 0)
    lhs1 = 1
    rhs1 = 0

    lhs2 = 1
    rhs2 = 1
    
    def __init__(self, lhs, rhs):

        self.lhs = lhs
        self.rhs = rhs

@pytest_diff.registry.register(Test1)
def diff( x, y):
    return   [
            f"{x.lhs1} vs {y.lhs1}",
               f"{x.rhs1} vs {y.rhs1}",
               f"{x.lhs2} vs {y.lhs2}",
               f"{x.rhs2} vs {y.rhs2}",
           ]

# sandwich the test , passing: lhs1, rhs1 ,to asssertExcept then
#                   , passing: lhs2, rhs2 ,to asssertNExcept


    [ 
        f"asssertExcept( lhs1  , rhs1 )",
        f"asssertNExcept( lhs2 , rhs2 )",

        f"asssertExcept( lhs2 , rhs2 )",
        f"asssertNExcept( lhs1  , rhs1 )", 
]
    
#user given values
globalLhs = 2010
golablRhs = 2010 # 09
def test_car():
    x = Test1("x.rhs1", "x.lhs1",  globalLhs ) #2010)

    y = Test1("y.rhs1", "y.lhs1",  globalLhs ) #2010)



    lhs1Obj  = Test1("x.lhs1", "y.lhs1",  globalLhs ) #2010) # good implementation
    
    rhs1Obj = Test1("y.rhs1", "y.rhs1",  globalRhs )  #2009)

    assert lhs1Obj == rhsObj  #x == y

    
def asssertExcept(lhs , rhs):

    try:
        assert lhs == rhs  #1 == 0

    except AssertionError: #as e:
        print( repr( AssertionError ) )

def asssertNExcept(lhs , rhs):

    try:
        assert lhs != rhs  #1 == 0

    except AssertionError: #as e:
        print( repr( AssertionError ) )


#the point, does not involve this w
print( asssertExcept( 1 , 0 ) ) 

""" If answer is valid, return answer
else if we return None, then error has been raised
(seemingly, if error has been raised 
"""

# Redo with pytest



def testMath(lhs, rhs ):
    
    try:
        assert lhs == rhs
    except AssertionError: #as e:
        print( repr( AssertionError ) )


# uncomment me 
print( testMath(1, 0) ) 


# Reading assertion failures

# cmd command:

# cd \\ThisWorkingDirectory\\

# python pytest moshe2.py

""" the first part
runnning the output

Moshe:
" it is useful to see, use and check the output"
-especially with high verbosity
it will print each test

we only have one test ( which is 100%)

If I had 100 each one of those will increase the
percentage by one
the next part is the failure (details)
this is usually: the part I want"


- Responsibility: figure out what went wrong

- you have more than (1) failing test


shows you details about the failure
you see  


- Note:
others would see this:

1. in build Log
2. on the consiole

while the tactics are:

Algorithm(testing):

1. If everything works, that is great

2. If some worked, then some has failed

- Probably, I broke something ( in the code behind the test code )

"""

assertionErrorMsg=" AssertionError : Left Hand Side is not equal to the Right Hand Side "

ZeroDivisionErrorMsg= "ZeroDivisionError : the denominator is equal to 0\n"

assertionErrorMsgFull = lambda e: "Error - " + str( assertionErrorMsg )+"\nError Dump:\n"+ str(e)

e = "error Test-314"

print( assertionErrorMsgFull(e) ) 
def test_error( lhs,  rhs ):
    try:
        assert lhs == rhs #<-- AssertionError: 
    except AssertionError: #as e:
         stderr.write("Error - " + str( assertionErrorMsg )
              +"\nError Dump:\n"+  (repr( (AssertionError) )  ))

def test_succeed(lhs , rhs):
    try:
        assert lhs == rhs

    except AssertionError : #as e:
        stderr.write("Error - " + str( assertionErrorMsg )
              +"\nError Dump:\n"+  (repr( (AssertionError) )  ))

# For this error: it has another Error which it raises `ZeroDivisionError`
def test_fail(a, b):
    try:
        assert a / b == 0
    except ZeroDivisionError: #as e:
        stderr.write("Error - " + str( ZeroDivisionErrorMsg  #)
              + "\nError Dump:\n"+ repr( (ZeroDivisionError)  ) ) )
#Testing
a = 0 ; b  = 1 
#=======Block A =====
print( test_error( a , b) ) # handeled 

print ( test_succeed(a, b)) #<---- handeled
print( test_fail( a, b) ) #this won't fail (denominator is not 0
# but we can make it fail:

print( test_fail( a, 0) ) # this too, should fail (for dividing by zero)


""" Learn why the assertion has failed [ how? ]
As the assert statement won't get reached

Q. How is this important ?
A.

- When you have an exception
-- You will not get more (useful) information

-this will happen sometimes, if so,
- you will have  to debug it


- Try to plan your tests
-- So, if something goes wrong

- They will fail [ an assertion ]
-- Before doing something for unrelated reasons

- Defintion:
-- Test:

- Run your buggiest cde
-- They will find bugs

- When you the test, assume the code is very buggy
-- If a succeeding test is not mentioned ( in the summary)  

- Takeaway:
-- Because `Succeeding Test` is counted,
-- That is very useful!


- Even if you break all the code:

Takeaway:


--  We are not interested in our  Successes
--  We are Only Interested in our Failures


- At this point,
-- Let us see what Progress has been made

Last Words

1. A succeeding test is not mentioned (by name in the summary) but it is counted

2. A failre that is not caused by an assertion,is a lot less obvious

The first section

# the first section

we will cover is 
a "real-life scenarios" : 

# Equality 


The most popular

Expect a specidic task
- Unfortunately it has a bug

-- It returns the expected result with a small
"""

# the actual lesson starts 

error = 0.1 

def add(a,b):

    #result = error # error
    #result += a
    #result += b

    result = a + b + error
    
    return result


#Moshe's function
#1. Run the test: learn more about the raised error
#

def test_add():
    try:
        assert( 3, 4) == 7

    except AssertionError:  #as e:
        stderr.write("Error - " + str( assertionErrorMsg )
              +"\nError Dump:\n"+ repr( (AssertionError) ) )


def test_add2(a, b):
    """ Test the add function [How?]
    by testing whether the output of function equals the end value of addition 
    """
    try:
        
        assert(a, b) ==  a + b
    except AssertionError: #as e:
        stderr.write("Error - " + str( assertionErrorMsg )
              +"\nError Dump:\n" + repr( (AssertionError) )  )
     
        
test_add2( 3, 4)


# cmd command:

# cd ~\ thisWorkingDirectory


"""
Note: there are lots of subtleties to unpack

The test is
Comparing add() to the expected result
Because , presuma ble ,
This is what the function wass documented to do

-Not only it will fail, but they will fail in the same way,
But from the perspective of the test

This is how you want to write tests
While trying to know what went wrong

The test only checks add against  the document guarantees

-The Documents when you give add to arguments' sum : documented guarantees are very strict 

"""

def test_missing(a = [1] , b = []):

    try:
        assert a == b
    except AssertionError:  #as e:
        stderr.write("Error - " + str( assertionErrorMsg 
              +"\nError Dump:\n" + repr( (AssertionError) ) ) )
    
print( test_missing( [1] , []) )


def test_extra(a = [1] , b = [1,2]):
    try:

        assert a == b
    except AssertionError: #as e:
        stderr.write("Error - " + str( assertionErrorMsg 
              +"\nError Dump:\n" + repr( (AssertionError) ) ) )

def test_difference(a = [1,2,3] , b = [1, 4, 3]):
    try:
        assert a == b
    except AssertionError: #as e:
        stderr.write("Error - " + str( assertionErrorMsg 
              +"\nError Dump:\n" + repr( (AssertionError) ) ) )
test_extra(a, b) 

#def test_difference:

test_difference( [1,2,3] , [1,4,3])

    
        
""" information is crucial
want to have a god idea on what is going on
(Thus understanding of code )
1. Debug
2. Test

"""

def test_string():
    try:
        assert "hello\nworld" == "goodbye\nworld" #304 

    except AssertionError: # as e:
        stderr.write("Error - " + str( assertionErrorMsg 
              +"\nError Dump:\n" + repr( (AssertionError) ) ) )

test_string()


def test_string2():
    try:
        assert "saying "+ 10 +"hello world" + " said" + 10  == "saying"  "goodbye\nworld" + "said" #304 

    except AssertionError : #as e:
        stderr.write("Error - " + str( assertionErrorMsg 
              +"\nError Dump:\n" + repr( ( AssertionError ) ) ) )

def test_set(a = [1,2] , b = [1,3]):
    assert set( a) == set ( b  )

# cmd command [ensure to have the ]:

# cd \ thisWorkingDirectory

#python 

#List Demo : 

""" raissing exception intentionally
is a very powerful way to `debug tests` [why?]

you know the exception will fail the test
and show you the output (regardless of what else is going on """
# just make sure test fails , if test doesn't fail with

# Tip -- inserting Exceptions
"""
Inserting exceptions into tests is a surprisingly good way to debug test failures

1. you can make sure the test fails: with an exception
2. the exception -> test failure output is the mst reliable output path

----
-provides a reliable test failure output

"""
#functions without assert

def subtle_manipulation( things, trim = 1 ):

    #trim = 1 #Error: should be 2
    #no assert 
    return things[ trim : -trim ]

def test_suble_manipulation( strHi="_hi_"):
    
    assert subtle_manipulation( strHi ) == strHi

def erroring_subtle_manipulation(things , trim = 1):

    """ A function without assert, returns valueError  """
    ret_value = things[ trim: - trim]
    # No assert
    
    raise valueError(things, ret_value, trim)
    return ret

def test_subtle_manipulation_2(strHi="_hi_"):
    try: 
        assert erroring_subtle_manipulation( strHi) == strHi
    except AssertionError:
        print("Exception ;  ",  AssertionError  )


        
"""this 'function' is  bit hard to read
the `erroring` shows both
(the error outputs the string ""hellow , as wrtten "

new behavior [Discovered!]
: insert the error, into a function
and how you got the right value
- this is a good way, when you debug your code
you are debugging , to literally insert bugs
into unknown
the best thing is order
- have some thing what it can be
(me: best to log error (with exception type  to recheck input )
Moshe: print function : trying displays the values (which it tries to compare)

"""
"""
Moshe: print function : trying displays the values (which it tries to compare)

"""

"""
i.e. inserting bugs, into unkown places
figure out what's going on

-The Equality is not the only assertion
--it is the most popular
there are other assertions
i.e.
For example:

# The inequality

- It is a help assertion, b ecause it does 2 things:
-- The only thing you can say about (2) things inequal.

- (not a lot of thing you can know ).
-- the diff cont. : as expected All you get is the values , but still useful

you expect a `diff`:
all you get the values, still, useful to see that

lhs = 1 !=  rhs = 1.0
Takeaway: this might indicate the nature of your problem
(indicating the type  mis-match )

- inequality is not for number
-- usefult to learn the expected output
here
a list where(1) is copy of another
the point: expected value:  function expects List equality

'it's good to see the output (contents of the list ) 
- regardless of how many steps, between that
-- actually, you will See the value
the list's value
x = [1,2, 3]

"""
# #the inequality

#code along :
# Lesson #1:  Know what you are expecting

x = [ 1, 2, 3]
def test_not_equal_lists(x):

    try:       
        assert x !=  x[:]
    
    except AssertionError:
        print("Exception: ",  AssertionError  )

#lhs = x
#rhs = x+ 1

def test_greater_or_equal( lhs, rhs): #test_greater_or_equal(lhs = x , rhs= x+ 1 ):

    try: 
        condition =  lhs  <= rhs

    #experimental : code is raised  due to `TypeError`
    except [AssertionError, TypeError] :
         print("Exception: ", AssertionError, TypeError  )


#Demo
         """
test_greater_or_equal(  x , x+ 1  )  # TypeError: can only concatenate list (not "int") to list
"""
smaller = {1,2,3}
bigger = {1,2}

def test_set_comparison( small = smaller , big = bigger ):

    try :    
        #condition = small  <= big
        #lhs = small
        #rhs = big 
        assert small == big

    except AssertionError:
        print("Exception: ",  AssertionError  )
    
def testLessThan( small =  smaller ,  big = bigger ):

    try:
        assert small & big <= big
    except AssertionError:
        print("Exception: ", AssertionError  )

def testAssertEqual( small =  smaller ,  big = bigger ):

    try:
        assert small & big == big
    except AssertionError:
        print("Exception: ", AssertionError  )

testLessThan({1,2} , {1,2,3}  )
testAssertEqual( {1,2} , {1,2,3}  ) 
#Testing: To Test go to cmd cd to this current python directory:
## There: ensure __main__.py exists on \\thisWorkingdirectory\\pytest


# takeaway: with set theory : make test much better
# @26:47

"""

- "It gets cionfusing, very easily"

The only thing you can tell about something is

If it is equal to something


"""

"""
In some cases, we want to verify the actual identity of objects
Note: the behavior of is on built-in consysany
"""
def testLoop(n):
    try:
        assert 5 in range(n)
    except AssertionError :
         print("Exception: ", AssertionError  )
         
def testNotLoop( n):
    try:
        assert 1 not in set( n)  #[1])
    except AssertionError :
         print("Exception: ", AssertionError  )


testLoop( 3)

testNotLoop( [1] )

a = [1,2,3]
b = [1,2,3]

def testIsIdentical(a,b):
    try:
        assert a is b
    except AssertionError :
         print("Exception: ", AssertionError  )


def testNotIdentical(a,b):
    try:
        assert a is not b
    except AssertionError :
         print("Exception: ", AssertionError  )

testIsIdentical( a, b)

testNotIdentical(a,b) 

"""
def testStringNotIdentical(a,b):
    try:
        
        assert a is Nort b
    except AssertionError :
         print("Exception: ", AssertionError  )
"""

# pytest special
# comparison chains

def testIsEqualChain( a, b ):
    try:
        x = [1,2,3]
        assert a == x ==  b # [1,2,3,4] #b
    except AssertionError :
        print("Exception: ", AssertionError  )


# Boolean
"""
The following method's test fails

As logic is complicated, it maybe interesting to test the function
-the final result: is to call the function

"""

def alwaysFalse( sth):
    return False

def testFalse( x ):
    try:
        assert alwaysFalse( x)
    except AssertionError :
        print("Exception: ", AssertionError  )

#Testing: To Test go to cmd cd to this current python directory:
## There: ensure __main__.py exists on \\thisWorkingdirectory\\pytest


# Exercise:

def safeRemove( a, b) :
    #pass # fix this line
    a.pop( b, None) #this makes the test pass 


things = {1 : "yes", 2: "no"}

def testSafeRemoveNo( things, ans = "No" , num= 2 ):

    safeRemove(things, ans )
    safeRemove(things, num ) # 2)
    assert num not in things

def testSafeRemoveYes(things, ans = "Yes", num = 2):

    safeRemove(things, ans)
    safeRemove(things, num )
    assert num not in things

# Demo:

testSafeRemoveNo( things, "No", 2 )

testSafeRemoveYes(things, "Yes", 2)

"""how to check if this works
run the diff class
to ensure both tests pass

"""


#Testing: To Test go to cmd cd to this current python directory:
## There: ensure __main__.py exists on \\thisWorkingdirectory\\pytest

testSafeRemoveNo( things ,"No", 2 ) 
testSafeRemoveYes(things , "Yes", 2)

#cmd:
# cd \\thisWorkingdirectory\\
# python pytest moshe2.py
    
#here:
""" the same thing:
1. run it
2. notice: one test fails
why?
function expects (2) things
(expected A < B

solution1:
by writing:
 max(a,b),min(a, b)
 fixes  test1 but not test2 [why?]

 A  < B

 min(a, b), max(a,b)

 this fixes the problem
 but in real life:
 some tests pass, some tests fail

 "be careful , as you fix one test not to harm others
 wrap-up:

 test includes (2) parts:
 1. Test Run: calls functions (or classes )
 2. Assertion : Assert : helps you verify

-this ends file 2 
"""
# MinMax
def getMinMax(a, b):

    #Line fixed
    return min(a, b), max(a,b)
    #return  max(a,b),min(a, b)

def getAssert(a,b):
    try:
        assert a<b
    except AssertionError :
        print("Exception: ", AssertionError  )


def testMinManHigh(a, b):

    a,b = getMinMax( a,  b)

    assert set([a,b] ) == set( [1, 2])
    getAssert( a,  b)


def testMinManLow(a, b):

    a,b = getMinMax( a,  b)

    assert set([a,b] ) == set( [1, 2])
    getAssert( a,  b)
    
