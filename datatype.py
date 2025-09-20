#numeric 1.int 2.float 3. complex
a=18
b=9.56
print(a,b,type(a),type(b))
#boolean 
life=True
n=10>2
print(life,n,type(life),type(n))
#string 
f="day1 sept 18 "
print(f,type(f))
#none
m=None
print(m,type(m))

''' scope of variable  l...local variable ,e...Enclosing variable ,g....gloBAL variable,b...builtin variables
 '''
'''
#local variable 
def local():
    t=9
    print("local is :",t)
local()
print(t) #local variable scope is only calling by inside of function so it gives error
'''
#Enclosing variable 
def card():
    v=54
    print(v)
    def counter():
        print("it print this v",v)#why this is print v but v is not inside this function?because child uses parent variable also in simple nested variables allow to use
        counter()
card()
#global variable 
name="Bub"
def home():
    print("welcome ",name)
def user():
    print("username is ",name)
home()
user()#both will use name coz its a global variable 
#Built in 
print(__file__)#this __file__ will print path of file


#use case of scope of variable
partner="Swiggy" #global variable
def food():
    quantity=6 #enclosing variable
    def name():
        fname="parotta" #local variable
        print(f"the online delivery partner name is {partner} and they ordered {quantity} {fname}")   
    name()
food()

""" type casting when place it does and when place it doesn't ..
there are two type conversion 
1.Implicit conversion 
2.Explicit conversion
"""
#converting different data type into common data type is called imlicit or coercion
h="wow"
print(type(h))
#2.done by user requirements
ant="10"
insects="23"
print(type(ant))
cast=int(ant)
print(type(insects))
print(type(cast))
#when is use?
#print(cast+insects) error
print(cast+int(insects))
#when doesnt type casting
x="a"
b="e"
print(x+b)
d="2.2"
#print(int(d)) #it doesnt type cast coz inside the string is float ...only possible when it is original type
print(float(d))