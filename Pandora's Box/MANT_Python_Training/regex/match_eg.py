import re

#match
#list = ["guru99 get", "guru99 give", "guru gelenium"]
#for element in list:
    
#    z = re.match(r'(g\w+)\W(g\w+)', element)
#    if z:
#        print((z.group(0)))
#        print((z.group(1)))
#        print((z.group(2)))
#        print ("\n")

       
##search    
#patterns = ['software testing', 'guru', 'manoj']
#text = 'software testing is fun guru99?'
#for pattern in patterns:
#    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
#    if re.search(pattern, text):
#        print('found a match!')
#    else:
#        print('no match')
#else:
#    print ("After for loop execution")

##findall
#abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
#print (type(abc))
#emails = re.findall(r'[\w.-]+@[\w.-]+', abc)
#for email in emails:
#    print(email)

#sub
#phone = "2004-959-559 # This is Phone Number"

## Delete Python-style comments
#num = re.sub(r'#.*$', "", phone)
#print ("Phone Num : ", num)

## Remove anything other than digits
#num = re.sub(r'\D', "", phone)    
#print ("Phone Num : ", num)

#compile
pattern = re.compile(r"cookie")
sequence = "Cake and cookie"
pattern.search(sequence).group()
