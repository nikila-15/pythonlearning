import sys
name=sys.argv[1]
email=name.lower().replace(" ",".")+"@company.com"
print("name:",name)
print("email:",email)