#THIS IS THE DAY ONE OF ME LEARNING PYTHON FROM SCRATCH 
#SO INSTALKED PYTHON IN MY DEVICE 
#FIRST LET'S KNOW SOME FACTS OR WE CAN SAY THINGS ABOUT PYTHON "PURELY FOR KNOWLEDGE".
#PYTHON WAS INVENTED BY GUIDO VAN RUSSUM HE IS DUTCH PROGRAMMER 
#THE PYTHON IS DERIVED FROM THE PROGRAMMER'S FAVIROTE SHOW MONTY'S FLYING PYTHON CIRCUS.
#THE FIRST VERSION OF PYTHON IS RELEASED ON 20 FEB 1991.

#WHY PYTHON?
#PYTHON PROGRAMMING LANGUAGE IS SAMEWHAT EASY BECAUSE ITS CLOSE TO HUMANLANGUAGE(ENGLISH).
#ITS EASY TO LEARN
#CURRENTLY PYTHON HAS A LOT OF DEMAND AND ALSO IT HAS AI APPLICATIONS AS WELL
#ALSO IT'S USED BY A LOT OF COMPANIES.

#SO LETS DIVE INTO OUR FIRST PYTHON CODE WHICH IS "PRINT()"

#PRINT IS A FUNCTION THAT IS PROVIDED BY PYTHON WHICH IS USED TO SHOW TEXT/OUTPUT ON THE DISPLAY LETS RUN IT AND SEE!

print("hello_world!")#NOTE:I KNOW THAT YOU GOT A DOUBT LIKE WHY THE WORD IS QUOTED AND OTHER THINGS WE CAN GET TO THEM LATER.
#NOW RUN IT BY USING THIS COMMAND "python day-1.py" day-1.py is file name so please replace that with your file name
#chack if your are in the currect folder or not in your terminal 

# NOW LET'S GET TO BUSINESS
# DATATYPES 

# DATATYPES ARE USED TO CATEGORIZE VALUES THAT ARE STORED IN A VARIABLE SO THAT PYTHON KNOWS WHICH TYPE OF DATA
# WHICH HELPS PROGRAM EXECUTION IN PYTHON

# THERE ARE A TOTAL OF 8 TYPES IN PYTHON:
# 1.NUMERIC
# 2.TEXT
# 3.BOOLEAN
# 4.SEQUENCE
# 5.MAPPING
# 6.SET 
# 7.BINARY
# 8.NONE

# NUMERIC DATA TYPE 
# NUMERIC TYPE IS A BASIC DATATYPE THAT IS USED IN PYTHON 
# IT INTEGERS, FLOATIONG(DECIMAL) VALUES ,AND COMPLEX NUMBER 
# THESE ARE REPRESENTED UDING THE FOLLOWING KEYWORDS
# INT --> INTEGERS
# FLOAT --> DECIMALS
# COMPLEX --> COMPLEX NUMBERS

# NOW LETS SEE SOME EXAMPLE CODE FOR THEM
Integer = int(1)
Float = float(1.1)
Complex = complex(1+2j)

print(type(Integer))
print(type(Float))
print(type(Complex))


# you should get the following as an output
# 30-days-of-python> python day-1.py
# hello_world!
# <class 'int'>
# <class 'float'>
# <class 'complex'>

# TEXT DATATYPE

# IN TEXT DATATYPE IS USE USED TO REPRESENT WORDS AND SENTENCE 
# THE WORDS OR SENTENCES THAT ARE WRITTEN WITHIN DOUBLE QUOTES IS CALLED A STRING 
# EXAMPLE: "HELLO_WORLD!"

a = "hello world"
print(a)
print(type(a))

#BOOLEAN 
#BOOLEAN IS USED TO REPERESENT TRUE OR FALSE AND 0 OR 1

VALID = True 

#SEQUENCE DATATYPE 

#SEQUENCE DATATYPE IS USED TO STORE MULTIPLE SIMILAR DATA IN A SINGLE METHOD 
#IN SEQUENCE DATATYPE IT HAS LIST, TUPLE , RANGE

#LIST
#LIST IS USED TO STORE MULTIPLE DATA POINTS IN SINGLE VARIABLE 
#IT IS ORDERED AND MUTABLE (CHANGABLE)

LIST = ["HELLO","WORLD"]
print(LIST)

#TUPLE

#TUPLE ARE SIMILAR TO LIST BUT THESE ARE IMMUTABLE(UNCHANGABLE)

tuple = ("hello","world")
print(tuple)

#RANGE

#RANGE IS BUILT IN FUNCTION IN PYTHON THAT USED TO COUNT UPTO A RANGE in integers
#range(start,end,step)
#start decides the starting value default = 0
#end ddetermines the n-1 value def has to decide the value
#step is how many steps it has to take like increament and decreament default = 1step
for i in range(0,5,1):
    print(i)

#MAPPING DATATYPE

#DICTNORY IS A MAPPING DATATYPE 
#THE KEY DEFINING CHARACTER OF MAPPING IS IT AS KEY:VALUE PAIR 

dict = {"year":2026}
print(dict)

"""
SET

set is an unordered collenction of list it has two types of sets 
1. set
2. frozenset syntax = frozenset({1,2,3})

the difference detween set and frozen set is set is mutable and frozen set is immutable
"""

Set = {1,2,3,3,2,4,5}
print(Set)

#output: {1, 2, 3, 4, 5}

# BINARY DATATYPE

# BINARY CONSISTS OF 0'S AND 1'S 
# THE BINARY ARE USED IN HANDLING THE RAW DATA
# 1.byte
# 2.bytearray
# 3.memoryview

# byte

# Syntax: Defined using a b prefix before a string literal.
# Behavior: Once created, you cannot alter any byte.

# bytearray

# A bytearray is the mutable counterpart to bytes. Think of it as a list of integers (0-255) that you can alter, append to, or delete from directly in memory.
# Syntax: Created using the bytearray() constructor.
# Behavior: Highly efficient when you need to constantly modify binary data in place (like processing a streaming video file buffer).

# memoryview

# A memoryview object allows Python code to access the internal data of an object that supports the buffer protocol (like bytes or bytearray) without making a copy.

#byte
b_data = b"Hello"
print(b_data)

# bytearray
mutable_data = bytearray(b"Hellx")
mutable_data[4] = 111
print(mutable_data)

#memoryview
data = bytearray(b"Hello World")
view = memoryview(data)
view[0] = 74  # ASCII for 'J'
print(data)  # Output: bytearray(b'Jello World')


# completion of my day-1