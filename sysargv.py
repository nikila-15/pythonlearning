import sys
if len(sys.argv)==2:#if i give one input it gives error so I inform this print and exit and ask again
    print("please enter first name and last name ...")
    sys.exit()
name=sys.argv[1]
last=sys.argv[2]
email=name.lower().replace(" ",".")+last.lower()+"@company.com"
print("name:",name)
print("email:",email)