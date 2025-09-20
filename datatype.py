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