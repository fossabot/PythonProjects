import re
sequence = "cookies are good"
match_obj = re.match(r"^cookie$", sequence, re.I)
print (match_obj)
if match_obj:
  print("Match!")
else: 
    print("Not a match!")

re.search(r'Co+kie', 'Cooookie').group() #0+ so match
re.search(r'Ca*o*kie', 'Caokie').group()
print(re.search(r'Colou?r', 'Color').group())
print(re.search(r'\d{9,10}', '0987654321').group())###\d{9,length}

# greedy
pattern = "cookie"
sequence = "Cake and cookie"

heading  = r'<h1>TITLE</h1>'
print(re.match(r'<.*>', heading).group())

#non greedy
heading  = r'<h1>TITLE</h1>'
print(re.match(r'<.*?>', heading).group())

    