a="python is a programming "
b="language"
print(a+b)#concatenation
print(a*5)#repeatation
print("nikila and pooja" in a)#member operator in
print("python" not in a)#member operator not in
d="Pooja and nikila f"
print(d*10 )
print(a.upper())
print(d.lower())
print(b.capitalize())
print(d.title())
print("food"=="Food")#string comparison it compares using Ascii value 
print("n">"hill")
print("fig"!="pig")
print(min("food"))#builtin functions
print(max("fooxe"))
print(len(d))
print(d[5:18])
print(d[-2:])
print(d[::-1])
list1=['uni','ver','city']
j=" ".join(list1)
print(j)
o=" ".join([word[0].upper() for word in list1])#extract first letter in list by join and one line
print(o)
name="nikila kumar.-1234 jayanthi"
z=" ".join([tell[0].upper() for tell in name.split()])#extract first letter by split in string
print(z)
print((name.split("-")[1].split()[0]))#extracting 1234 from name
#join list,tuple,dictionary
list2=['u','n','i','v','e','r','s','e']
print("".join(list2))
print(" ".join(list2))
print("-".join(list2))
print("/".join(list2))
tuple1=('blue','black','pink')
print(" ".join(tuple1))
dic={'day':'15','year':'2001'}
print("-".join(dic))
#string traversing means access all the elements first to last
for e in d:
    print(e)
print(d.find("f"))#finding position of f in d
print(d.find(a,2,6))#start and end parameter
hel="  heho"
print(hel.strip())#remove front and back space by strip()
location="chennai"
print(location.replace("chennai","coimbatore"))#replace one by another ..old------>new
#counting word
print(len(d.split()))
po="polindrome palindrome"
print(po.rfind("o"))
print(po.count("in"))
print(po.index("n"))
print(po.rindex("n"))
print(hel.center(10,"*"))
print(hel.ljust(10,"*"))
print(hel.rjust(10,"*"))
#checking methods
check="1234niila"
check1="1234"
check3="nika"
check4="12"
print(check3.isalpha())
print(check.isalnum())
print(check1.isdecimal())
print(check4.isdigit())
